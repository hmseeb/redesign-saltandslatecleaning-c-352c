# -*- coding: utf-8 -*-
"""Shell: <head>, header, footer, hero, quote form, CTA band."""

from data import (BIZ, OFFICES, RESIDENTIAL, COMMERCIAL, STATES, PAGE_HERO,
                  HERO_SLIDES)

SITE = "https://saltandslatecleaning.com"

ARROW = ('<svg class="arw" width="14" height="14" viewBox="0 0 16 16" aria-hidden="true" '
         'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M3 8h9M8.5 4l4 4-4 4"/></svg>')
CHEV = ('<svg class="chev" viewBox="0 0 12 8" aria-hidden="true" fill="none" stroke="currentColor" '
        'stroke-width="1.8" stroke-linecap="round"><path d="M1 1.5 6 6.5l5-5"/></svg>')


def pic(jpg, webp, alt, cls="", loading="lazy", sizes=None, extra=""):
    """<picture> with webp source + jpg fallback (both files ship in the repo)."""
    src = "/images/source/%s.jpg" % jpg if jpg else "/images/source/%s.webp" % webp
    attrs = ' class="%s"' % cls if cls else ""
    szs = ' sizes="%s"' % sizes if sizes else ""
    img = ('<img src="%s" alt="%s" loading="%s" decoding="async"%s%s%s>'
           % (src, alt, loading, attrs, szs, (" " + extra) if extra else ""))
    if webp and jpg:
        return ('<picture><source type="image/webp" srcset="/images/source/%s.webp">%s</picture>'
                % (webp, img))
    return img


def _mega(items, base, foot_href, foot_label, note=None, wide=True):
    links = "".join(
        '<a class="mega__link" href="%s%s/">%s</a>' % (base, slug, label) if slug
        else '<span class="mega__link" style="color:var(--muted);cursor:default">%s</span>' % label
        for slug, label in items)
    extra = '<span class="mega__note">%s</span>' % note if note else ""
    return ('<div class="mega%s"><div class="mega__grid">%s</div>'
            '<div class="mega__foot"><a class="link-arrow" href="%s">%s %s</a>%s</div></div>'
            % (" mega--wide" if wide else " mega--narrow", links, foot_href, foot_label, ARROW, extra))


