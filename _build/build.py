"""Generate the static pages for vaughncompanyinc.com.

Run from the repo root:  python _build/build.py
Edit the shared header, footer and head here, never in the generated HTML.
House rules: no U+2014 anywhere, internal links root relative and extensionless.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://vaughncompanyinc.com"
BIZ = "Vaughn Company, Inc."

PHONES = {
    "excavation": ("417-235-9912", "+14172359912"),
    "office": ("417-235-7700", "+14172357700"),
    "hauling": ("417-236-2269", "+14172362269"),
}
ADDRESS = "22453 Highway H, Monett, MO, United States"
FACEBOOK = "https://www.facebook.com/profile.php?id=100057502027866"
YOUTUBE = "https://www.youtube.com/@michaelflummerfelt1905"
DRIVER_APP = "https://na4.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhBF9DDHB40i65S-xhPWtMpyzseo7PheNaqhZ5t-eFNDwCwLtwg4h8cylavmtFu35e0*"
EMPLOY_APP = "https://na4.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhBinTM9z8K-ahjLWJJyG3KVkPbpjtJsu4HPrEpHSUm0cVfoCYICBYcWqt77Xg8szGw*"

NAV = [("/", "Home"), ("/about-us", "About Us"), ("/hiring-now", "Hiring Now"), ("/contact-us", "Contact Us")]


def tel(key):
    return PHONES[key][1]


# ---------- icons (original line drawings) ----------
ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11.5 11.5 0 0 0 7.2 7.2l1.4-2.1 4.2 1.6V19a1.7 1.7 0 0 1-1.8 1.7A16.6 16.6 0 0 1 3.3 5.3 1.7 1.7 0 0 1 5 3.5z"/></svg>',
    "calc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2.5" width="14" height="19" rx="2"/><rect x="8" y="5.5" width="8" height="3.5"/><path d="M8.5 12.5h.01M12 12.5h.01M15.5 12.5h.01M8.5 15.5h.01M12 15.5h.01M8.5 18.5h.01M12 18.5h.01M15.5 15.5v3"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="14" height="13" rx="1.5"/><path d="M2.5 8h14M6 2.5v3M13 2.5v3M5.5 11h.01M8.5 11h.01M11.5 11h.01M5.5 14h.01M8.5 14h.01"/><circle cx="17" cy="16.5" r="5"/><path d="M17 14v2.5l1.8 1.2"/></svg>',
    "home": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11 12 3.5 21 11M5.5 9v11.5h13V9M10 20.5v-6h4v6"/></svg>',
    "pay": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="M13.8 6.8c-.4-.6-1-.9-1.8-.9-1.1 0-1.9.6-1.9 1.5 0 2 3.8 1.2 3.8 3.2 0 .9-.9 1.5-1.9 1.5-.9 0-1.6-.4-2-1M12 4.8v1.1M12 12.1v1.1M3 21l3-3h5l3-2"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 4.5 5.5v6c0 4.6 3.2 8.6 7.5 10 4.3-1.4 7.5-5.4 7.5-10v-6z"/><path d="M12 8.5v6M9 11.5h6"/></svg>',
    "piggy": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 10.5c.9 0 1.5.5 1.5 1.5v2c0 .8-.5 1.4-1.3 1.5-.6 1.2-1.6 2.2-2.7 2.8V21h-3v-2h-3v2h-3v-3c-1.9-1.2-3-3-3-5 0-3.6 3.4-6.5 7.5-6.5 1.2 0 2.3.2 3.3.7L17.5 5v3.2c.6.6 1.1 1.4 1.5 2.3z"/><path d="M15.5 11h.01M10 8.5h3"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="16.5" cy="6.5" r="2.5"/><path d="M2.5 20.5h19M6 20.5c0-5 1.5-9 4-11.5M10 9C8 8 5.5 8.3 4 10M10 9c.4-2.2 2-3.7 4-4M10 9c2 .1 3.8 1.3 4.5 3.2M10 9c-1.6 1.2-2.4 3.2-2.2 5.2"/></svg>',
    "play": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3.5v17l14-8.5z"/></svg>',
    "chev-l": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M15 4 7 12l8 8"/></svg>',
    "chev-r": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 4 8 8-8 8"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1v2.4H7.6V14h2.8v8z"/></svg>',
    "yt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 7.2c-.2-1-1-1.8-2-2C18.3 4.8 12 4.8 12 4.8s-6.3 0-8 .4c-1 .2-1.8 1-2 2C1.6 9 1.6 12 1.6 12s0 3 .4 4.8c.2 1 1 1.8 2 2 1.7.4 8 .4 8 .4s6.3 0 8-.4c1-.2 1.8-1 2-2 .4-1.8.4-4.8.4-4.8s0-3-.4-4.8zM9.9 15.1V8.9l5.4 3.1z"/></svg>',
}


# ---------- shared blocks ----------
def head(page):
    url = DOMAIN + (page["slug"] if page["slug"] != "/" else "/")
    ld = json.dumps(page["jsonld"], indent=1, ensure_ascii=False)
    extra = page.get("head_extra", "")
    robots = '\n<meta name="robots" content="noindex">' if page.get("noindex") else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page['title']}</title>
<meta name="description" content="{page['description']}">{robots}
<link rel="canonical" href="{url}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['description']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/images/og-image.jpg">
<meta name="theme-color" content="#1b1929">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind:wght@400;500;700&family=Roboto:ital,wght@0,700;0,900;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">{extra}
<script type="application/ld+json">
{ld}
</script>
</head>"""


