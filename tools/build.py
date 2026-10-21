# -*- coding: utf-8 -*-
"""Static site generator for the Salt & Slate Cleaning Company redesign."""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data import (BIZ, OFFICES, RESIDENTIAL, COMMERCIAL, STATES, PICKER, WHY,
                  HOW_IT_WORKS, RECOGNIZED, HOME_STATE_CITIES, BEFORE_AFTER,
                  REVIEWS, SHOWCASE)
import layout
from layout import (ARROW, pic, page, home_hero, hero, quote_section, cta_band)
from parse import parse, esc, inline
from render import render_sections, render_intro

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, ".git", "gsb-source-pages")

PAGES = [
    ("01.md", "/services/", [("Home", "/"), ("Residential", None)]),
    ("02.md", "/services/recurring-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Standard &amp; Recurring Cleaning", None)]),
    ("03.md", "/services/deep-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Deep Cleaning", None)]),
    ("04.md", "/services/move-in-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Move-In Cleaning", None)]),
    ("05.md", "/services/move-out-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Move-Out Cleaning", None)]),
    ("06.md", "/services/vacation-home-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Vacation Home Cleaning", None)]),
    ("07.md", "/services/airbnb-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Airbnb &amp; Rental Cleaning", None)]),
    ("08.md", "/services/estate-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Estate Cleaning", None)]),
    ("09.md", "/services/specialty-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Specialty Cleaning", None)]),
    ("10.md", "/services/post-construction-cleaning/", [("Home", "/"), ("Residential", "/services/"), ("Post-Construction Cleaning", None)]),
    ("11.md", "/commercial/", [("Home", "/"), ("Commercial", None)]),
    ("12.md", "/commercial/office-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Office Cleaning", None)]),
    ("13.md", "/commercial/medical-office-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Medical Office Cleaning", None)]),
    ("14.md", "/commercial/dental-office-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Dental Office Cleaning", None)]),
    ("15.md", "/commercial/law-firm-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Law Firm Cleaning", None)]),
    ("16.md", "/commercial/gym-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Gym &amp; Fitness Cleaning", None)]),
    ("17.md", "/commercial/restaurant-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Restaurant Cleaning", None)]),
    ("18.md", "/commercial/warehouse-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Warehouse Cleaning", None)]),
    ("19.md", "/commercial/retail-cleaning/", [("Home", "/"), ("Commercial", "/commercial/"), ("Retail Cleaning", None)]),
    ("20.md", "/locations/", [("Home", "/"), ("Locations", None)]),
    ("21.md", "/locations/utah/", [("Home", "/"), ("Locations", "/locations/"), ("Utah", None)]),
    ("22.md", "/locations/arizona/", [("Home", "/"), ("Locations", "/locations/"), ("Arizona", None)]),
    ("23.md", "/locations/nevada/", [("Home", "/"), ("Locations", "/locations/"), ("Nevada", None)]),
    ("24.md", "/locations/texas/", [("Home", "/"), ("Locations", "/locations/"), ("Texas", None)]),
    ("25.md", "/about/", [("Home", "/"), ("About", None)]),
]


DEFAULT_EYEBROW = {
    "/locations/utah/": "Where We Serve — Utah",
    "/locations/arizona/": "Where We Serve — Arizona",
    "/locations/nevada/": "Where We Serve — Nevada",
    "/locations/texas/": "Where We Serve — Texas",
}


def write(path, html):
    rel = path.strip("/")
    out = os.path.join(ROOT, "index.html") if not rel else os.path.join(ROOT, rel, "index.html")
    d = os.path.dirname(out)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out


def meta_desc(parsed):
    text = parsed["lede"] or parsed["h1"] or ""
    text = re.sub(r"\s*Salt & Slate (provides|serves).*$", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text).strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) > 158:
        cut = text[:158].rsplit(" ", 1)[0]
        text = cut + "…"
    return esc(text).replace('"', "&quot;")


def clean_lede(parsed):
    text = parsed["lede"] or ""
    text = re.sub(r"\s{2,}", " ", text).strip()
    return inline(text)