def header(path):
    res_items = [(s, l) for s, l, _ in RESIDENTIAL]
    com_items = [(s, l) for s, l, _ in COMMERCIAL[:8]]
    loc_items = [(s, l) for s, l, _ in STATES]

    def cur(p):
        return ' aria-current="page"' if path == p else ""

    def sect(prefix):
        return ' aria-current="page"' if path.startswith(prefix) else ""

    nav = """
      <nav class="nav" aria-label="Primary">
        <div class="nav__item">
          <a class="nav__link" href="/services/"%(c_res)s>Residential %(chev)s</a>
          %(mega_res)s
        </div>
        <div class="nav__item">
          <a class="nav__link" href="/commercial/"%(c_com)s>Commercial %(chev)s</a>
          %(mega_com)s
        </div>
        <div class="nav__item">
          <a class="nav__link" href="/locations/"%(c_loc)s>Locations %(chev)s</a>
          %(mega_loc)s
        </div>
        <div class="nav__item"><a class="nav__link" href="/about/"%(c_ab)s>About</a></div>
        <div class="nav__item"><a class="nav__link" href="/#reviews">Reviews</a></div>
      </nav>""" % {
        "chev": CHEV,
        "c_res": sect("/services"), "c_com": sect("/commercial"),
        "c_loc": sect("/locations"), "c_ab": cur("/about/"),
        "mega_res": _mega(res_items, "/services/", "/services/", "All residential services",
                          "9 home services"),
        "mega_com": _mega(com_items, "/commercial/", "/commercial/", "All 15 industries",
                          "15 industries served"),
        "mega_loc": _mega(loc_items, "/locations/", "/locations/", "All service areas",
                          "106 cities", wide=False),
    }

    drawer_res = "".join('<a href="/services/%s/">%s</a>' % (s, l) for s, l, _ in RESIDENTIAL)
    drawer_com = "".join('<a href="/commercial/%s/">%s</a>' % (s, l) for s, l, _ in COMMERCIAL[:8])
    drawer_loc = "".join('<a href="/locations/%s/">%s</a>' % (s, l) for s, l, _ in STATES)

    return """
  <div class="topbar">
    <div class="wrap topbar__in">
      <span class="topbar__areas">Serving Utah · Arizona · Nevada · Texas — 100+ communities</span>
      <span class="topbar__right">
        <span class="topbar__badge"><span class="stars" aria-hidden="true">★★★★★</span>
          <span>%(rating)s on Google · %(reviews)s reviews</span></span>
        <a href="tel:%(tel)s">%(phone)s</a>
      </span>
    </div>
  </div>

  <header class="site-header">
    <div class="wrap site-header__in">
      <a class="brand" href="/" aria-label="%(name)s — home">
        <span class="brand__mark" aria-hidden="true">S&amp;S</span>
        <span class="brand__text">
          <span class="brand__name">Salt &amp; Slate</span>
          <span class="brand__sub">Cleaning Company</span>
        </span>
      </a>
      %(nav)s
      <div class="header__cta">
        <a class="header__phone" href="tel:%(tel)s">%(phone)s</a>
        <a class="btn btn--primary btn--sm" href="#quote">Get a Free Quote</a>
      </div>
      <button class="burger" type="button" aria-expanded="false"
              aria-controls="mobile-drawer" aria-label="Open menu"><span></span></button>
    </div>
  </header>

  <div class="drawer" id="mobile-drawer">
    <div class="drawer__panel" role="dialog" aria-label="Site menu" aria-modal="true">
      <div class="drawer__top">
        <span class="brand__name">Salt &amp; Slate</span>
        <button class="drawer__close" type="button" aria-label="Close menu">&times;</button>
      </div>
      <details><summary>Residential</summary><div class="drawer__sub">
        <a href="/services/"><strong>All residential services</strong></a>%(d_res)s</div></details>
      <details><summary>Commercial</summary><div class="drawer__sub">
        <a href="/commercial/"><strong>All 15 industries</strong></a>%(d_com)s</div></details>
      <details><summary>Locations</summary><div class="drawer__sub">
        <a href="/locations/"><strong>All service areas</strong></a>%(d_loc)s</div></details>
      <a class="drawer__flat" href="/about/">About</a>
      <a class="drawer__flat" href="/#reviews">Reviews</a>
      <a class="drawer__flat" href="/review">Leave us a review</a>
      <div class="drawer__cta">
        <a class="btn btn--primary btn--block" href="#quote">Get a Free Quote</a>
        <a class="btn btn--ghost btn--block" href="tel:%(tel)s">Call %(phone)s</a>
      </div>
    </div>
  </div>
""" % {"nav": nav, "tel": BIZ["tel"], "phone": BIZ["phone"], "name": BIZ["name"],
       "rating": BIZ["rating"], "reviews": BIZ["reviews"],
       "d_res": drawer_res, "d_com": drawer_com, "d_loc": drawer_loc}