def header(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append('<li class="mobile-cta"><a class="btn" href="/#contact">Call Us Today</a></li>')
    nav = "\n          ".join(items)
    e, o, h = PHONES["excavation"], PHONES["office"], PHONES["hauling"]
    return f"""
<a class="sr-only" href="#main">Skip to content</a>
<header class="site-header">
  <div class="topbar">
    <div class="container">
      <a href="tel:{e[1]}">Excavation {e[0]}</a>
      <a href="tel:{o[1]}">Office {o[0]}</a>
      <a href="tel:{h[1]}">Hauling {h[0]}</a>
    </div>
  </div>
  <div class="navbar">
    <div class="container">
      <a class="logo-link" href="/" aria-label="{BIZ} home">
        <img src="/images/logo.webp" alt="Vaughn Company, Inc. logo" width="345" height="138">
      </a>
      <nav class="main-nav" aria-label="Main">
        <ul>
          {nav}
        </ul>
      </nav>
      <a class="btn nav-cta" href="/#contact">Call Us Today</a>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>"""


def footer():
    links = "\n          ".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV + [("/privacy-policy", "Privacy Policy")])
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <img class="footer-logo" src="/images/logo-footer.webp" alt="Vaughn Company, Inc. Dirtworks and Hauling logo" width="637" height="359" loading="lazy">
      <dl class="footer-meta">
        <dt>Address</dt>
        <dd>{ADDRESS}</dd>
        <dt>Phone</dt>
        <dd><a href="tel:{tel('office')}">+1 (417) 235-7700</a></dd>
      </dl>
    </div>
    <div class="footer-nav">
      <h2>Navigation</h2>
      <ul>
          {links}
      </ul>
      <div class="social">
        <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Vaughn Company on Facebook">{ICON['fb']}</a>
        <a href="{YOUTUBE}" target="_blank" rel="noopener" aria-label="Vaughn Company on YouTube">{ICON['yt']}</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>&copy; Created by <strong><a href="https://convirswebdesign.com" target="_blank" rel="noopener">Convirs Web Design</a></strong></span>
      <span>All Rights Reserved</span>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>"""


def render(page):
    body_cls = f' class="{page["body_class"]}"' if page.get("body_class") else ""
    html = (head(page) + f"\n<body{body_cls}>" + header(page["slug"]) +
            f'\n<main id="main">\n{page["body"].strip()}\n</main>' + footer() +
            page.get("foot_extra", "") + "\n</body>\n</html>\n")
    assert "\u2014" not in html, page["slug"]
    out = os.path.join(ROOT, page["file"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", page["file"])


# ---------- JSON-LD ----------
ORG = {
    "@context": "https://schema.org",
    "@type": "GeneralContractor",
    "@id": DOMAIN + "/#business",
    "name": BIZ,
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/images/logo.webp",
    "image": DOMAIN + "/images/og-image.jpg",
    "description": "Excavation, material hauling, dirt work and rock sales in Southwest Missouri. Established 1959.",
    "foundingDate": "1959",
    "telephone": "+1-417-235-7700",
    "address": {"@type": "PostalAddress", "streetAddress": "22453 Highway H", "addressLocality": "Monett",
                "addressRegion": "MO", "addressCountry": "US"},
    "contactPoint": [
        {"@type": "ContactPoint", "contactType": "Excavation", "telephone": "+1-417-235-9912"},
        {"@type": "ContactPoint", "contactType": "Hauling", "telephone": "+1-417-236-2269"},
        {"@type": "ContactPoint", "contactType": "Office", "telephone": "+1-417-235-7700"},
    ],
    "sameAs": [FACEBOOK, YOUTUBE],
}


def crumbs(name, slug):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": DOMAIN + slug}]}


# ---------- pages ----------
from pages import home, about, hiring, contact, privacy, notfound  # noqa: E402

PAGES = [
    dict(file="index.html", slug="/", body_class="home",
         title="Excavation, Material Hauling, Dirt Work, Rock Sales | Vaughn Company",
         description="We have the experience to get your earthwork done right the first time - hassle-free, no matter the size. Vaughn Company Inc, established 1959.",
         jsonld=ORG, body=home(ICON, PHONES, ADDRESS)),
    dict(file="about-us/index.html", slug="/about-us",
         title="About us Page | Vaughn Company, Inc.",
         description="Established in 1959 and realize that all jobs are unique and complex. We match our skilled experts and equipment for a project's guaranteed success.",
         jsonld=crumbs("About Us", "/about-us"), body=about(ICON)),
    dict(file="hiring-now/index.html", slug="/hiring-now",
         title="Work For Vaughn Company, Inc. Today",
         description="Located in Southwest Missouri, you will be home every night, paid weekly, have health/dental/vision Insurance, 401K, and Vacation Pay",
         jsonld=crumbs("Hiring Now", "/hiring-now"), body=hiring(ICON, DRIVER_APP, EMPLOY_APP)),
    dict(file="contact-us/index.html", slug="/contact-us",
         title="Contact Us | Vaughn Company, Inc.",
         description="Give us a call today to get your earthwork done right the first time - hassle-free, no matter the size. Excavation 417-235-9912 | Hauling 417-236-2269",
         jsonld=crumbs("Contact Us", "/contact-us"), body=contact()),
    dict(file="privacy-policy/index.html", slug="/privacy-policy",
         title="Vaughn Company, Inc | Privacy Policy",
         description="Privacy Policy for Vaughn Company, Inc., excavation, material hauling, dirt work and rock sales in Monett, Missouri.",
         jsonld=crumbs("Privacy Policy", "/privacy-policy"), body=privacy(),
         foot_extra='\n<script src="https://app.termageddon.com/js/termageddon.js"></script>'),
    dict(file="404.html", slug="/404", noindex=True,
         title="Page Not Found | Vaughn Company, Inc.",
         description="The page you are looking for could not be found.",
         jsonld=ORG, body=notfound()),
]

if __name__ == "__main__":
    for p in PAGES:
        render(p)
