#!/usr/bin/env python3
"""Recover broken PDF links into assets/pdfs/ and emit a rewrite map."""
from __future__ import annotations

import json
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "pdfs"
OUT.mkdir(parents=True, exist_ok=True)

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()
TIMEOUT = 60

# Each entry: preferred local filename, original URL(s) that appear in posts,
# candidate download URLs (direct / alternates / known Wayback).
TARGETS: list[dict] = [
    {
        "local": "sivek-aejmc-fall2013.pdf",
        "rewrites": [
            "http://aejmcmagazine.arizona.edu/Journal/Fall2013/Sivek.pdf",
            "https://aejmcmagazine.arizona.edu/Journal/Fall2013/Sivek.pdf",
        ],
        "candidates": [
            "https://web.archive.org/web/20131008223414if_/http://aejmcmagazine.arizona.edu:80/Journal/Fall2013/Sivek.pdf",
            "http://aejmcmagazine.arizona.edu/Journal/Fall2013/Sivek.pdf",
        ],
    },
    {
        "local": "sivek-aejmc-fall2015.pdf",
        "rewrites": [
            "https://aejmcmagazine.arizona.edu/Journal/Fall2015/Sivek.pdf",
        ],
        "candidates": [
            # SSRN deposit of the same JMNMR Fall 2015 article
            "https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3028976_code2775870.pdf?abstractid=3028976&mirid=1",
            "https://papers.ssrn.com/sol3/Delivery.cfm/3028976.pdf?abstractid=3028976&mirid=1&type=2",
            "http://aejmcmagazine.arizona.edu/Journal/Fall2015/Sivek.pdf",
            "https://aejmcmagazine.arizona.edu/Journal/Fall2015/Sivek.pdf",
        ],
        "wayback_of": [
            "http://aejmcmagazine.arizona.edu/Journal/Fall2015/Sivek.pdf",
            "https://aejmcmagazine.arizona.edu/Journal/Fall2015/Sivek.pdf",
        ],
    },
    {
        "local": "sivek-townsend-aejmc-spring2014.pdf",
        "rewrites": [
            "https://aejmcmagazine.arizona.edu/Journal/Spring2014/SivekTownsend.pdf",
        ],
        "candidates": [
            "https://web.archive.org/web/20170811121152if_/https://aejmcmagazine.arizona.edu/Journal/Spring2014/SivekTownsend.pdf",
            "https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3028978_code2775870.pdf?abstractid=3028978&mirid=1",
            "https://papers.ssrn.com/sol3/Delivery.cfm/3028978.pdf?abstractid=3028978&mirid=1&type=2",
        ],
    },
    {
        "local": "sivek-community-journalism-2014.pdf",
        "rewrites": [
            "http://journal.community-journalism.net/sites/default/files/sivek-cj2014.pdf",
        ],
        "candidates": [
            "https://digitalcommons.linfield.edu/cgi/viewcontent.cgi?article=1015&context=mscmfac_pubs",
            "https://digitalcommons.linfield.edu/cgi/viewcontent.cgi?article=1014&context=mscmfac_pubs",
            "https://digitalcommons.linfield.edu/cgi/viewcontent.cgi?article=1013&context=mscmfac_pubs",
        ],
        "wayback_of": [
            "http://journal.community-journalism.net/sites/default/files/sivek-cj2014.pdf",
        ],
    },
    {
        "local": "outbreak-science-2020.pdf",
        "rewrites": [
            "http://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2020/200324-outbreak-science.pdf",
        ],
        "candidates": [
            "https://centerforhealthsecurity.org/sites/default/files/2022-12/200324-outbreak-science.pdf",
            "https://www.centerforhealthsecurity.org/sites/default/files/2022-12/200324-outbreak-science.pdf",
        ],
        "wayback_of": [
            "http://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2020/200324-outbreak-science.pdf",
        ],
    },
    {
        "local": "mpa-handbook-2009.pdf",
        "rewrites": [
            "http://www.magazine.org/ASSETS/088C8564EB9E4E978A69B183881AEF58/MPA-Handbook-2009.pdf",
        ],
        "candidates": [],
        "wayback_of": [
            "http://www.magazine.org/ASSETS/088C8564EB9E4E978A69B183881AEF58/MPA-Handbook-2009.pdf",
        ],
    },
    {
        "local": "mm360-bar-feb2015.pdf",
        "rewrites": [
            "http://www.magazine.org/sites/default/files/MM360BARFeb2015.pdf",
        ],
        "candidates": [],
        "wayback_of": [
            "http://www.magazine.org/sites/default/files/MM360BARFeb2015.pdf",
        ],
    },
    {
        "local": "state-of-journalism-education-2013.pdf",
        "rewrites": [
            "http://www.newsu.org/course_files/StateOfJournalismEducation2013.pdf",
        ],
        "candidates": [],
        "wayback_of": [
            "http://www.newsu.org/course_files/StateOfJournalismEducation2013.pdf",
        ],
    },
    {
        "local": "jour504-syllabus.pdf",
        "rewrites": [
            "http://www.sustainability.umd.edu/content/curriculum/Chesapeake_Project_Revised_Courses/2013/JOUR504_syllabus.pdf",
        ],
        "candidates": [],
        "wayback_of": [
            "http://www.sustainability.umd.edu/content/curriculum/Chesapeake_Project_Revised_Courses/2013/JOUR504_syllabus.pdf",
        ],
    },
    {
        "local": "alteryx-for-good-educator.pdf",
        "rewrites": [
            "https://community.alteryx.com/pvsmt99345/attachments/pvsmt99345/AFGResources/6/1/Alteryx%20for%20Good.Educator.pdf",
        ],
        "candidates": [
            "https://community.alteryx.com/pvsmt99345/attachments/pvsmt99345/AFGResources/6/1/Alteryx%20for%20Good.Educator.pdf",
        ],
        "wayback_of": [
            "https://community.alteryx.com/pvsmt99345/attachments/pvsmt99345/AFGResources/6/1/Alteryx for Good.Educator.pdf",
        ],
    },
    {
        "local": "what-and-why-of-predictive-analytics.pdf",
        "rewrites": [
            "https://fs.hubspotusercontent00.net/hubfs/7594808/Content/Whitepapers/The-What-and-Why-of-Predictive-Analytics.pdf",
        ],
        "candidates": [
            "https://fs.hubspotusercontent00.net/hubfs/7594808/Content/Whitepapers/The-What-and-Why-of-Predictive-Analytics.pdf",
            "https://www.pecan.ai/wp-content/uploads/2022/03/The-What-and-Why-of-Predictive-Analytics.pdf",
            "https://www.pecan.ai/wp-content/uploads/2021/12/The-What-and-Why-of-Predictive-Analytics.pdf",
        ],
        "wayback_of": [
            "https://fs.hubspotusercontent00.net/hubfs/7594808/Content/Whitepapers/The-What-and-Why-of-Predictive-Analytics.pdf",
        ],
    },
    {
        "local": "whr20.pdf",
        "rewrites": [
            "https://happiness-report.s3.amazonaws.com/2020/WHR20.pdf",
        ],
        "candidates": [
            "https://happiness-report.s3.amazonaws.com/2020/WHR20.pdf",
            "https://s3.amazonaws.com/happiness-report/2020/WHR20.pdf",
            "https://worldhappiness.report/ed/2020/",
        ],
        "wayback_of": [
            "https://happiness-report.s3.amazonaws.com/2020/WHR20.pdf",
        ],
    },
    {
        "local": "eli7085.pdf",
        "rewrites": [
            "https://net.educause.edu/ir/library/pdf/ELI7085.pdf",
        ],
        "candidates": [
            "https://library.educause.edu/-/media/files/library/2018/4/eli7085.pdf",
            "https://library.educause.edu/~/media/files/library/2018/4/eli7085.pdf",
        ],
        "wayback_of": [
            "https://net.educause.edu/ir/library/pdf/ELI7085.pdf",
        ],
    },
    {
        "local": "salesforce-ai-model-cards.pdf",
        "rewrites": [
            "https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_ai_model_cards.pdf",
        ],
        "candidates": [
            "https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_ai_model_cards.pdf",
        ],
        "wayback_of": [
            "https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_ai_model_cards.pdf",
        ],
    },
    {
        "local": "ascarza-jmr-2018.pdf",
        "rewrites": [
            "https://www.hbs.edu/faculty/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf",
        ],
        "candidates": [
            "https://www.hbs.edu/faculty/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf",
            "https://www.hbs.edu/ris/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf",
        ],
        "wayback_of": [
            "https://www.hbs.edu/faculty/Publication Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf",
        ],
    },
    {
        "local": "medrxiv-2020-02-29.pdf",
        "rewrites": [
            "https://www.medrxiv.org/content/10.1101/2020.02.29.20029421v1.full.pdf",
        ],
        "candidates": [
            "https://www.medrxiv.org/content/10.1101/2020.02.29.20029421v1.full.pdf",
            "https://www.medrxiv.org/content/medrxiv/early/2020/03/05/2020.02.29.20029421.full.pdf",
        ],
        "wayback_of": [
            "https://www.medrxiv.org/content/10.1101/2020.02.29.20029421v1.full.pdf",
        ],
    },
    {
        "local": "pnas-112-45-13892.pdf",
        "rewrites": [
            "https://www.pnas.org/content/pnas/112/45/13892.full.pdf",
        ],
        "candidates": [
            "https://www.pnas.org/doi/pdf/10.1073/pnas.1517743112",
            "https://www.pnas.org/doi/pdf/10.1073/pnas.1517743112?download=true",
            "https://www.pnas.org/content/pnas/112/45/13892.full.pdf",
        ],
        "wayback_of": [
            "https://www.pnas.org/content/pnas/112/45/13892.full.pdf",
        ],
    },
    {
        "local": "krause-interacting-with-predictions.pdf",
        "rewrites": [
            "https://www.researchgate.net/profile/Josua_Krause/publication/301931162_Interacting_with_Predictions_Visual_Inspection_of_Black-box_Machine_Learning_Models/links/5a299994a6fdccfbbf8178ae/Interacting-with-Predictions-Visual-Inspection-of-Black-box-Machine-Learning-Models.pdf",
        ],
        "candidates": [
            "https://graphics.cs.wisc.edu/Papers/2016/KSNLWP16/interacting_with_predictions.pdf",
            "https://www.cs.ubc.ca/~tmm/courses/cpsc533c-18-spr/materials/krause.pdf",
        ],
        "wayback_of": [
            "https://www.researchgate.net/profile/Josua_Krause/publication/301931162_Interacting_with_Predictions_Visual_Inspection_of_Black-box_Machine_Learning_Models/links/5a299994a6fdccfbbf8178ae/Interacting-with-Predictions-Visual-Inspection-of-Black-box-Machine-Learning-Models.pdf",
        ],
    },
]