def footer():
    res = "".join('<li><a href="/services/%s/">%s</a></li>' % (s, l) for s, l, _ in RESIDENTIAL)
    com = "".join('<li><a href="/commercial/%s/">%s</a></li>' % (s, l) for s, l, _ in COMMERCIAL[:8])
    com_more = " · ".join(l for s, l, _ in COMMERCIAL[8:])
    locs = "".join('<li><a href="/locations/%s/">%s</a></li>' % (s, l) for s, l, _ in STATES)
    offices = "<br>".join("%s, %s" % (o[0], o[2].rsplit(" ", 1)[0].split(", ")[-1] + "")
                          for o in OFFICES)
    office_line = ("Salt Lake City, UT · Park City, UT · Draper, UT<br>"
                   "Scottsdale, AZ · Las Vegas, NV · Frisco, TX")
    return """
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer__top">
        <div class="footer__brand">
          <a class="brand" href="/" aria-label="%(name)s — home">
            <span class="brand__mark" aria-hidden="true">S&amp;S</span>
            <span class="brand__text"><span class="brand__name">Salt &amp; Slate</span>
            <span class="brand__sub">Cleaning Company</span></span>
          </a>
          <p class="footer__about">Premium home and office cleaning serving 100+ communities across
            Utah, Arizona, Nevada, and Texas. Background-checked teams, consistent quality, every visit.</p>
          <span class="footer__rating"><span class="stars" aria-hidden="true">★★★★★</span>
            Salt &amp; Slate: %(reviews)s Google reviews across %(locations)s locations.</span>
          <div class="footer__contact">
            <a href="tel:%(tel)s">%(phone)s</a>
            <a href="mailto:%(email)s">%(email)s</a>
          </div>
          <div class="footer__offices">%(office_line)s</div>
          <div class="footer__social">
            <a href="%(ig)s" rel="noopener" target="_blank" aria-label="Salt &amp; Slate on Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg></a>
            <a href="%(fb)s" rel="noopener" target="_blank" aria-label="Salt &amp; Slate on Facebook">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7h2.6l.4-3h-3V9.1c0-.9.3-1.5 1.6-1.5H16.6V4.9c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.4-4 4.1V11H7.8v3h2.4v7z"/></svg></a>
          </div>
        </div>

        <div class="footer__col">
          <h3>Home Cleaning</h3>
          <ul>%(res)s</ul>
          <a class="link-arrow" href="/services/">All residential services %(arw)s</a>
        </div>

        <div class="footer__col">
          <h3>Commercial Cleaning</h3>
          <ul>%(com)s</ul>
          <a class="link-arrow" href="/commercial/">All commercial services %(arw)s</a>
          <p class="footer__offices">Also serving: %(com_more)s</p>
        </div>

        <div class="footer__col">
          <h3>Service Areas</h3>
          <ul>%(locs)s</ul>
          <a class="link-arrow" href="/locations/">All service areas %(arw)s</a>
          <div class="footer__sublabel">Company</div>
          <ul>
            <li><a href="/about/">About Salt and Slate Cleaning Company</a></li>
            <li><a href="/#reviews">Customer Reviews</a></li>
            <li><a href="/#quote">Request a Quote</a></li>
          </ul>
          <a class="footer__review" href="/review">%(star)s Leave us a review</a>
        </div>
      </div>

      <div class="footer__strip">
        <div><strong style="color:#fff">Ready for a cleaner space?</strong>
          Request a quote or text or call <a href="tel:%(tel)s">%(phone)s</a>.</div>
        <div class="footer__strip-cta">
          <a class="btn btn--primary btn--sm" href="#quote">Request a Quote</a>
          <a class="btn btn--light btn--sm" href="tel:%(tel)s">Call %(phone)s</a>
        </div>
      </div>

      <div class="footer__bottom">
        <span>&copy; %(year)s Salt &amp; Slate Cleaning Company</span>
        <span><a href="/review">Leave us a review</a> &nbsp;·&nbsp;
              <a href="/locations/">Service areas</a> &nbsp;·&nbsp;
              <a href="/about/">About us</a></span>
      </div>
    </div>
  </footer>

  <div class="mobile-bar">
    <a class="btn btn--ghost btn--sm" href="tel:%(tel)s">Call now</a>
    <a class="btn btn--primary btn--sm" href="#quote">Free quote</a>
  </div>
""" % {"name": BIZ["name"], "tel": BIZ["tel"], "phone": BIZ["phone"], "email": BIZ["email"],
       "reviews": BIZ["reviews"], "locations": BIZ["locations"], "ig": BIZ["instagram"],
       "fb": BIZ["facebook"], "res": res, "com": com, "com_more": com_more, "locs": locs,
       "office_line": office_line, "year": BIZ["year"], "arw": ARROW,
       "star": '<span class="stars" aria-hidden="true">★</span>'}


