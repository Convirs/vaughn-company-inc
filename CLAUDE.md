# Vaughn Company, Inc. (vaughncompanyinc.com)

This is a 1:1 static rebuild of the Weblium site. It is plain HTML, CSS and vanilla JS, deployed on Vercel with no build step.

## Standing rules (Andy)
- FAQs and accordions open one at a time. Use `details.acc` with a shared `name`; the JS fallback lives in main.js.
- Mobile menu: the page and the panel must not scroll while it is open, and the hamburger turns into an X. The panel is pinned to the header's live bottom edge through `--menu-top`.
- When images need downloading, paste a PowerShell one-liner in chat. The sandbox has no network access to the CDN.
- The favicon is the original site's own favicon (`images/favicon.png` and `apple-touch-icon.png`). Never generate one from the logo.
- No U+2014 anywhere. Internal links are root relative and extensionless. `vercel.json` sets `cleanUrls: true`.

## Editing
- All pages are generated: edit `_build/build.py` (head, header, footer, meta) or `_build/pages.py` (page bodies), then run `python _build/build.py` from the repo root. Do not hand edit the generated HTML.
- `_build/`, `_migration/` and the docs are excluded from deploys by `.vercelignore`.

## Brand tokens (measured)
- red `#f50f24`, red-dark `#ca0c1e`, ink `#1b1929`, sand `#eae6e2`, tile grey `#eeeeee`, tile dark `#434343`
- Fonts: Roboto 700/900 for display type, Hind 400/500/700 for body text. Container width is 1170px.
- Type uses fixed px sizes, as on the original: hero h1 56/900, section h2 48/900, sub h2 36/700, card title 24/700, lead 28/500, body 17, eyebrow 13/700 with 2.6px letter-spacing. Mobile overrides start at 767px.

## Bands
- Home: photo hero with a transparent header that turns solid after 40px of scroll, then the red problems band, the YouTube background video band (ZTzYgyLRYi8, overlay .56 plus a popup), 4 association tiles (SVG backgrounds under alpha overlays), the testimonial **carousel** (2 slides, height follows the active slide), project complexity (fixed photo, overlay .87), 3 steps, and the ready split (`#contact`).
- About: red hero, a click-to-load YouTube video (dnon5u-oxNI), a 3-column projects grid, and the topo CTA band (overlay .3).
- Hiring: YouTube background hero (dnon5u-oxNI), benefits list, and the topo apply band (overlay .94). Both buttons go to Adobe Sign widgets.
- Privacy: Termageddon embed `div#policy` with key `WXpGVVdFSTVZa2d5UzFOQlRXYzlQUT09` (the id must be `policy`).

## CDN
- Site images: `https://res2.yourwebsite.life/res/6509d611a28ceb00174ddcf8/<exact filename>`
- Template images (60e... ids): `https://res2.yourwebsite.life/res/60e561b865ebc10021338c63/<id>?nowebp`. These are SVGs, so check the type with `file` before naming.
- Always use the exact captured filename. A bare id often 404s.

### Path Prefixes
Internal links: `/`, `/about-us`, `/hiring-now`, `/contact-us`, `/privacy-policy`, `/#contact`.

### Punctuation
No U+2014. En dashes stay in ranges and in "APAC &ndash; Central". The spaced hyphen in "first time - hassle-free" is original copy.
