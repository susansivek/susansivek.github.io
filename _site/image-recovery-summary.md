# Image recovery report

## Results (2026-08-08)

| Metric | Count |
|---|---|
| Image references in posts | 976 |
| Already working remotes | ~560 |
| Self-hosted after recovery | ~164 |
| Alteryx/Lithium URLs still remote (likely dead) | ~242 |
| Files under `assets/images/posts/` | 201 (~116 MB) |

## What we did

1. **Audit** all remote image URLs.
2. **Pass 1** — recover from live `original_url` pages + Wayback of assets; mirror fragile Alteryx hosts when downloadable.
3. **Pass 2** — Wayback snapshots of original articles + republish twins (e.g. TDS/Medium copies of Alteryx posts).

Scripts: `scripts/recover_images.py`, `scripts/recover_images_pass2.py`  
JSON details: `image-recovery-report.json`, `image-recovery-pass2.json`

## What’s still missing

Most remaining broken images are **Alteryx Community / Lithium CDN** assets. Live pages often require login or no longer expose `image-id` URLs, and Wayback frequently has no snapshot of those binaries. Journal cover images (Taylor & Francis, SAGE) are also gated.

For those, options are: leave broken, remove the image markdown, or replace manually if you have exports.