def encode_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/%")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, ""))


def http_get(url: str, timeout: int = TIMEOUT) -> tuple[bytes | None, str]:
    clean = encode_url(url)
    try:
        req = urllib.request.Request(
            clean,
            headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*;q=0.8"},
        )
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            data = resp.read()
            return data, resp.geturl()
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def is_pdf(data: bytes) -> bool:
    return data.startswith(b"%PDF")


def wayback_snapshots(url: str) -> list[str]:
    out: list[str] = []
    q = urllib.parse.quote(url, safe="")
    # CDX
    cdx = (
        f"https://web.archive.org/cdx/search/cdx?url={q}"
        "&output=json&filter=statuscode:200&fl=timestamp,original&limit=15&collapse=digest"
    )
    data, meta = http_get(cdx, timeout=40)
    if data:
        try:
            rows = json.loads(data.decode())
            for row in rows[1:]:
                ts, original = row[0], row[1]
                out.append(f"https://web.archive.org/web/{ts}if_/{original}")
        except Exception as e:  # noqa: BLE001
            print(f"    cdx parse fail: {e}", flush=True)
    else:
        print(f"    cdx fail: {meta}", flush=True)

    # available API fallback
    avail = f"https://archive.org/wayback/available?url={q}"
    data, meta = http_get(avail, timeout=30)
    if data:
        try:
            payload = json.loads(data.decode())
            closest = payload.get("archived_snapshots", {}).get("closest", {})
            if closest.get("available") and closest.get("url"):
                u = closest["url"]
                # insert identity flag
                u = re.sub(r"/web/(\d+)/", r"/web/\1if_/", u, count=1)
                if u not in out:
                    out.append(u)
        except Exception as e:  # noqa: BLE001
            print(f"    available parse fail: {e}", flush=True)
    else:
        print(f"    available fail: {meta}", flush=True)
    return out


