#!/usr/bin/env python3
"""
Second-pass recovery for still-broken images:
1) Wayback Machine snapshot of the original article page
2) Republish twin posts (same title) that still have working remote images
3) Self-host anything successfully fetched
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
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
ASSET_ROOT = ROOT / "assets" / "images" / "posts"
REPORT = ROOT / "image-recovery-report.json"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
TIMEOUT = 12
WORKERS = 6

IMG_MD_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
IMG_HTML_RE = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.I
)
ORIGINAL_URL_RE = re.compile(r'^original_url:\s*"?([^"\n]+)"?\s*$', re.M)
TITLE_RE = re.compile(r'^title:\s*"(.*)"\s*$', re.M)

_wb_cache: dict[str, str | None] = {}
_page_cache: dict[str, list[str]] = {}
_lock = threading.Lock()


def request(url: str) -> tuple[int, bytes, str]:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"}
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.status, resp.read(), resp.headers.get("Content-Type", "")


def looks_like_html(data: bytes, ct: str) -> bool:
    if "text/html" in (ct or ""):
        return True
    head = data[:300].lower()
    return b"<html" in head or b"<!doctype" in head


def wayback_closest(url: str) -> str | None:
    with _lock:
        if url in _wb_cache:
            return _wb_cache[url]
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(
        url, safe=""
    )
    result = None
    try:
        status, data, _ = request(api)
        if status < 400 and data:
            payload = json.loads(data.decode("utf-8", errors="replace"))
            closest = payload.get("archived_snapshots", {}).get("closest") or {}
            if closest.get("available") and closest.get("url"):
                snap = closest["url"]
                # Keep HTML snapshot URL (not id_) for page parsing
                result = snap
    except Exception:
        result = None
    with _lock:
        _wb_cache[url] = result
    return result


def wayback_asset(url: str) -> str | None:
    snap = wayback_closest(url)
    if not snap:
        return None
    return re.sub(r"(https://web\.archive\.org/web/\d+)/", r"\1id_/", snap, count=1)


def normalize_url(url: str, base: str | None = None) -> str:
    url = (
        url.strip()
        .replace("&amp;", "&")
        .replace("&quot;", '"')
    )
    if base:
        url = urllib.parse.urljoin(base, url)
    # Unwrap archive.org wrapper if present as a normal img src
    m = re.match(r"https://web\.archive\.org/web/\d+(?:im_)?/(https?://.*)", url)
    if m:
        url = m.group(1)
    parsed = urllib.parse.urlparse(url)
    if "miro.medium.com" in parsed.netloc:
        url = urllib.parse.urlunparse(parsed._replace(query="", fragment=""))
    return url


def extract_page_images(html: str, page_url: str) -> list[str]:
    urls: list[str] = []
    seen = set()
    for pat in (
        IMG_HTML_RE,
        re.compile(r'data-src\s*=\s*["\']([^"\']+)["\']', re.I),
        re.compile(r'data-original\s*=\s*["\']([^"\']+)["\']', re.I),
    ):
        for m in pat.finditer(html):
            raw = m.group(1).strip()
            if raw.startswith("data:"):
                continue
            low = raw.lower()
            if "pixel" in low or "1x1" in low or "spacer" in low:
                continue
            full = normalize_url(raw, page_url)
            # Prefer unwrapped original asset URL when archived
            asset = normalize_url(full)
            if not asset.startswith("http") or asset in seen:
                continue
            # Prefer medium / wp / pecan / unsplash over alteryx lithium if both exist
            seen.add(asset)
            urls.append(asset)
    return urls


def fetch_text(url: str) -> str | None:
    try:
        status, data, _ = request(url)
        if status >= 400 or not data:
            return None
        return data.decode("utf-8", errors="replace")
    except Exception:
        return None


def page_images(url: str) -> list[str]:
    with _lock:
        if url in _page_cache:
            return list(_page_cache[url])
    html = fetch_text(url)
    imgs = extract_page_images(html, url) if html else []
    with _lock:
        _page_cache[url] = imgs
    return list(imgs)


def slug_for_post(filename: str) -> str:
    stem = Path(filename).stem
    parts = stem.split("-", 3)
    return parts[3] if len(parts) == 4 else stem


def guess_ext(url: str, content_type: str) -> str:
    path = urllib.parse.urlparse(url).path
    suffix = Path(path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}:
        return suffix
    ext = mimetypes.guess_extension((content_type or "").split(";")[0].strip())
    if ext == ".jpe":
        ext = ".jpg"
    return ext or ".img"


def download_to(url: str, dest_dir: Path, preferred_name: str) -> Path | None:
    # Prefer id_ wayback for binary fidelity if this is a soft archive URL
    candidates = [url]
    if "web.archive.org/web/" in url and "id_/" not in url:
        candidates.insert(0, re.sub(r"(web/\d+)/", r"\1id_/", url, count=1))
    # also try wayback of raw url
    wb = wayback_asset(url)
    if wb:
        candidates.append(wb)

    for candidate in candidates:
        try:
            status, data, ct = request(candidate)
        except Exception:
            continue
        if status >= 400 or not data or looks_like_html(data, ct):
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        ext = guess_ext(candidate, ct)
        stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", preferred_name).strip("-")[:80] or "image"
        name = stem if stem.lower().endswith(ext) else f"{stem}{ext}"
        dest = dest_dir / name
        if dest.exists():
            dest = dest_dir / f"{dest.stem}-{hashlib.sha1(data).hexdigest()[:8]}{ext}"
        dest.write_bytes(data)
        return dest
    return None


def norm_title(t: str) -> str:
    t = t.casefold()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def load_posts():
    posts = []
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        title_m = TITLE_RE.search(text)
        url_m = ORIGINAL_URL_RE.search(text)
        title = title_m.group(1) if title_m else ""
        original = url_m.group(1).strip().strip('"') if url_m else None
        body = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
        content = body[2] if len(body) >= 3 else text
        images = []
        for m in IMG_MD_RE.finditer(content):
            images.append({"alt": m.group(1), "url": m.group(2).strip()})
        posts.append(
            {
                "file": path.name,
                "path": path,
                "title": title,
                "norm_title": norm_title(title),
                "original_url": original,
                "images": images,
                "text": text,
            }
        )
    return posts


def is_local(url: str) -> bool:
    return url.startswith("/assets/")


def is_broken_host(url: str) -> bool:
    return any(
        h in url
        for h in (
            "community.alteryx.com",
            "lithium.com",
            "tandfonline.com",
            "journals.sagepub.com",
        )
    ) or (url.startswith("http") and not is_local(url) and False)


def twin_sources(posts, post) -> list[str]:
    """Working image URLs from republish siblings with the same title."""
    sources = []
    for other in posts:
        if other["file"] == post["file"]:
            continue
        if other["norm_title"] != post["norm_title"]:
            continue
        for img in other["images"]:
            u = img["url"]
            if is_local(u):
                # copy from local sibling path later
                sources.append(u)
            elif u.startswith("http") and not is_broken_host(u):
                sources.append(u)
        if other.get("original_url") and not is_broken_host(other["original_url"]):
            # scrape twin page
            sources.extend(page_images(other["original_url"])[:20])
    # dedupe preserve order
    seen = set()
    out = []
    for s in sources:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def main() -> None:
    socket.setdefaulttimeout(TIMEOUT)
    posts = load_posts()

    # Prefer using prior report for which URLs were broken
    prior_broken = set()
    if REPORT.exists():
        data = json.loads(REPORT.read_text())
        for item in data.get("still_broken", []):
            prior_broken.add((item["file"], item["url"]))

    targets = []
    for p in posts:
        broken_imgs = []
        for img in p["images"]:
            u = img["url"]
            if is_local(u):
                continue
            if (p["file"], u) in prior_broken or is_broken_host(u):
                # Double-check still remote fragile/broken host
                if u.startswith("http"):
                    broken_imgs.append(img)
        if broken_imgs:
            targets.append((p, broken_imgs))

    print(f"Pass-2 targets: {len(targets)} posts", flush=True)
    recovered = 0
    rewritten = 0
    details = []

    for idx, (post, broken_imgs) in enumerate(targets, 1):
        sources: list[str] = []
        # Wayback of original article
        if post["original_url"]:
            wb_page = wayback_closest(post["original_url"])
            if wb_page:
                sources.extend(page_images(wb_page))
            # Also try live page once more
            sources.extend(page_images(post["original_url"]))
        # Twin republish posts
        sources.extend(twin_sources(posts, post))

        # Filter junk / alteryx dead ends unless they're already local
        filtered = []
        seen = set()
        for s in sources:
            if s in seen:
                continue
            seen.add(s)
            if is_broken_host(s) and not is_local(s):
                continue
            filtered.append(s)

        unused = list(filtered)
        dest_dir = ASSET_ROOT / slug_for_post(post["file"])
        replacements: list[tuple[str, str]] = []

        for img in broken_imgs:
            preferred = Path(urllib.parse.urlparse(img["url"]).path).stem or "image"
            local = None
            note = ""
            # try wayback of exact image first
            wb_img = wayback_asset(img["url"])
            if wb_img:
                local = download_to(wb_img, dest_dir, preferred)
                note = "wayback-image"
            if not local and unused:
                cand = unused.pop(0)
                if is_local(cand):
                    # copy sibling local asset
                    src_path = ROOT / cand.lstrip("/")
                    if src_path.exists():
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        dest = dest_dir / src_path.name
                        if not dest.exists():
                            dest.write_bytes(src_path.read_bytes())
                        local = dest
                        note = "twin-local"
                else:
                    local = download_to(cand, dest_dir, preferred)
                    note = "twin-or-wayback-page"
            if local:
                rel = "/" + str(local.relative_to(ROOT)).replace("\\", "/")
                replacements.append((img["url"], rel))
                recovered += 1
                details.append(
                    {
                        "file": post["file"],
                        "from": img["url"],
                        "to": rel,
                        "via": note,
                    }
                )

        if replacements:
            text = post["path"].read_text(encoding="utf-8")
            original = text
            for old, new in sorted(replacements, key=lambda x: len(x[0]), reverse=True):
                text = text.replace(old, new)
            if text != original:
                post["path"].write_text(text, encoding="utf-8")
                rewritten += 1

        print(
            f"[{idx}/{len(targets)}] {post['file']}: "
            f"sources={len(filtered)} fixed={len(replacements)}",
            flush=True,
        )

    summary = {
        "pass": 2,
        "target_posts": len(targets),
        "recovered": recovered,
        "posts_rewritten": rewritten,
        "asset_bytes": sum(
            f.stat().st_size for f in ASSET_ROOT.rglob("*") if f.is_file()
        ),
        "asset_files": sum(1 for f in ASSET_ROOT.rglob("*") if f.is_file()),
        "details": details,
    }
    out = ROOT / "image-recovery-pass2.json"
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in summary if k != "details"}, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