SERVICE_OPTIONS = ([l.replace("&amp;", "&") for _, l, _ in RESIDENTIAL] +
                   [l.replace("&amp;", "&") for _, l, _ in COMMERCIAL] +
                   ["Something else / not sure"])


def quote_section(form_name="Quote request", default_service=None):
    opts = "".join('<option%s>%s</option>'
                   % (' selected' if default_service and s == default_service else '', s)
                   for s in SERVICE_OPTIONS)
    return """
  <section class="band quote" id="quote">
    <div class="wrap quote__in">
      <div class="quote__aside">
        <span class="eyebrow">Free quote · No obligation</span>
        <h2>Tell us about your space</h2>
        <p>Send the details and we'll come back with flat-rate pricing so you know the full cost
          upfront. Prefer to talk it through? Text or call — we answer.</p>
        <ul class="quote__list">
          <li><span aria-hidden="true">✓</span><span><b>Flat-rate pricing</b>No hourly surprises.
            You approve the scope before any work begins.</span></li>
          <li><span aria-hidden="true">✓</span><span><b>Licensed, insured, background-checked</b>
            Every cleaner, every visit. Certificate of insurance on request.</span></li>
          <li><span aria-hidden="true">✓</span><span><b>24-hour satisfaction guarantee</b>
            If anything falls short, we return and make it right at no charge.</span></li>
        </ul>
        <div class="contact-lines">
          <a href="tel:%(tel)s">%(phone)s</a>
          <a href="sms:%(tel)s?body=%(sms)s">Text us for a quote</a>
          <a href="mailto:%(email)s">%(email)s</a>
          <span>Salt Lake City · Park City · Draper · Scottsdale · Las Vegas · Frisco</span>
          <a href="/review"><strong>Already a client? Leave us a review &rarr;</strong></a>
        </div>
      </div>

      <div>
        <div class="alert" hidden>
          <span class="alert__ico" aria-hidden="true">&#10003;</span>
          <span><b>Thanks, your message was sent.</b>
            A Salt &amp; Slate team member will follow up shortly — usually within one business day.</span>
        </div>
        <div class="form-card">
          <form method="POST" action="%(action)s" data-leadr>
            <input type="hidden" name="_form" value="%(form_name)s">
            <input type="hidden" name="_page" value="">
            <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">
            <div class="form-grid">
              <div class="field">
                <label for="q-name">Your name</label>
                <input id="q-name" type="text" name="name" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="q-phone">Phone</label>
                <input id="q-phone" type="tel" name="phone" autocomplete="tel" required>
              </div>
              <div class="field field--full">
                <label for="q-email">Email</label>
                <input id="q-email" type="email" name="email" autocomplete="email" required>
              </div>
              <div class="field">
                <label for="q-service">Service needed</label>
                <select id="q-service" name="Service needed">%(opts)s</select>
              </div>
              <div class="field">
                <label for="q-type">Property type</label>
                <select id="q-type" name="Property type">
                  <option>Home</option><option>Apartment or condo</option>
                  <option>Short-term rental</option><option>Vacation or second home</option>
                  <option>Office or commercial space</option><option>New build or renovation</option>
                </select>
              </div>
              <div class="field">
                <label for="q-city">City &amp; state</label>
                <input id="q-city" type="text" name="City and state" placeholder="e.g. Park City, UT">
              </div>
              <div class="field">
                <label for="q-date">Preferred date</label>
                <input id="q-date" type="date" name="Preferred date">
              </div>
              <div class="field field--full">
                <label for="q-size">Square footage, bedrooms &amp; bathrooms</label>
                <input id="q-size" type="text" name="Property size" placeholder="e.g. 3,200 sq ft · 4 bed · 3 bath">
              </div>
              <div class="field field--full">
                <label for="q-msg">Anything we should know?</label>
                <textarea id="q-msg" name="Project details" placeholder="Pets, surfaces that need special care, access details, timing…"></textarea>
              </div>
            </div>
            <div class="form-foot">
              <button class="btn btn--primary btn--block" type="submit">Request my free quote</button>
              <p>We use your details only to prepare your quote and schedule your cleaning.</p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
""" % {"action": BIZ["form_action"], "form_name": form_name, "opts": opts,
       "tel": BIZ["tel"], "phone": BIZ["phone"], "email": BIZ["email"], "sms": BIZ["sms_body"]}