def recover_one(target: dict) -> dict:
    local_name = target["local"]
    path = OUT / local_name
    result = {
        "local": local_name,
        "path": f"/assets/pdfs/{local_name}",
        "rewrites": target["rewrites"],
        "ok": False,
        "source": None,
        "bytes": 0,
    }

    if path.exists() and path.stat().st_size > 1000 and is_pdf(path.read_bytes()[:8]):
        print(f"EXISTS {local_name} ({path.stat().st_size} bytes)", flush=True)
        result["ok"] = True
        result["source"] = "already-present"
        result["bytes"] = path.stat().st_size
        return result

    candidates: list[str] = list(target.get("candidates") or [])
    for wurl in target.get("wayback_of") or []:
        print(f"  looking up wayback for {wurl}", flush=True)
        candidates.extend(wayback_snapshots(wurl))
        time.sleep(0.5)

    # unique preserve order
    seen: set[str] = set()
    uniq: list[str] = []
    for c in candidates:
        if c and c not in seen:
            seen.add(c)
            uniq.append(c)

    for cand in uniq:
        print(f"  try {cand[:140]}", flush=True)
        data, meta = http_get(cand)
        if not data:
            print(f"    fail: {meta}", flush=True)
            continue
        if not is_pdf(data):
            print(f"    not pdf ({len(data)} bytes) {meta}", flush=True)
            continue
        path.write_bytes(data)
        print(f"  SAVED {local_name} ({len(data)} bytes)", flush=True)
        result["ok"] = True
        result["source"] = cand
        result["bytes"] = len(data)
        return result

    print(f"  UNRECOVERED {local_name}", flush=True)
    return result


def main() -> None:
    results = []
    for t in TARGETS:
        print(f"\n=== {t['local']}", flush=True)
        results.append(recover_one(t))

    rewrite_map = {}
    for r in results:
        if not r["ok"]:
            continue
        for old in r["rewrites"]:
            rewrite_map[old] = r["path"]

    report = {
        "recovered": [r for r in results if r["ok"]],
        "failed": [r for r in results if not r["ok"]],
        "rewrite_map": rewrite_map,
    }
    (OUT / "_recovery.json").write_text(json.dumps(report, indent=2) + "\n")
    (ROOT / "broken-pdfs-recovery.json").write_text(json.dumps(report, indent=2) + "\n")
    print("\n==== SUMMARY ====", flush=True)
    print(f"recovered: {len(report['recovered'])}/{len(results)}", flush=True)
    for r in report["failed"]:
        print(f"  FAIL {r['local']}: {r['rewrites'][0]}", flush=True)


if __name__ == "__main__":
    main()
