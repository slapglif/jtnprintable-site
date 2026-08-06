from pathlib import Path
import html
import re
import xml.etree.ElementTree as ET
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://slapglif.github.io/jtnprintable-site/"
TODAY = date.today().isoformat()

CATEGORY_MAP = {
    "Foundational collection pages": [
        "coastal-cottage-wall-art/",
        "tropical-aquarium-wall-art/",
        "printable-gallery-wall-sets/",
        "digital-download-help/",
        "how-to-print-printable-wall-art/",
    ],
    "Coastal, cottage, and lake-house decorating guides": [
        "up-north-cottage-printable-wall-art/",
        "beach-house-bathroom-wall-art/",
        "blue-hydrangea-sailboat-wall-art/",
        "nautical-studio-wall-art/",
        "river-species-cabin-wall-art/",
    ],
    "Kitchen and dining printable-art guides": [
        "retro-cherry-kitchen-wall-art/",
        "tinned-sardine-kitchen-wall-art/",
        "heirloom-tomato-kitchen-wall-art/",
        "cozy-bakery-kitchen-wall-art/",
        "moody-dining-room-wall-art/",
    ],
    "Game room, office, and study wall-art guides": [
        "mahjong-game-room-wall-art/",
        "preppy-mahjong-game-room-decor/",
        "minimalist-chess-game-room-wall-art/",
        "preppy-croquet-game-room-wall-art/",
        "brutalist-home-office-wall-art/",
        "cyberpunk-japan-gaming-room-wall-art/",
        "horse-lover-home-office-decor/",
    ],
    "Science, nature, and atmosphere wall-art guides": [
        "storm-supercell-plains-wall-art/",
        "storm-chaser-office-decor/",
        "moody-weather-room-wall-art/",
        "deep-space-nebula-wall-art/",
        "desert-observatory-wall-art/",
        "fossil-paleontology-wall-art/",
        "mineral-crystal-geology-wall-art/",
        "solarpunk-city-wall-art/",
        "volcano-glass-workshop-wall-art/",
    ],
    "Soft rooms and specialty gallery-wall guides": [
        "nordic-sauna-wall-art/",
        "dark-academia-library-wall-art/",
        "cottagecore-botanical-wall-art/",
        "equestrian-tack-room-wall-art/",
        "woodland-nursery-gallery-wall/",
        "medieval-castle-wall-art/",
    ],
}


def read(p):
    return p.read_text(encoding="utf-8")


def write(p, s):
    p.write_text(s, encoding="utf-8", newline="\n")