def cta_band(title, body=""):
    return """
  <section class="band cta-band">
    <div class="wrap">
      <h2>%(title)s</h2>
      %(body)s
      <div class="hero__actions">
        <a class="btn btn--primary" href="#quote">Get a Free Quote</a>
        <a class="btn btn--light" href="sms:%(tel)s?body=%(sms)s">Text or Call %(phone)s</a>
      </div>
    </div>
  </section>
""" % {"title": title, "body": ("<p>%s</p>" % body) if body else "",
       "tel": BIZ["tel"], "phone": BIZ["phone"], "sms": BIZ["sms_body"]}


def crumbs(trail):
    """trail = [(label, href_or_None), ...] — last item is current."""
    out = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        if href and not last:
            out.append("<li><a href=\"%s\">%s</a></li>" % (href, label))
        else:
            out.append("<li><span aria-current=\"page\">%s</span></li>" % label)
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(out)


def hero(path, title, lede, eyebrow=None, trail=None, cta_label="Get a Free Quote"):
    media = PAGE_HERO.get(path)
    cls = "hero hero--page" + (" has-media" if media else "")
    inner = []
    if trail:
        inner.append(crumbs(trail))
    if eyebrow:
        inner.append('<span class="eyebrow eyebrow--light">%s</span>'
                     % eyebrow.replace("&", "&amp;").replace("&amp;amp;", "&amp;"))
    inner.append('<span class="hero__badge"><span class="stars" aria-hidden="true">★★★★★</span>'
                 '<b>%s on Google</b> · %s reviews across all %s Salt &amp; Slate locations</span>'
                 % (BIZ["rating"], BIZ["reviews"], BIZ["locations"]))
    inner.append("<h1>%s</h1>" % title)
    if lede:
        inner.append('<p class="hero__lede">%s</p>' % lede)
    inner.append('<div class="hero__actions">'
                 '<a class="btn btn--primary" href="#quote">%s</a>'
                 '<a class="btn btn--light" href="tel:%s">Call %s</a></div>'
                 % (cta_label, BIZ["tel"], BIZ["phone"]))
    col = "<div>%s</div>" % "".join(inner)
    if media:
        jpg, webp, alt = media
        col += ('<div class="hero__media"><div class="hero__frame">%s</div></div>'
                % pic(jpg, webp, alt, loading="eager",
                      sizes="(max-width: 900px) 100vw, 46vw"))
    return '<section class="%s"><div class="wrap hero__in">%s</div></section>' % (cls, col)


def home_hero():
    slides = []
    dots = []
    for i, (jpg, webp, alt) in enumerate(HERO_SLIDES):
        slides.append('<div class="hero__slide%s">%s</div>'
                      % (" is-active" if i == 0 else "",
                         pic(jpg, webp, alt, loading="eager" if i == 0 else "lazy",
                             sizes="(max-width: 900px) 100vw, 46vw")))
        dots.append('<button class="hero__dot%s" type="button" role="tab" aria-selected="%s" '
                    'aria-label="Show photo %d"></button>'
                    % (" is-active" if i == 0 else "", "true" if i == 0 else "false", i + 1))
    return """
  <section class="hero hero--home hero--split">
    <div class="wrap hero__in">
      <div>
        <span class="hero__badge"><span class="stars" aria-hidden="true">★★★★★</span>
          <b>%(rating)s on Google</b> · %(reviews)s reviews</span>
        <h1>Professional cleaning for homes and businesses that expect more</h1>
        <p class="hero__lede">Licensed, insured, background-checked professionals serving homes and
          businesses across Utah, Arizona, Nevada, and Texas. Flat-rate pricing and a 24-hour
          satisfaction guarantee on every cleaning.</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="#quote">Get Free Quote</a>
          <a class="btn btn--light" href="sms:%(tel)s?body=%(sms)s">Text or Call %(phone)s</a>
        </div>
        <p class="hero__note">No contracts · Flat-rate pricing · 24-hour satisfaction guarantee</p>
      </div>
      <div class="hero__media">
        <div class="hero__frame" data-hero-slides role="tablist" aria-label="Recent Salt &amp; Slate cleanings">%(slides)s</div>
        <div class="hero__dots">%(dots)s</div>
        <div class="hero__chip">
          <span class="hero__chip-num">%(rating)s</span>
          <span><strong>%(reviews)s Google reviews</strong><small>Across all %(locations)s Salt &amp; Slate locations</small></span>
        </div>
      </div>
    </div>
  </section>
""" % {"rating": BIZ["rating"], "reviews": BIZ["reviews"], "locations": BIZ["locations"],
       "tel": BIZ["tel"], "phone": BIZ["phone"], "sms": BIZ["sms_body"],
       "slides": "".join(slides), "dots": "".join(dots)}


