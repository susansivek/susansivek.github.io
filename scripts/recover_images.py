#!/usr/bin/env python3
"""
Audit remote images in posts, recover broken ones from the live
original_url page and/or the Wayback Machine, then self-host recovered
(and fragile Alteryx/Lithium) assets under assets/images/posts/.
"""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import mimetypes
import re
import socket
import threading
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
ASSET_ROOT = ROOT / "assets" / "images" / "posts"
REPORT = ROOT / "image-recovery-report.json"
AUDIT_CACHE = ROOT / "scripts" / ".image-audit-cache.json"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
TIMEOUT = 10
WORKERS = 16
POST_WORKERS = 4

IMG_MD_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
IMG_HTML_RE = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.I
)
ORIGINAL_URL_RE = re.compile(r'^original_url:\s*"?([^"\n]+)"?\s*$', re.M)

FRAGILE_HOST_HINTS = (
    "community.alteryx.com",
    "alteryx.com",
    "lithium.com",
)
SKIP_SCHEMES = ("data:", "blob:")

_ok_cache: dict[str, bool] = {}
_wb_cache: dict[str, str | None] = {}
_page_cache: dict[str, list[str]] = {}
_wb_lock = threading.Lock()
_page_lock = threading.Lock()


@dataclass
class ImageRef:
    post: str
    alt: str
    url: str
    kind: str
    status: str = "unknown"
    local_path: str | None = None
    recovered_from: str | None = None
    notes: str = ""


@dataclass
class PostResult:
    file: str
    original_url: str | None = None
    images: list[ImageRef] = field(default_factory=list)
    page_images: list[str] = field(default_factory=list)


def parse_front_matter_url(text: str) -> str | None:
    m = ORIGINAL_URL_RE.search(text)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def post_body(text: str) -> str:
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
    return parts[2] if len(parts) >= 3 else text


def slug_for_post(filename: str) -> str:
    stem = Path(filename).stem
    parts = stem.split("-", 3)
    return parts[3] if len(parts) == 4 else stem


