# Owned-site discovery and indexation package

Prepared for the GitHub Pages site at `https://slapglif.github.io/jtnprintable-site/` while `jtnprintable.com` DNS/custom-domain repair proceeds.

## Current public state verified

- Public GitHub Pages URL: `https://slapglif.github.io/jtnprintable-site/`
- Repository: `https://github.com/slapglif/jtnprintable-site`
- GitHub Pages source: `main` branch, repository root `/`
- GitHub Pages status: `built`
- GitHub Pages custom domain: not attached yet (`cname: null`)
- HTTPS enforcement: enabled
- Current canonical host: `slapglif.github.io`, not `jtnprintable.com`, to avoid canonicalizing to a domain before DNS and Pages custom-domain verification are complete.

## Live discovery endpoints

- `https://slapglif.github.io/jtnprintable-site/robots.txt`
- `https://slapglif.github.io/jtnprintable-site/sitemap.xml`
- `https://slapglif.github.io/jtnprintable-site/llms.txt`
- `https://slapglif.github.io/jtnprintable-site/feed.xml`

## Repository improvements included in this package

1. Regenerated `sitemap.xml` from indexable, self-canonical HTML pages only.
   - Includes 38 indexable URLs.
   - Excludes the `storm-supercell-wall-art/` duplicate/noindex redirect page because it canonicalizes to `storm-supercell-plains-wall-art/`.
   - Adds `lastmod`, `changefreq`, and `priority` fields.
2. Expanded `llms.txt` into a complete, grouped owned-site map for AI/search discovery.
3. Added normal internal hub links on:
   - `/` home page
   - `/printable-gallery-wall-sets/`
4. Added cache headers for `llms.txt` and `feed.xml` in `_headers`.
5. Added `scripts/update_discovery.py` so sitemap, llms.txt, and internal hub snippets can be regenerated without hand-editing.

## Search-console and indexation readiness

### Google Search Console

Ready to submit **after** the DNS/custom-domain repair is complete if the property being verified is `jtnprintable.com`.

Recommended order:

1. Finish DNS for `jtnprintable.com` and `www.jtnprintable.com`.
2. Attach the custom domain in GitHub Pages and confirm `cname` is no longer null.
3. Switch canonicals, sitemap URLs, robots sitemap URL, RSS/llms URLs, and schema URLs from the GitHub Pages host to `https://jtnprintable.com/` in one commit.
4. Verify `https://jtnprintable.com/robots.txt` and `https://jtnprintable.com/sitemap.xml` return 200.
5. Submit the sitemap in Google Search Console.

Do not submit the custom-domain sitemap before the custom domain returns stable 200/HTTPS responses.

### Bing Webmaster Tools / IndexNow

Ready after the same custom-domain transition above. IndexNow requires a key file or key location on the verified host; no key is committed here because no Bing/IndexNow key was provided and the custom domain is not attached yet.

When ready:

1. Create an IndexNow key in Bing Webmaster Tools.
2. Add the key file at the site root, for example `/INDEXNOW_KEY.txt`.
3. Submit only canonical `https://jtnprintable.com/...` URLs after the domain is live.

## Compliant owned-profile discovery opportunities

Use profiles controlled by JTNPrintableCo only. Avoid fake engagement, paid traffic inflation, doorway pages, and any claim that site visits are Etsy visitors.

Safe opportunities:

- Pinterest owned profile `https://www.pinterest.com/JTNPrintableCo/`: add the owned site URL to profile/about fields where supported; create boards that point to hub pages like `/printable-gallery-wall-sets/`, `/how-to-print-printable-wall-art/`, and room-theme guides.
- Etsy shop About/related links: add `https://jtnprintable.com/` only after DNS/HTTPS is live; until then, use the GitHub Pages URL only if the owner accepts the temporary host branding.
- GitHub repository homepage/README: keep the public Pages URL listed until custom domain is live, then update to `https://jtnprintable.com/`.
- Owned RSS/llms discovery: keep `feed.xml` and `llms.txt` current whenever guide pages are added.

## Guardrails

- Do not count GitHub Pages, Pinterest, or other owned-site sessions as Etsy visitors. Etsy visitor counts must come from first-party Etsy Stats.
- Do not create thin one-listing pages. New pages should add useful room/layout/printing guidance and be linked from hubs.
- Do not canonicalize to `jtnprintable.com` until DNS, HTTPS, and GitHub Pages custom-domain state are verified.
