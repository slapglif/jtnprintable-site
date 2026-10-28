# Discovery generator drift audit — 2026-08-27

## Finding

`scripts/update_discovery.py` currently derives discovery output from a manually maintained `CATEGORY_MAP`. That map is behind the checked-in sitemap.

A dry run in a temporary copy of the repository produced **43** indexable URLs, while the checked-in/live sitemap contains **72** URLs. Applying the generator as written would remove **29** existing sitemap and `llms.txt` entries. This is a material organic-discovery risk, so the generator must not be run against the production branch until its source list is reconciled.

## Verification performed

- Public sitemap: `https://slapglif.github.io/jtnprintable-site/sitemap.xml` returned HTTP 200 and contains 72 URLs.
- Current generator dry run: 43 URLs; 29 removals; no additions.
- Each of the 29 removed-by-generator public routes was requested directly: **29/29 returned HTTP 200** on 2026-08-27.
- The dry run occurred in a temporary copy; the working tree was restored without applying the generated removals.

## Routes at risk of accidental removal

- `abstract-ocean-coastal-wall-art/`
- `art-deco-cocktail-bar-wall-art/`
- `boho-desert-bedroom-wall-art/`
- `coastal-grandmother-bedroom-wall-art/`
- `deep-sea-creatures-gallery-wall/`
- `english-country-manor-gallery-wall/`
- `folk-art-bird-prints-gallery-wall/`
- `french-countryside-gallery-wall/`
- `gardening-potting-shed-wall-art/`
- `heritage-tennis-club-wall-art/`
- `high-desert-wind-turbine-wall-art/`
- `maximalist-gallery-wall-art/`
- `microscopic-botanical-cells-wall-art/`
- `moody-billiards-game-room-wall-art/`
- `neutral-mediterranean-wall-art/`
- `nursery-and-personalized-printable-art/`
- `pickleball-game-room-wall-art/`
- `printable-art-formats-and-gallery-sets/`
- `printable-art-moods-and-trends/`
- `printable-wall-art-by-room/`
- `printable-wall-art-colors/`
- `printable-wall-art-for-occasions/`
- `printable-wall-art-gifts/`
- `printable-wall-art-styles/`
- `printable-wall-art-subjects/`
- `rowing-lake-house-wall-art/`
- `sewing-room-wall-art-guide/`
- `stratospheric-balloon-office-wall-art/`
- `vintage-mushroom-botanical-wall-art/`

## Safe remediation

1. Treat the checked-in sitemap plus self-canonical, indexable local HTML pages as the reconciliation source; do not assume a manually curated subset is exhaustive.
2. Update `CATEGORY_MAP` or replace it with a validated manifest that includes every approved guide and hub.
3. Add a guard test that fails whenever a generator run removes an existing self-canonical URL unless that removal is explicitly allowlisted with a reason.
4. Only then regenerate `sitemap.xml`, `llms.txt`, and discovery hubs, review the complete diff, and publish.

This is an owned-site SEO/distribution finding only. It does not assert Etsy traffic, marketplace ranking, sales, or external-platform performance.
