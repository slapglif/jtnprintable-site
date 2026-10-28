# JTN Printable Pinterest profile — owned-site link brief

**Status:** prepared locally; not applied to Pinterest.

## Verified distribution issue

On 2026-08-27, the public `JTNPrintableCo` Pinterest profile was reachable while signed out and showed its sole profile website link as `http://etsy.com/shop/JTNPrintableCo`. This bypasses the owned JTN Printable guides and prevents first-party attribution of profile traffic. It should not be described as Etsy traffic or Etsy conversion data.

## Approved replacement profile website URL

Use this exact HTTPS URL in the Pinterest profile website field:

`https://slapglif.github.io/jtnprintable-site/?utm_source=pinterest&utm_medium=organic&utm_campaign=profile_evergreen_2026q3&utm_content=profile_website`

Purpose: profile visitors arrive at the owned JTN Printable collection and guide hub, then can choose an existing Etsy CTA from the relevant guide. The URL uses the same `utm_source=pinterest` / `utm_medium=organic` convention as the prepared Pin queue.

## Optional profile bio replacement

> Printable wall art and digital decor for thoughtfully styled homes. Explore room-by-room gallery-wall ideas, then find the matching digital-download collection.

Do not add price, availability, review, delivery-time, or sales claims unless confirmed in the relevant Etsy listing.

## Safe application and verification steps

1. Sign in only to the verified owner account, `JTNPrintableCo`.
2. Replace the profile website field with the exact tracked owned-site URL above. Do not change boards, Pins, or account settings in the same session.
3. If using the optional bio, replace only the profile bio with the text above.
4. Save, then load the public profile while signed out and confirm it shows the owned-site link rather than Etsy.
5. Request the tracked URL and require HTTP 200. Record the date of the change and Pinterest outbound-click data separately from Etsy stats.

## Evidence from this audit

- Public profile: https://www.pinterest.com/JTNPrintableCo/
- Public owned-site homepage: https://slapglif.github.io/jtnprintable-site/
- The public owned-site homepage and public Pinterest profile both returned HTTP 200 during this audit.
- Pinterest publishing/account authority is not authenticated or verified in this environment; no change was made.
