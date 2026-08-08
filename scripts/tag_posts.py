#!/usr/bin/env python3
"""Add categories, publication, and featured flags to post front matter."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

HOST_PUBLICATION = {
    "community.alteryx.com": "Alteryx Community",
    "alteryx.com": "Alteryx",
    "www.alteryx.com": "Alteryx",
    "pecan.ai": "Pecan AI",
    "www.pecan.ai": "Pecan AI",
    "towardsdatascience.com": "Towards Data Science",
    "www.towardsdatascience.com": "Towards Data Science",
    "kdnuggets.com": "KDnuggets",
    "www.kdnuggets.com": "KDnuggets",
    "medium.com": "Medium",
    "susansivek.medium.com": "Medium",
    "mediashift.org": "MediaShift",
    "www.mediashift.org": "MediaShift",
    "texasmonthly.com": "Texas Monthly",
    "www.texasmonthly.com": "Texas Monthly",
    "cjr.org": "Columbia Journalism Review",
    "www.cjr.org": "Columbia Journalism Review",
    "tandfonline.com": "Taylor & Francis",
    "www.tandfonline.com": "Taylor & Francis",
    "journals.sagepub.com": "SAGE Journals",
    "aejmcmagazine.arizona.edu": "Journal of Magazine Media",
    "digitalcommons.uri.edu": "Journal of Media Literacy Education",
    "papers.ssrn.com": "SSRN",
    "muse.jhu.edu": "Project MUSE",
    "ijoc.org": "International Journal of Communication",
    "www.ijoc.org": "International Journal of Communication",
    "mediacommons.org": "MediaCommons",
    "journal.community-journalism.com": "Community Journalism",
    "fs.hubspotusercontent00.net": "Pecan AI",
}

DATA_SCIENCE_HOSTS = {
    "community.alteryx.com",
    "alteryx.com",
    "www.alteryx.com",
    "pecan.ai",
    "www.pecan.ai",
    "towardsdatascience.com",
    "www.towardsdatascience.com",
    "kdnuggets.com",
    "www.kdnuggets.com",
    "medium.com",
    "susansivek.medium.com",
    "fs.hubspotusercontent00.net",
}

MEDIA_HOSTS = {
    "mediashift.org",
    "www.mediashift.org",
    "texasmonthly.com",
    "www.texasmonthly.com",
    "cjr.org",
    "www.cjr.org",
    "mediacommons.org",
}

ACADEMIC_HOSTS = {
    "tandfonline.com",
    "www.tandfonline.com",
    "journals.sagepub.com",
    "aejmcmagazine.arizona.edu",
    "digitalcommons.uri.edu",
    "papers.ssrn.com",
    "muse.jhu.edu",
    "ijoc.org",
    "www.ijoc.org",
    "journal.community-journalism.com",
}

FEATURE_HOSTS = {
    "texasmonthly.com",
    "www.texasmonthly.com",
    "cjr.org",
    "www.cjr.org",
}

# Slug substrings for curated favorites
FEATURED_SLUGS = {
    "both-facts-and-feelings-emotion-and-news-literacy",
    "the-contribution-of-city-magazines-to-the-urban-information-environmen",
    "am-i-the-data-geek-who-analyzed-reddit-aita-posts-yes",
    "how-to-make-word-clouds-people-wont-hate",
    "llms-alone-wont-solve-your-businesss-predictive-needs",
    "what-is-marketing-mix-modeling",
    "outbreak-analytics-data-science-strategies-for-a-novel-problem",
    "city-magazine-editors-and-the-evolving-urban-information-environment",
    "political-magazines-on-twitter-during-the-us-presidential-election-201",
    "teaching-magazine-students-more-than-magazines",
    "refining-retention-strategies-for-mobile-games-at-sciplay",
    "your-brand-their-product-a-critical-look-at-teaching-personal-branding",
}

PROFILE_TITLE_RE = re.compile(
    r"(principal components|interview|meet |q\s*&\s*a|ask me anything|"
    r"rising above|overcoming constraints|facing the learning curve)",
    re.I,
)

FEATURE_TITLE_RE = re.compile(
    r"(deep dive|whitepaper|case study|special report|"
    r"how |why |inside |behind |challenge|opportunit|evolving|"
    r"lesson|crowdfunding|netflix|digital magazine|"
    r"multi-platform|social media|kickstarter|maker space|timeline)",
    re.I,
)

DATA_SCIENCE_TITLE_RE = re.compile(
    r"\b(data science|machine learning|\bai\b|\bml\b|predictive|analytics|"
    r"alteryx|python|visualization|model(?:ing)?|mmm|marketing mix)\b",
    re.I,
)

MEDIA_TITLE_RE = re.compile(
    r"\b(magazine|journalism|media|publish(?:ing|er)|newsroom|editor)\b",
    re.I,
)

ACADEMIC_TITLE_RE = re.compile(
    r"\b(teaching|student|professor|university|academic|curriculum|"
    r"classroom|aejmc|literacy)\b",
    re.I,
)

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def host_of(url: str | None) -> str | None:
    if not url:
        return None
    try:
        host = urlparse(url).netloc.lower()
    except ValueError:
        return None
    return host[4:] if host.startswith("www.") else host


def normalize_host(host: str | None) -> str | None:
    if not host:
        return None
    return host[4:] if host.startswith("www.") else host


def publication_for(host: str | None, url: str | None) -> str | None:
    if not host:
        return None
    for key, label in HOST_PUBLICATION.items():
        key_n = normalize_host(key) or key
        if host == key_n or host.endswith("." + key_n):
            return label
    if host.endswith("medium.com"):
        return "Medium"
    return host


def categories_for(host: str | None, title: str, slug: str) -> list[str]:
    cats: list[str] = []

    def add(cat: str) -> None:
        if cat not in cats:
            cats.append(cat)

    host_n = normalize_host(host)

    if host_n in {normalize_host(h) for h in DATA_SCIENCE_HOSTS} or (
        host_n and (host_n.endswith("alteryx.com") or host_n.endswith("pecan.ai")
                    or host_n.endswith("medium.com"))
    ):
        add("data-science")

    if host_n in {normalize_host(h) for h in MEDIA_HOSTS}:
        add("media")

    if host_n in {normalize_host(h) for h in ACADEMIC_HOSTS}:
        add("academic")

    if host_n in {normalize_host(h) for h in FEATURE_HOSTS}:
        add("features")

    if PROFILE_TITLE_RE.search(title) or "principal-components" in slug:
        add("profiles")
        if "data-science" not in cats and DATA_SCIENCE_TITLE_RE.search(title):
            add("data-science")

    if FEATURE_TITLE_RE.search(title):
        add("features")

    # Reported MediaShift pieces often belong under Features as well
    if host_n in {"mediashift.org"} and FEATURE_TITLE_RE.search(title):
        add("features")
        add("media")

    # Teaching / journalism-school pieces often live on MediaShift
    if ACADEMIC_TITLE_RE.search(title) and "media" in cats:
        add("academic")

    if not cats:
        if DATA_SCIENCE_TITLE_RE.search(title):
            add("data-science")
        elif ACADEMIC_TITLE_RE.search(title):
            add("academic")
        elif MEDIA_TITLE_RE.search(title):
            add("media")
        else:
            # Undated whitepapers / marketing PDFs without URL
            if "pecan" in slug or "predictive" in slug or "marketing-mix" in slug:
                add("data-science")
            elif MEDIA_TITLE_RE.search(slug.replace("-", " ")):
                add("media")
            else:
                add("features")

    # Substantive academic/media essays also count as features
    if "academic" in cats and "features" not in cats:
        if any(
            key in slug
            for key in (
                "contribution-of-city",
                "emotion-and-news",
                "political-magazines-on-twitter",
                "urban-information",
                "personal-branding",
            )
        ):
            add("features")

    return cats


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError("missing front matter")
    raw = match.group(1)
    body = text[match.end() :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip()
    return data, body


def yaml_quote(value: str) -> str:
    if value.startswith('"') and value.endswith('"'):
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def rebuild(data: dict[str, object], body: str) -> str:
    lines = ["---"]
    # Preserve a stable key order
    order = ["title", "date", "undated", "excerpt", "original_url", "publication", "categories", "featured"]
    seen = set()
    for key in order:
        if key not in data:
            continue
        seen.add(key)
        val = data[key]
        if key == "categories":
            cats = ", ".join(val)  # type: ignore[arg-type]
            lines.append(f"categories: [{cats}]")
        elif key == "featured":
            lines.append("featured: true")
        elif key == "undated":
            lines.append("undated: true")
        elif key in ("title", "excerpt", "original_url", "publication"):
            raw = str(val)
            # keep existing quoting style if already quoted in stored form
            if isinstance(val, str) and not (val.startswith('"') and val.endswith('"')):
                lines.append(f"{key}: {yaml_quote(val)}")
            else:
                lines.append(f"{key}: {raw}")
        else:
            lines.append(f"{key}: {val}")
    for key, val in data.items():
        if key in seen:
            continue
        lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")
    if body.startswith("\n"):
        return "\n".join(lines) + body.lstrip("\n")
    return "\n".join(lines) + "\n" + body


def extract_field(raw_map: dict[str, str], key: str) -> str | None:
    val = raw_map.get(key)
    if val is None:
        return None
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    return val


def is_featured(slug: str, path: Path) -> bool:
    stem = path.stem  # YYYY-MM-DD-slug
    slug_part = stem.split("-", 3)[-1] if stem.count("-") >= 3 else stem
    for featured in FEATURED_SLUGS:
        if slug_part.startswith(featured) or featured in slug_part:
            # Prefer canonical non-duplicate file (no -2/-3 suffix) when possible
            if re.search(r"-(2|3)$", slug_part) and not featured.endswith(("-2", "-3")):
                # Allow only if the featured slug explicitly includes suffix
                if featured not in slug_part or slug_part != featured and not slug_part.startswith(featured):
                    # e.g. ...-yes-2 should not match ...-yes
                    if re.fullmatch(re.escape(featured) + r"-(2|3)", slug_part):
                        return False
            return True
    return False


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    raw_map, body = parse_front_matter(text)
    title = extract_field(raw_map, "title") or path.stem
    url = extract_field(raw_map, "original_url")
    host = host_of(url)
    stem = path.stem
    slug_part = stem.split("-", 3)[-1]

    cats = categories_for(host, title, slug_part)
    pub = publication_for(host, url)

    # Clean quoted fields back to plain strings for rebuild
    data: dict[str, object] = {}
    for key, val in raw_map.items():
        if key in ("categories", "publication", "featured"):
            continue
        if key in ("title", "excerpt", "original_url"):
            data[key] = extract_field(raw_map, key) or val
        else:
            data[key] = val

    data["categories"] = cats
    if pub:
        data["publication"] = pub
    if is_featured(slug_part, path):
        # Prefer primary files for favorites (skip -2/-3 dupes)
        if not re.search(r"-(2|3)$", slug_part):
            data["featured"] = True
        else:
            # special-case: only feature base versions
            pass

    new_text = rebuild(data, body)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    counts: dict[str, int] = {}
    featured = 0
    for path in sorted(POSTS.glob("*.md")):
        process(path)
        text = path.read_text(encoding="utf-8")
        raw_map, _ = parse_front_matter(text)
        cats_line = raw_map.get("categories", "[]")
        cats = re.findall(r"[a-z0-9-]+", cats_line)
        for c in cats:
            if c != "categories":
                counts[c] = counts.get(c, 0) + 1
        if raw_map.get("featured", "").startswith("true"):
            featured += 1
        changed += 1
    print(f"Processed {changed} posts")
    print("Category counts:", dict(sorted(counts.items())))
    print(f"Featured: {featured}")


if __name__ == "__main__":
    main()
