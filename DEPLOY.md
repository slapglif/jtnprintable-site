# Cloudflare Pages deployment

This static artifact is configured by the repository-root `wrangler.toml`.

## Guarded deployment
1. Use an already authenticated managed Cloudflare deployment identity.
2. Deploy `owned_site/` to the Pages project named `jtnprintable`.
3. Read back the generated Pages URL and verify all four routes, robots.txt, sitemap.xml, images, and exact Etsy CTA URLs.
4. Only then attach `jtnprintable.com` and `www` in the existing Cloudflare zone, preserving mail and unrelated DNS records.
5. Verify canonical URLs, DNS, HTTPS, and search crawlers before submitting to Search Console/Bing.

No token, account ID, registrar transfer, paid plan, or DNS mutation belongs in this repository.