def meta_for(slug):
    p = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    s = read(p)
    title = re.search(r"<title>(.*?)</title>", s, re.I | re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', s, re.I | re.S)
    canonical = re.search(r'<link rel="canonical" href="(.*?)"', s, re.I | re.S)
    robots = re.search(r'<meta name="robots" content="(.*?)"', s, re.I | re.S)
    return {
        "slug": slug,
        "path": p,
        "title": html.unescape(title.group(1)).strip() if title else slug,
        "description": html.unescape(desc.group(1)).strip() if desc else "",
        "canonical": canonical.group(1) if canonical else BASE + slug,
        "robots": robots.group(1).lower() if robots else "",
    }

all_slugs = ["", *[slug for slugs in CATEGORY_MAP.values() for slug in slugs]]
# Keep only self-canonical, indexable pages in discovery feeds. Excludes redirect/noindex duplicates.
pages = []
seen = set()
for slug in all_slugs:
    m = meta_for(slug)
    expected = BASE + slug
    if "noindex" in m["robots"] or m["canonical"] != expected or expected in seen:
        continue
    pages.append(m)
    seen.add(expected)

# sitemap.xml with full current indexable page set.
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for m in pages:
    url = ET.SubElement(urlset, "url")
    ET.SubElement(url, "loc").text = m["canonical"]
    ET.SubElement(url, "lastmod").text = TODAY
    ET.SubElement(url, "changefreq").text = "weekly" if m["slug"] else "daily"
    ET.SubElement(url, "priority").text = "1.0" if m["slug"] == "" else ("0.8" if m["slug"] in {"printable-gallery-wall-sets/", "how-to-print-printable-wall-art/", "digital-download-help/"} else "0.7")
ET.indent(urlset, space="  ")
write(ROOT / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(urlset, encoding="unicode"))

# llms.txt: concise owned-site map for AI/crawler discovery without inventing claims.
lines = [
    "# JTN Printable",
    "",
    "> Original printable gallery-wall collections and room-by-room printable wall-art guides. Digital downloads only; no physical prints or frames are shipped.",
    "",
    "## Canonical site",
    f"- Primary public URL while custom-domain DNS is being repaired: {BASE}",
    "- Intended custom domain after DNS and GitHub Pages custom-domain verification: https://jtnprintable.com/",
    "",
]
lookup = {m["slug"]: m for m in pages}
for heading, slugs in CATEGORY_MAP.items():
    lines.append(f"## {heading}")
    for slug in slugs:
        m = lookup.get(slug)
        if not m:
            continue
        desc = m["description"] or m["title"]
        lines.append(f"- [{m['title'].replace(' | JTN Printable','')}]({m['canonical']}): {desc}")
    lines.append("")
lines += [
    "## Discovery endpoints",
    f"- Sitemap: {BASE}sitemap.xml",
    f"- Robots: {BASE}robots.txt",
    f"- RSS feed: {BASE}feed.xml",
    "",
    "Etsy listing CTAs on collection and guide pages use owned-organic UTM links. Etsy handles checkout and file delivery.",
]
write(ROOT / "llms.txt", "\n".join(lines) + "\n")

# Add stronger home and gallery hubs so sitemap-only pages become normal internal links.
def link_list(slugs, prefix=""):
    out = ["<ul class=\"link-list\">"]
    for slug in slugs:
        m = lookup.get(slug)
        if not m:
            continue
        out.append(f'<li><a href="{prefix}{slug}">{html.escape(m["title"].replace(" | JTN Printable", ""))}</a></li>')
    out.append("</ul>")
    return "".join(out)

home_hub = "".join([
    '<section class="prose discovery-hub"><h2>Browse printable wall-art guides by room and theme</h2>',
    '<p>Use these owner-written decorating guides to compare rooms, layouts, print ratios, frame finishes, and digital-download details before opening a specific Etsy listing.</p>',
    link_list(["printable-gallery-wall-sets/", "how-to-print-printable-wall-art/", "digital-download-help/", "coastal-cottage-wall-art/", "tropical-aquarium-wall-art/", "mahjong-game-room-wall-art/", "nordic-sauna-wall-art/", "deep-space-nebula-wall-art/", "storm-supercell-plains-wall-art/", "cottagecore-botanical-wall-art/"], ""),
    '</section>'
])
idx = read(ROOT / "index.html")
idx = re.sub(r'<section class="prose discovery-hub">.*?</section>', '', idx, flags=re.S)
idx = idx.replace('<p class="notice">Digital download only.', home_hub + '<p class="notice">Digital download only.')
write(ROOT / "index.html", idx)

gallery_sections = ['<section class="discovery-hub"><h2>More printable wall-art guides</h2><p>These guides are grouped as discovery hubs rather than one-off doorway pages; each page adds room-specific layout, framing, print, and digital-download guidance.</p>']
for heading, slugs in list(CATEGORY_MAP.items())[1:]:
    gallery_sections.append(f"<h3>{html.escape(heading)}</h3>")
    gallery_sections.append(link_list(slugs, "../"))
gallery_sections.append('</section>')
gallery_hub = ''.join(gallery_sections)
gal = read(ROOT / "printable-gallery-wall-sets" / "index.html")
gal = re.sub(r'<section class="discovery-hub">.*?</section>', '', gal, flags=re.S)
gal = gal.replace('<p class="notice">Digital download only.', gallery_hub + '<p class="notice">Digital download only.')
write(ROOT / "printable-gallery-wall-sets" / "index.html", gal)

# cache headers for llms/feed discovery endpoint freshness.
hdr = read(ROOT / "_headers")
for block in ["/llms.txt\n  Cache-Control: public, max-age=3600\n", "/feed.xml\n  Cache-Control: public, max-age=3600\n"]:
    if block.split("\n",1)[0] not in hdr:
        hdr = hdr.rstrip() + "\n\n" + block
write(ROOT / "_headers", hdr)

print(f"Updated {len(pages)} indexable URLs")