# ------------------------------------------------------------------ home page
def home_services():
    cards = "".join(
        '<a class="card card--num" data-n="%02d" href="/services/%s/"><h3>%s</h3><p>%s</p>'
        '<span class="link-arrow">Learn more %s</span></a>'
        % (i + 1, slug, label, tag, ARROW)
        for i, (slug, label, tag) in enumerate(RESIDENTIAL))
    return """
  <section class="band" id="residential">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow">Residential</span>
        <h2>Cleaning Services for Your Home</h2>
        <p>Nine distinct services designed around the way you actually live — every one performed by
          licensed, background-checked, and insured professionals and backed by our 24-hour
          satisfaction guarantee.</p>
      </div>
      <div class="grid grid--3">%s</div>
      <div class="review-actions" style="justify-content:flex-start">
        <a class="btn btn--primary" href="#quote">Get Free Quote</a>
        <a class="btn btn--ghost" href="/services/">All residential services</a>
      </div>
    </div>
  </section>""" % cards


def home_commercial():
    cards = []
    for slug, label, desc in COMMERCIAL:
        if slug:
            cards.append('<a class="card" href="/commercial/%s/"><h3>%s</h3><p>%s</p>'
                         '<span class="link-arrow">Learn more %s</span></a>'
                         % (slug, label, desc, ARROW))
        else:
            cards.append('<div class="card card--static"><span class="card__tag">Also served</span>'
                         '<h3>%s</h3><p>%s</p></div>' % (label, desc))
    return """
  <section class="band band--mist" id="commercial">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow">Commercial</span>
        <h2>Cleaning for Your Business</h2>
        <p>Industry-specific cleaning protocols for offices, medical facilities, restaurants, gyms,
          and more. Detailed checklists, after-hours scheduling, and commercial-grade products
          tailored to how your business operates.</p>
      </div>
      <div class="grid grid--3">%s</div>
      <div class="review-actions" style="justify-content:flex-start">
        <a class="btn btn--primary" href="#quote">Request Commercial Quote</a>
        <a class="btn btn--ghost" href="/commercial/">All 15 industries</a>
      </div>
    </div>
  </section>""" % "".join(cards)


def home_why():
    feats = "".join(
        '<div class="feature"><span class="feature__ico" aria-hidden="true">%02d</span>'
        '<div><h3>%s</h3><p>%s</p></div></div>' % (i + 1, t, d)
        for i, (t, d) in enumerate(WHY))
    img = pic("12-why-salt-and-slate", None,
              "Salt &amp; Slate cleaning professional at work in a luxury kitchen",
              sizes="(max-width: 900px) 100vw, 46vw")
    return """
  <section class="band">
    <div class="wrap split" data-reveal>
      <div>
        <div class="sec-head" style="margin-bottom:2rem">
          <span class="eyebrow">Why Salt &amp; Slate</span>
          <h2>What sets us apart</h2>
        </div>
        <div class="features" style="grid-template-columns:1fr">%s</div>
        <div class="review-actions" style="justify-content:flex-start;margin-top:2rem">
          <a class="btn btn--ghost" href="/about/">Learn About Us</a>
        </div>
      </div>
      <div class="split__media">%s</div>
    </div>
  </section>""" % (feats, img)


def home_before_after():
    items = []
    for n, (cap, bj, bw, aj, aw, balt, aalt) in enumerate(BEFORE_AFTER):
        items.append("""
        <figure class="ba">
          <div class="ba__stage">
            %s
            <div class="ba__after">%s</div>
            <span class="ba__tag ba__tag--b">Before</span>
            <span class="ba__tag ba__tag--a">After</span>
            <span class="ba__line" aria-hidden="true"></span>
            <input class="ba__range" type="range" min="0" max="100" value="50" step="1"
                   aria-label="Reveal the after photo — %s">
          </div>
          <figcaption class="ba__cap">%s</figcaption>
        </figure>""" % (pic(bj, bw, balt), pic(aj, aw, aalt), esc(cap), esc(cap)))
    show = "".join(
        '<figure>%s<figcaption>%s</figcaption></figure>'
        % (pic(j, w, alt, sizes="(max-width: 680px) 100vw, 48vw"), esc(cap))
        for j, w, alt, cap in SHOWCASE)
    return """
  <section class="band band--sand" id="before-after">
    <div class="wrap" data-reveal>
      <div class="sec-head sec-head--center">
        <span class="eyebrow">Before &amp; After</span>
        <h2>Real cleanings, real customers</h2>
        <p>Drag the handle on any photo to see the difference. Every image below is from an actual
          Salt &amp; Slate job — luxury homes, post-construction handovers, and deep cleans.</p>
      </div>
      <div class="ba-grid">%s</div>
      <div class="showcase">%s</div>
    </div>
  </section>""" % ("".join(items), show)