def jsonld(path, title, description):
    offices = ",".join("""{"@type":"LocalBusiness","@id":"%(site)s/#office-%(i)d",
      "name":"Salt & Slate Cleaning Company — %(city)s","telephone":"%(tel)s",
      "email":"%(email)s","priceRange":"$$$",
      "image":"%(site)s/images/source/00-hero-home.jpg",
      "address":{"@type":"PostalAddress","streetAddress":"%(street)s",
        "addressLocality":"%(loc)s","addressRegion":"%(region)s","postalCode":"%(zip)s",
        "addressCountry":"US"},
      "parentOrganization":{"@id":"%(site)s/#org"}}""" % {
        "site": SITE, "i": i, "city": o[0], "tel": o[4], "email": BIZ["email"],
        "street": o[1], "loc": o[2].rsplit(",", 1)[0],
        "region": o[2].rsplit(",", 1)[1].strip().split(" ")[0],
        "zip": o[2].rsplit(" ", 1)[1],
    } for i, o in enumerate(OFFICES))

    return """<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":["Organization","CleaningService"],"@id":"%(site)s/#org",
 "name":"Salt & Slate Cleaning Company","url":"%(site)s/","telephone":"%(tel)s",
 "email":"%(email)s","priceRange":"$$$",
 "description":"Premium home and office cleaning serving 100+ communities across Utah, Arizona, Nevada, and Texas.",
 "areaServed":[{"@type":"State","name":"Utah"},{"@type":"State","name":"Arizona"},
   {"@type":"State","name":"Nevada"},{"@type":"State","name":"Texas"}],
 "sameAs":["%(ig)s","%(fb)s"],
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"%(rating)s","reviewCount":"%(reviews)s"}},
{"@type":"WebPage","@id":"%(site)s%(path)s","url":"%(site)s%(path)s","name":"%(title)s",
 "description":"%(desc)s","isPartOf":{"@id":"%(site)s/#org"}},
%(offices)s]}
</script>""" % {"site": SITE, "tel": BIZ["tel"], "email": BIZ["email"], "ig": BIZ["instagram"],
                "fb": BIZ["facebook"], "rating": BIZ["rating"], "reviews": BIZ["reviews"],
                "path": path, "title": title.replace('"', ""), "desc": description.replace('"', ""),
                "offices": offices}


def page(path, title, description, body, og_image="/images/source/00-hero-home.jpg"):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(site)s%(path)s">
<meta name="theme-color" content="#0d1316">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Salt &amp; Slate Cleaning Company">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(site)s%(path)s">
<meta property="og:image" content="%(site)s%(og)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(site)s%(og)s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="stylesheet" href="/assets/css/site.css">
%(jsonld)s
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
<script src="/assets/js/site.js" defer></script>
</body>
</html>
""" % {"title": title, "desc": description, "site": SITE, "path": path, "og": og_image,
       "jsonld": jsonld(path, title, description), "header": header(path),
       "body": body, "footer": footer()}
