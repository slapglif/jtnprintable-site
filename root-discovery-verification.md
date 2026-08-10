# Root task t_5825e2d3: Owned-site organic discovery and indexation campaign

## Completion summary

All four child tasks completed successfully. This root task performed a critical canonical-URL fix and final verification read-back.

## Critical fix applied this run

**Problem:** Child task t_15193046 (commits `69ba55a` + `df8fc06`) rebased all canonical/sitemap/robots/schema/og/llms/feed URLs to `jtnprintable.com`, but `jtnprintable.com` apex DNS has no A/AAAA/CNAME records on the Cloudflare nameservers (`dig +short` returns empty; `curl` returns 000 "Could not resolve host"). Per the `owned-site-discovery-indexation` skill reference: *"Do not canonicalize to jtnprintable.com while it is unresolved or unattached."* Canonical tags pointing to a dead domain would prevent Google indexing and waste the IndexNow submission.

**Fix:** Commit `d220382` reverted 79 files (905 URL replacements) back to the working `https://slapglif.github.io/jtnprintable-site/` host while preserving all structural improvements from df8fc06 (schema additions, llms.txt expansion, sitemap noindex removal, new buyer guides, and ontology hub pages).

## Child task results

### 1. Sitemap/robots/canonicals/schema/llms.txt (t_15193046, completed)
- 70 indexable pages, 0 failures across all checks
- Removed noindex page from sitemap, added Organization+WebSite+BreadcrumbList JSON-LD to 13 pages
- Updated llms.txt with 26 missing page entries
- Commit: `df8fc06`

### 2. IndexNow submission (t_d6b5af7c, completed)
- IndexNow key published at `https://slapglif.github.io/jtnprintable-site/c7d68d8ddbf114ba1682f6b178866211.txt` (HTTP 200)
- 58 URLs submitted via global IndexNow endpoint; API returned HTTP 202 (accepted/pending key verification)
- All 58 URLs independently returned HTTP 200
- GSC: correctly skipped (no existing authenticated property/session/API credential)
- Commit: `baca168` (key file)

### 3. Ontology hub pages (t_bbb2f08c, completed)
- 9 hub pages, all HTTP 200 with 365-466 words each, 8-14 internal links
- 164/164 ontology terms mapped, 0 unmapped
- All pages have canonical tags, meta descriptions, and valid CollectionPage JSON-LD schema
- Commits: `0a4f5bc`, `78f6c19`, `22f3d8f`

### 4. Compliant discovery links (t_48f8e924, completed)
- 8 UTM-tagged discovery links on the slapglif/jtnprintable-site GitHub repository
- 1 in repository homepage field + 7 in README.md (contextually relevant)
- All destinations return HTTP 200 (re-verified 2026-08-10)
- No paid/exchanged/spam links; all destinations are owned GitHub Pages hub routes
- Compliant exclusions documented: GitHub profile bio (token lacks user scope), Pinterest (no authenticated access)
- Commit: `9f131f6` + verification commit `94ea6b9`

## Final live verification (2026-08-10, commit d220382)

### Pages deployment
- Status: `built`
- cname: `null` (custom domain correctly NOT attached)
- html_url: `https://slapglif.github.io/jtnprintable-site/`

### HTTP status checks (all 200)
| Endpoint | HTTP |
|----------|------|
| Homepage | 200 |
| sitemap.xml | 200 |
| robots.txt | 200 |
| llms.txt | 200 |
| feed.xml | 200 |
| IndexNow key | 200 |

### Canonical URL verification
- Homepage: `https://slapglif.github.io/jtnprintable-site/` ✓
- 5 spot-checked pages (coastal-cottage, printable-wall-art-by-room, nursery, gallery-wall-sets, how-to-print): all correct slapglif canonicals ✓
- Sitemap: 70 URLs, all `slapglif.github.io`, 0 `jtnprintable.com` ✓
- robots.txt: `Sitemap: https://slapglif.github.io/jtnprintable-site/sitemap.xml` ✓
- llms.txt canonical: `https://slapglif.github.io/jtnprintable-site/` ✓
- feed.xml: all item links use slapglif host ✓

### Discovery links
- All 7 link destinations HTTP 200 ✓

### JSON-LD schema
- Hub pages: CollectionPage + WebSite + ItemList with ListItems ✓
- Homepage: CollectionPage + ItemList + sameAs Pinterest ✓

### UTM normalization (from prior verification)
- 37 Etsy CTAs: `utm_source=jtnprintable_site`, `utm_medium=organic`, `utm_campaign=100k_etsy_visitors`, `utm_content=<non-empty>` ✓

## Remaining dependency: DNS repair (human action required)

`jtnprintable.com` apex still has NO A/AAAA/CNAME on Cloudflare NS. Once the owner adds the four GitHub Pages apex A records (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`) and confirms DNS resolution, a single commit can switch all canonicals/sitemap/robots/schema/llms/feed URLs from `slapglif.github.io/jtnprintable-site/` to `https://jtnprintable.com/` and reattach the Pages custom domain.

## Measurement guardrails
- No owned-site visits, GitHub Pages traffic, Pinterest visits, or crawler fetches counted as Etsy visitors
- Etsy visitor/session/order attribution must come from first-party Etsy Stats only