def home_recognized():
    cards = "".join(
        '<div class="recog__card"><div class="recog__kicker">Recognized by</div>'
        '<h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in RECOGNIZED)
    return """
  <section class="band band--ink">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow eyebrow--light">Recognized By</span>
        <h2>Trusted with the events and estates that demand discretion</h2>
      </div>
      <div class="recog">%s</div>
      <p class="disclaimer">References describe engagements where the listed entity directly
        contracted Salt &amp; Slate. No endorsement or affiliation is implied beyond the scope
        described.</p>
    </div>
  </section>""" % cards


def home_reviews():
    def card(name, quote, when):
        initials = "".join(w[0] for w in name.split()[:2]).upper()
        return ('<figure class="review"><div class="stars" aria-hidden="true">★★★★★</div>'
                '<blockquote class="review__q">&ldquo;%s&rdquo;</blockquote>'
                '<figcaption class="review__who"><span class="review__av" aria-hidden="true">%s</span>'
                '<span class="review__meta"><b>%s</b>%s · on Google</span></figcaption></figure>'
                % (quote, initials, name, when))

    half = (len(REVIEWS) + 1) // 2
    row_a = "".join(card(*r) for r in REVIEWS[:half])
    row_b = "".join(card(*r) for r in REVIEWS[half:])
    return """
  <section class="band band--sand" id="reviews">
    <div class="wrap" data-reveal>
      <div class="sec-head sec-head--center">
        <span class="eyebrow">Verified Google Reviews</span>
        <h2>What our clients are saying</h2>
        <p>Selected customer reviews from Salt &amp; Slate locations — %(reviews)s Google reviews
          across %(locations)s offices, averaging %(rating)s stars.</p>
      </div>
    </div>
    <div class="wrap">
      <div class="rev-rail"><div class="rev-track">%(a)s</div>
      <div class="rev-track rev-track--b">%(b)s</div></div>
      <div class="review-actions">
        <a class="btn btn--primary" href="/review">Leave us a review</a>
        <a class="btn btn--ghost" href="#quote">Get your free quote</a>
      </div>
      <p style="text-align:center;font-size:.82rem;color:var(--muted);margin-top:1.2rem">
        Powered by Google</p>
    </div>
  </section>""" % {"a": row_a, "b": row_b, "reviews": BIZ["reviews"],
                   "locations": BIZ["locations"], "rating": BIZ["rating"]}


def home_areas():
    cards = []
    for slug, name, _desc in STATES:
        cities, more = HOME_STATE_CITIES[slug]
        cards.append('<a class="state" href="/locations/%s/"><h3>%s</h3>'
                     '<p class="state__cities">%s</p><span class="link-arrow">%s %s</span></a>'
                     % (slug, name, cities, more or "View service area", ARROW))
    return """
  <section class="band" id="locations">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow">Where We Serve</span>
        <h2>Service areas across four states</h2>
        <p>Residential and commercial cleaning across 106 cities in Utah, Arizona, Nevada, and Texas
          — with offices in Salt Lake City, Park City, Draper, Scottsdale, Las Vegas, and Frisco.</p>
      </div>
      <div class="state-grid">%s</div>
      <div class="review-actions" style="justify-content:flex-start">
        <a class="btn btn--ghost" href="/locations/">View All Service Areas</a>
      </div>
    </div>
  </section>""" % "".join(cards)


def home_picker():
    cards = "".join(
        '<a class="picker__card" href="%s"><strong>%s</strong><span>%s</span>'
        '<em>%s %s</em></a>' % (href, t, d, c, ARROW) for t, d, c, href in PICKER)
    return """
  <section class="band band--mist">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow">Find your clean</span>
        <h2>What would you like help with?</h2>
        <p>Choose what fits your space. See the checklist, compare the options and request a quote.</p>
      </div>
      <div class="picker">%s</div>
      <p class="picker__note">Moving in? <a href="/services/move-in-cleaning/">See move-in cleaning</a>.
        Maintaining a second home?
        <a href="/services/vacation-home-cleaning/">Explore vacation-home care</a>.</p>
    </div>
  </section>""" % cards


def home_trust():
    items = [("4", "States Served"), ("100+", "Communities Served"),
             ("100%", "Background Checked"), ("100%", "Satisfaction Guarantee")]
    return ('<section class="trust"><div class="wrap"><div class="trust__grid">%s</div></div></section>'
            % "".join('<div class="trust__item"><div class="trust__n">%s</div>'
                      '<div class="trust__l">%s</div></div>' % (n, l) for n, l in items))


def home_how():
    steps = "".join('<div class="step" data-n="%s"><h3>%s</h3><p>%s</p></div>' % s
                    for s in HOW_IT_WORKS)
    return """
  <section class="band band--ink">
    <div class="wrap" data-reveal>
      <div class="sec-head">
        <span class="eyebrow eyebrow--light">How It Works</span>
        <h2>Three steps to a space you are proud of</h2>
      </div>
      <div class="steps steps--3">%s</div>
      <div class="review-actions" style="justify-content:flex-start;margin-top:2.6rem">
        <a class="btn btn--primary" href="#quote">Book Your Cleaning</a>
        <a class="btn btn--light" href="tel:%s">Call %s</a>
      </div>
    </div>
  </section>""" % (steps, BIZ["tel"], BIZ["phone"])


def build_home():
    body = "".join([
        home_hero(),
        home_trust(),
        home_picker(),
        home_services(),
        home_commercial(),
        home_why(),
        home_before_after(),
        home_recognized(),
        home_reviews(),
        home_areas(),
        home_how(),
        cta_band("Your property. Our standard.",
                 "Background-checked teams, flat-rate pricing, 24-hour satisfaction guarantee. "
                 "Serving homes and businesses across Utah, Arizona, Nevada, and Texas."),
        quote_section("Quote request"),
    ])
    html = page("/", "Salt &amp; Slate Cleaning Company | Home &amp; Commercial Cleaning in UT, AZ, NV &amp; TX",
                "Licensed, insured, background-checked cleaning professionals serving homes and "
                "businesses across Utah, Arizona, Nevada and Texas. Flat-rate pricing and a "
                "24-hour satisfaction guarantee.",
                body)
    write("/", html)


# ------------------------------------------------------------- scraped pages
def build_page(src, path, trail):
    parsed = parse(os.path.join(SRC, src))
    sections, final_cta = render_sections(parsed)
    media = layout.PAGE_HERO.get(path)
    if media and media[0]:
        og = "/images/source/%s.jpg" % media[0]
    elif media and media[1]:
        og = "/images/source/%s.webp" % media[1]
    else:
        og = "/images/source/00-hero-home.jpg"

    body = "".join([
        hero(path, inline(parsed["h1"]), clean_lede(parsed),
             eyebrow=parsed["eyebrow"] or DEFAULT_EYEBROW.get(path), trail=trail),
        render_intro(parsed),
        sections,
        final_cta or cta_band("Ready for a cleaner space?",
                              "Request a free quote and we'll get you scheduled with a Salt &amp; "
                              "Slate cleaning team within 24 hours."),
        quote_section("Quote request"),
    ])
    title = esc(parsed["title"])
    html = page(path, title, meta_desc(parsed), body, og_image=og)
    write(path, html)
    return path


# -------------------------------------------------------------------- extras
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#16222a"/><stop offset="1" stop-color="#0f6f66"/>
  </linearGradient></defs>
  <rect width="64" height="64" rx="14" fill="url(#g)"/>
  <text x="32" y="42" font-family="Georgia, serif" font-size="27" font-weight="600"
        text-anchor="middle" fill="#ffffff">S&amp;S</text>
</svg>
"""


def build_extras(paths):
    with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON)
    urls = "".join(
        "  <url><loc>%s%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>\n"
        % (layout.SITE, p, "1.0" if p == "/" else ("0.8" if p.count("/") <= 2 else "0.6"))
        for p in paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % layout.SITE)


def main():
    build_home()
    built = ["/"]
    for src, path, trail in PAGES:
        built.append(build_page(src, path, trail))
    build_extras(built)
    print("built %d pages" % len(built))


if __name__ == "__main__":
    main()