def is_remote(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def is_fragile(url: str) -> bool:
    try:
        host = urllib.parse.urlparse(url).netloc.lower()
    except Exception:
        return False
    return any(h in host for h in FRAGILE_HOST_HINTS)


def html_unescape(s: str) -> str:
    return (
        s.replace("&amp;", "&")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
    )


def normalize_url(url: str, base: str | None = None) -> str:
    url = html_unescape(url.strip())
    if base:
        url = urllib.parse.urljoin(base, url)
    parsed = urllib.parse.urlparse(url)
    if "miro.medium.com" in parsed.netloc:
        return urllib.parse.urlunparse(parsed._replace(query="", fragment=""))
    return url


def request(url: str, method: str = "GET") -> tuple[int, bytes, str]:
    req = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        content_type = resp.headers.get("Content-Type", "")
        data = b"" if method == "HEAD" else resp.read()
        return resp.status, data, content_type


def looks_like_html(data: bytes, ct: str) -> bool:
    if "text/html" in (ct or ""):
        return True
    head = data[:300].lower()
    return b"<html" in head or b"<!doctype" in head


def url_is_ok(url: str) -> bool:
    if url in _ok_cache:
        return _ok_cache[url]
    if url.startswith(SKIP_SCHEMES):
        _ok_cache[url] = True
        return True
    if not is_remote(url):
        ok = (ROOT / url.lstrip("/")).exists()
        _ok_cache[url] = ok
        return ok
    ok = False
    try:
        status, data, ct = request(url, method="GET")
        ok = status < 400 and bool(data) and not looks_like_html(data, ct)
    except Exception:
        ok = False
    _ok_cache[url] = ok
    return ok


def fetch_text(url: str) -> str | None:
    try:
        status, data, _ct = request(url, method="GET")
        if status >= 400 or not data:
            return None
        return data.decode("utf-8", errors="replace")
    except Exception:
        return None


def extract_page_images(html: str, page_url: str) -> list[str]:
    urls: list[str] = []
    seen = set()
    patterns = [
        IMG_HTML_RE,
        re.compile(r'data-src\s*=\s*["\']([^"\']+)["\']', re.I),
        re.compile(r'data-original\s*=\s*["\']([^"\']+)["\']', re.I),
    ]
    for pat in patterns:
        for m in pat.finditer(html):
            raw = m.group(1).strip()
            if raw.startswith(SKIP_SCHEMES):
                continue
            low = raw.lower()
            if "pixel" in low or "1x1" in low or "spacer" in low:
                continue
            full = normalize_url(raw, page_url)
            if not is_remote(full) or full in seen:
                continue
            seen.add(full)
            urls.append(full)
    for m in re.finditer(r'srcset\s*=\s*["\']([^"\']+)["\']', html, re.I):
        first = m.group(1).split(",")[0].strip().split(" ")[0]
        full = normalize_url(first, page_url)
        if is_remote(full) and full not in seen:
            seen.add(full)
            urls.append(full)
    return urls


def wayback_closest(url: str) -> str | None:
    with _wb_lock:
        if url in _wb_cache:
            return _wb_cache[url]
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(
        url, safe=""
    )
    result = None
    try:
        status, data, _ = request(api, method="GET")
        if status < 400 and data:
            payload = json.loads(data.decode("utf-8", errors="replace"))
            closest = payload.get("archived_snapshots", {}).get("closest") or {}
            if closest.get("available") and closest.get("url"):
                snap = closest["url"]
                result = re.sub(
                    r"(https://web\.archive\.org/web/\d+)/",
                    r"\1id_/",
                    snap,
                    count=1,
                )
    except Exception:
        result = None
    with _wb_lock:
        _wb_cache[url] = result
    return result


def page_images_for(original_url: str) -> list[str]:
    with _page_lock:
        if original_url in _page_cache:
            return list(_page_cache[original_url])
    html = fetch_text(original_url)
    source = original_url
    if not html:
        wb = wayback_closest(original_url)
        if wb:
            page_wb = wb.replace("id_/", "/")
            html = fetch_text(page_wb)
            source = page_wb
    imgs = extract_page_images(html, source) if html else []
    with _page_lock:
        _page_cache[original_url] = imgs
    return list(imgs)


def guess_ext(url: str, content_type: str) -> str:
    path = urllib.parse.urlparse(url).path
    suffix = Path(path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}:
        return suffix
    ext = mimetypes.guess_extension((content_type or "").split(";")[0].strip())
    if ext == ".jpe":
        ext = ".jpg"
    return ext or ".img"


def download_to(
    url: str, dest_dir: Path, preferred_name: str | None = None
) -> Path | None:
    try:
        status, data, ct = request(url, method="GET")
    except Exception:
        return None
    if status >= 400 or not data or looks_like_html(data, ct):
        return None
    dest_dir.mkdir(parents=True, exist_ok=True)
    ext = guess_ext(url, ct)
    stem = preferred_name or hashlib.sha1(url.encode()).hexdigest()[:12]
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", stem).strip("-")[:80] or "image"
    name = stem if stem.lower().endswith(ext) else f"{stem}{ext}"
    dest = dest_dir / name
    if dest.exists():
        dest = dest_dir / f"{dest.stem}-{hashlib.sha1(data).hexdigest()[:8]}{ext}"
    dest.write_bytes(data)
    _ok_cache[url] = True
    return dest


def collect_posts() -> list[PostResult]:
    results: list[PostResult] = []
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        body = post_body(text)
        pr = PostResult(file=path.name, original_url=parse_front_matter_url(text))
        for m in IMG_MD_RE.finditer(body):
            pr.images.append(
                ImageRef(
                    post=path.name,
                    alt=m.group(1),
                    url=m.group(2).strip(),
                    kind="md",
                )
            )
        for m in IMG_HTML_RE.finditer(body):
            url = m.group(1).strip()
            if any(img.url == url for img in pr.images):
                continue
            pr.images.append(
                ImageRef(post=path.name, alt="", url=url, kind="html")
            )
        results.append(pr)
    return results


def audit_statuses(posts: list[PostResult]) -> None:
    urls = sorted(
        {
            img.url
            for pr in posts
            for img in pr.images
            if is_remote(img.url) and not img.url.startswith(SKIP_SCHEMES)
        }
    )

    cached: dict[str, bool] = {}
    if AUDIT_CACHE.exists():
        try:
            cached = json.loads(AUDIT_CACHE.read_text())
        except Exception:
            cached = {}

    to_check = [u for u in urls if u not in cached]
    print(f"Checking {len(to_check)} URLs ({len(urls) - len(to_check)} cached)...")

    def check(u: str) -> tuple[str, bool]:
        return u, url_is_ok(u)

    if to_check:
        with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
            for i, (u, ok) in enumerate(ex.map(check, to_check), 1):
                cached[u] = ok
                if i % 50 == 0 or i == len(to_check):
                    print(f"  checked {i}/{len(to_check)}", flush=True)

    AUDIT_CACHE.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_CACHE.write_text(json.dumps(cached) + "\n")
    _ok_cache.update(cached)

    for pr in posts:
        for img in pr.images:
            if img.url.startswith(SKIP_SCHEMES):
                img.status = "skipped"
                img.notes = "data URI"
            elif not is_remote(img.url):
                img.status = (
                    "ok" if (ROOT / img.url.lstrip("/")).exists() else "broken"
                )
            else:
                img.status = "ok" if cached.get(img.url) else "broken"


def try_sources(img: ImageRef, unused: list[str]) -> tuple[str | None, str]:
    base = Path(urllib.parse.urlparse(img.url).path).name
    if base and base not in ("", "/", "image", "serverpage"):
        for pu in list(unused):
            if base in pu:
                return pu, "original-page-name"
    if unused:
        return unused[0], "original-page-order"
    wb = wayback_closest(img.url)
    if wb:
        return wb, "wayback-image"
    return None, ""


def recover_for_post(pr: PostResult) -> PostResult:
    broken = [img for img in pr.images if img.status == "broken"]
    fragile_ok = [
        img for img in pr.images if img.status == "ok" and is_fragile(img.url)
    ]
    if not broken and not fragile_ok:
        return pr

    page_imgs: list[str] = []
    if pr.original_url and broken:
        page_imgs = page_images_for(pr.original_url)
        pr.page_images = page_imgs
    unused = list(page_imgs)
    dest_dir = ASSET_ROOT / slug_for_post(pr.file)

    for img in broken:
        preferred = Path(urllib.parse.urlparse(img.url).path).stem or "image"
        local = download_to(img.url, dest_dir, preferred_name=preferred)
        note, source = "direct-retry", img.url
        if not local:
            source, note = try_sources(img, unused)
            if source and source in unused:
                unused.remove(source)
            if source:
                local = download_to(source, dest_dir, preferred_name=preferred)
        if not local:
            wb = wayback_closest(img.url)
            if wb:
                local = download_to(wb, dest_dir, preferred_name=preferred)
                note, source = "wayback-image", wb
        if not local:
            img.notes = f"unrecovered-after-{note or 'none'}"
            continue
        img.local_path = "/" + str(local.relative_to(ROOT)).replace("\\", "/")
        img.status = "recovered"
        img.recovered_from = note
        img.notes = source or img.url

    for img in fragile_ok:
        preferred = Path(urllib.parse.urlparse(img.url).path).stem or "image"
        local = download_to(img.url, dest_dir, preferred_name=preferred)
        note = "fragile-host"
        if not local:
            wb = wayback_closest(img.url)
            if wb:
                local = download_to(wb, dest_dir, preferred_name=preferred)
                note = "wayback-fragile"
        if local:
            img.local_path = "/" + str(local.relative_to(ROOT)).replace("\\", "/")
            img.status = "mirrored"
            img.recovered_from = note
            img.notes = img.url
    return pr


def rewrite_posts(posts: list[PostResult]) -> int:
    changed = 0
    by_file: dict[str, list[ImageRef]] = defaultdict(list)
    for pr in posts:
        for img in pr.images:
            if img.local_path:
                by_file[pr.file].append(img)

    for filename, imgs in by_file.items():
        path = POSTS / filename
        text = path.read_text(encoding="utf-8")
        original = text
        for img in sorted(imgs, key=lambda i: len(i.url), reverse=True):
            if not img.local_path:
                continue
            if img.kind == "md":
                text = text.replace(
                    f"![{img.alt}]({img.url})",
                    f"![{img.alt}]({img.local_path})",
                )
            text = text.replace(img.url, img.local_path)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    socket.setdefaulttimeout(TIMEOUT)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    posts = collect_posts()
    total_imgs = sum(len(p.images) for p in posts)
    print(f"Posts: {len(posts)} | image refs: {total_imgs}", flush=True)

    audit_statuses(posts)
    broken = sum(1 for p in posts for i in p.images if i.status == "broken")
    ok = sum(1 for p in posts for i in p.images if i.status == "ok")
    print(f"Audit: ok={ok} broken={broken}", flush=True)

    targets = [
        p
        for p in posts
        if any(i.status == "broken" for i in p.images)
        or any(i.status == "ok" and is_fragile(i.url) for i in p.images)
    ]
    print(f"Recovery targets (posts): {len(targets)}", flush=True)

    lock = threading.Lock()
    done = 0

    def work(pr: PostResult) -> PostResult:
        nonlocal done
        result = recover_for_post(pr)
        with lock:
            done += 1
            n = done
        print(
            f"[{n}/{len(targets)}] {pr.file} "
            f"(page imgs={len(result.page_images)}, "
            f"recovered={sum(1 for i in result.images if i.status == 'recovered')}, "
            f"mirrored={sum(1 for i in result.images if i.status == 'mirrored')})",
            flush=True,
        )
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=POST_WORKERS) as ex:
        list(ex.map(work, targets))

    changed = rewrite_posts(posts)
    recovered = sum(1 for p in posts for i in p.images if i.status == "recovered")
    mirrored = sum(1 for p in posts for i in p.images if i.status == "mirrored")
    still_broken = [
        {"file": p.file, "url": i.url, "notes": i.notes}
        for p in posts
        for i in p.images
        if i.status == "broken"
    ]

    report = {
        "summary": {
            "posts": len(posts),
            "image_refs": total_imgs,
            "ok": ok,
            "broken_before": broken,
            "recovered": recovered,
            "mirrored_fragile": mirrored,
            "still_broken": len(still_broken),
            "posts_rewritten": changed,
            "asset_bytes": sum(
                f.stat().st_size for f in ASSET_ROOT.rglob("*") if f.is_file()
            ),
            "asset_files": sum(1 for f in ASSET_ROOT.rglob("*") if f.is_file()),
        },
        "still_broken": still_broken,
        "posts": [
            {
                "file": p.file,
                "original_url": p.original_url,
                "page_images_found": len(p.page_images),
                "images": [asdict(i) for i in p.images],
            }
            for p in posts
            if any(
                i.status in {"recovered", "mirrored", "broken"} or i.local_path
                for i in p.images
            )
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2), flush=True)
    print(f"Wrote {REPORT}", flush=True)


if __name__ == "__main__":
    main()
