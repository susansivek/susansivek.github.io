# Susan Currie Sivek — Portfolio Site

This is a Jekyll site built from your Authory XML export (324 articles),
ready to host free on GitHub Pages.

## What's in here

- `_posts/` — one Markdown file per article, with title, date, original
  publication link, and full body content converted from your Authory export.
- `_config.yml` — site settings, using the free "Minimal" theme that GitHub
  Pages supports natively (no local build tools needed).
- `index.md` — homepage listing all posts, paginated.
- 5 articles had no usable date in the export and were filed under
  `1900-01-01` — search `_posts/1900-01-01-*` and fix the date in the
  filename + front matter once you know when they ran (or leave as-is;
  they'll just sort to the bottom of the list).

## Deploy it (10 minutes, free)

1. Create a new GitHub repository (e.g. `susanwrites.github.io` if you want
   it at the root of a github.io domain, or any name like `portfolio`).
2. Push everything in this `site/` folder to the repo root:
   ```
   git init
   git add .
   git commit -m "Initial portfolio site"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
   git push -u origin main
   ```
3. In the repo, go to **Settings → Pages**, set Source to "Deploy from a
   branch", branch `main`, folder `/ (root)`. Save.
4. Wait ~1 minute, then visit `https://YOUR-USERNAME.github.io/YOUR-REPO/`
   (or just `https://YOUR-USERNAME.github.io/` if you used the special
   `username.github.io` repo name).
5. (Optional) Add a custom domain under Settings → Pages → Custom domain.

## Customizing

- Edit `_config.yml` to change the title/description, or swap
  `remote_theme:` for another GitHub Pages–supported theme
  (https://pages.github.com/themes/).
- Edit `index.md` to change the homepage layout/intro text.
- Each post's front matter (top of the `.md` file, between `---` lines) can
  be edited freely — title, date, excerpt, original_url.

## Canceling Authory

Once you've confirmed the site looks right (push it, check it live), you're
safe to cancel your Authory subscription — all the article text and metadata
is now in this repo, not dependent on Authory.
