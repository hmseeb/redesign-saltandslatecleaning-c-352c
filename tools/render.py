# -*- coding: utf-8 -*-
"""Render parsed source-page sections into the new design's HTML."""

import re
from data import PICKER
from layout import ARROW, cta_band
from parse import inline, esc, split_card, map_href, tokenize

BAND_CYCLE = ["", " band--mist", "", " band--sand"]


def _head(eyebrow, title, intro_html="", center=False, level=2):
    out = ['<div class="sec-head%s">' % (" sec-head--center" if center else "")]
    if eyebrow:
        out.append('<span class="eyebrow">%s</span>' % esc(eyebrow))
    out.append("<h%d>%s</h%d>" % (level, inline(title), level))
    if intro_html:
        out.append(intro_html)
    out.append("</div>")
    return "".join(out)


def _checklist(items, excl=False):
    cls = "checklist checklist--excl" if excl else "checklist"
    if len(items) > 6:
        cls += " checklist--cols"
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % inline(i) for i in items))


def _cards(cards, static_ok=True):
    out = []
    for inner, href in cards:
        title, desc = split_card(inner)
        target = map_href(href)
        if target:
            out.append('<a class="card" href="%s"><h3>%s</h3>%s<span class="link-arrow">'
                       'Learn more %s</span></a>'
                       % (target, esc(title), "<p>%s</p>" % esc(desc) if desc else "", ARROW))
        else:
            out.append('<div class="card card--static"><h3>%s</h3>%s</div>'
                       % (esc(title), "<p>%s</p>" % esc(desc) if desc else ""))
    cols = 3 if len(out) >= 3 else 2
    return '<div class="grid grid--%d">%s</div>' % (cols, "".join(out))


def _linkchips(links):
    out = []
    for label, href in links:
        label = re.sub(r"\s*→\s*$", "", label).strip()
        target = map_href(href)
        if target:
            out.append('<li><a href="%s">%s %s</a></li>' % (target, esc(label), ARROW))
        else:
            out.append("<li>%s</li>" % esc(label))
    return '<ul class="chips">%s</ul>' % "".join(out)


def _chips(links):
    return '<ul class="chips">%s</ul>' % "".join(
        "<li>%s</li>" % esc(re.sub(r"\s*→\s*$", "", lbl).strip()) for lbl, _h in links)


def _extralinks(links):
    out = []
    for label, href in links:
        label = re.sub(r"\s*→\s*$", "", label).strip()
        target = map_href(href)
        if target:
            out.append('<a class="link-arrow" href="%s">%s %s</a>' % (target, esc(label), ARROW))
    if not out:
        return ""
    return ('<p style="margin-top:1.6rem;display:flex;flex-wrap:wrap;gap:1.4rem">%s</p>'
            % "".join(out))


# ------------------------------------------------------------------ sections
def r_rooms(sec, toks):
    intro = []
    rooms = []
    notes = []
    mode = "inc"
    i = 0
    while i < len(toks):
        kind = toks[i][0]
        val = toks[i][1] if len(toks[i]) > 1 else None
        nxt = toks[i + 1][0] if i + 1 < len(toks) else None
        if kind == "p":
            if nxt in ("mode", "inc"):
                rooms.append({"name": val, "inc": [], "exc": []})
                mode = "inc"
            else:
                intro.append(val)
        elif kind == "mode":
            mode = val
        elif kind == "inc":
            if rooms:
                rooms[-1]["inc"].append(val)
        elif kind == "exc":
            if rooms:
                rooms[-1]["exc"].append(val)
        elif kind == "note":
            notes.append(val)
        elif kind == "h3":
            break
        i += 1

    body = []
    for n, room in enumerate(rooms):
        cols = []
        if room["inc"]:
            cols.append('<div class="room__col"><h5>Included</h5>%s</div>'
                        % _checklist(room["inc"]))
        if room["exc"]:
            cols.append('<div class="room__col"><h5>Not included in this service</h5>%s</div>'
                        % _checklist(room["exc"], excl=True))
        body.append('<details class="room"%s><summary>%s</summary>'
                    '<div class="room__body%s">%s</div></details>'
                    % (" open" if n == 0 else "", esc(room["name"]),
                       " room__body--one" if len(cols) == 1 else "", "".join(cols)))
    html = '<div class="rooms">%s</div>' % "".join(body)
    if notes:
        html += '<div class="notes">%s</div>' % "".join("<p>%s</p>" % inline(x) for x in notes)
    intro_html = "".join("<p>%s</p>" % inline(p) for p in intro)
    return _head(sec["eyebrow"], sec["title"], intro_html) + html, toks[i:]


def r_addons(title, toks, level=2):
    intro = []
    rows = []
    for kind, val in [(t[0], t[1] if len(t) > 1 else None) for t in toks]:
        if kind == "addon":
            rows.append(val)
        elif kind == "p":
            intro.append(val)
    out = _head(None, title, "".join("<p>%s</p>" % inline(p) for p in intro), level=level)
    out += '<div class="addons">%s</div>' % "".join(
        '<div class="addon"><span>%s</span><b>%s</b></div>' % (esc(a), esc(b)) for a, b in rows)
    return out


def r_who(sec, toks):
    paras = [t[1] for t in toks if t[0] == "p"]
    arrows = [t[1] for t in toks if t[0] == "arr"]
    incs = [t[1] for t in toks if t[0] == "inc"]
    out = _head(sec["eyebrow"], sec["title"],
                "".join('<p>%s</p>' % inline(p) for p in paras))
    items = arrows or incs
    if items:
        out += ('<div class="grid grid--2">%s</div>'
                % "".join('<div class="card"><p style="margin:0;color:var(--ink-2)">%s</p></div>'
                          % inline(x) for x in items))
    return out


def r_steps(sec, toks):
    paras = []
    steps = []
    num = None
    for t in toks:
        kind = t[0]
        val = t[1] if len(t) > 1 else None
        if kind == "stepnum":
            num = val
        elif kind == "h3":
            steps.append({"n": num or "%02d" % (len(steps) + 1), "t": val, "p": []})
            num = None
        elif kind == "p":
            if steps:
                steps[-1]["p"].append(val)
            else:
                paras.append(val)
    out = _head(sec["eyebrow"], sec["title"], "".join("<p>%s</p>" % inline(p) for p in paras))
    cls = "steps steps--3" if len(steps) == 3 else "steps"
    out += '<div class="%s">%s</div>' % (cls, "".join(
        '<div class="step" data-n="%s"><h3>%s</h3>%s</div>'
        % (esc(s["n"]), esc(s["t"]), "".join("<p>%s</p>" % inline(p) for p in s["p"]))
        for s in steps))
    return out


def r_faq(sec, toks):
    paras = []
    items = []
    for t in toks:
        kind = t[0]
        val = t[1] if len(t) > 1 else None
        if kind == "h3":
            items.append({"q": val, "a": []})
        elif kind == "p":
            if items:
                items[-1]["a"].append(val)
            else:
                paras.append(val)
        elif kind in ("inc", "arr"):
            if items:
                items[-1]["a"].append(val)
    out = _head(sec["eyebrow"], sec["title"], "".join("<p>%s</p>" % inline(p) for p in paras))
    out += '<div class="faq">%s</div>' % "".join(
        '<details class="faq__item"><summary>%s</summary><div class="faq__a">%s</div></details>'
        % (esc(it["q"]), "".join("<p>%s</p>" % inline(p) for p in it["a"])) for it in items)
    return out


def r_picker(sec, toks):
    paras = [t[1] for t in toks if t[0] == "p" and "](" not in t[1]]
    note = next((t[1] for t in toks if t[0] == "p" and "](" in t[1]), None)
    intro = "".join("<p>%s</p>" % inline(p) for p in paras[:1])
    out = _head(sec["eyebrow"] or "Find your clean", sec["title"], intro)
    out += '<div class="picker">%s</div>' % "".join(
        '<a class="picker__card" href="%s"><strong>%s</strong><span>%s</span>'
        '<em>%s %s</em></a>' % (href, esc(t), esc(d), esc(c), ARROW)
        for t, d, c, href in PICKER)
    if note:
        out += '<p class="picker__note">%s</p>' % inline(note)
    return out


def r_areas(sec, toks):
    out = [_head(sec["eyebrow"], sec["title"], "")]
    pending_p = []
    i = 0
    while i < len(toks):
        t = toks[i]
        kind = t[0]
        i += 1
        if kind == "p":
            pending_p.append(t[1])
            continue
        if pending_p:
            out.append("".join("<p>%s</p>" % inline(p) for p in pending_p))
            pending_p = []
        if kind == "cards":
            out.append(_cards(t[1]))
        elif kind == "extralinks":
            out.append(_extralinks(t[1]))
        elif kind == "h3link":
            target = map_href(t[2])
            label = esc(t[1])
            out.append('<div class="city-block"><h3>%s</h3>'
                       % ('<a href="%s">%s</a>' % (target, label) if target else label))
        elif kind == "h3":
            out.append('<div class="city-block"><h3>%s</h3>' % esc(t[1]))
        elif kind == "h4":
            out.append("<h4>%s</h4>" % esc(t[1]))
        elif kind == "meta":
            out.append('<p style="font-size:.86rem;color:var(--muted);margin:.2rem 0 0">%s</p>'
                       % esc(t[1]))
        elif kind == "links":
            first = t[1][0][1]
            if first.startswith("/locations/") and first.count("/") > 3:
                out.append(_chips(t[1]))
            else:
                out.append(_linkchips(t[1]))
    if pending_p:
        out.append("".join("<p>%s</p>" % inline(p) for p in pending_p))
    html = "".join(out)
    # close any opened .city-block wrappers
    html += "</div>" * html.count('<div class="city-block">')
    return html


def _is_office_list(blocks):
    """True when every block looks like an office address card (street, city/zip, phone)."""
    if len(blocks) < 3:
        return False
    for b in blocks:
        if len(b["p"]) < 3:
            return False
        if not re.search(r"\b[A-Z]{2}\s+\d{5}\b", b["p"][1]):
            return False
        if "tel:" not in b["p"][-1]:
            return False
    return True


def r_generic(sec, toks):
    lead = []
    blocks = []
    incs = []
    excs = []
    cards_html = []
    links_html = []
    cur = None
    for t in toks:
        kind = t[0]
        val = t[1] if len(t) > 1 else None
        if kind == "h3":
            cur = {"t": val, "p": []}
            blocks.append(cur)
        elif kind == "h3link":
            target = map_href(t[2])
            label = esc(t[1])
            cur = {"t": ('<a href="%s">%s</a>' % (target, label)) if target else label, "p": [],
                   "raw": True}
            blocks.append(cur)
        elif kind == "p":
            (cur["p"] if cur else lead).append(val)
        elif kind == "inc":
            incs.append(val)
        elif kind == "exc":
            excs.append(val)
        elif kind == "arr":
            incs.append(val)
        elif kind == "cards":
            cards_html.append(_cards(val))
        elif kind == "extralinks":
            links_html.append(_extralinks(val))
        elif kind == "links":
            if cur is not None and all(h.startswith(("tel:", "mailto:", "sms:"))
                                       for _l, h in val):
                cur["p"].append(" ".join("[%s](%s)" % (l, h) for l, h in val))
            else:
                links_html.append(_linkchips(val))
        elif kind == "note":
            lead.append(val)

    intro = "".join("<p>%s</p>" % inline(p) for p in lead)
    out = [_head(sec["eyebrow"], sec["title"], "")]
    if intro:
        out.append('<div class="prose prose--wide">%s</div>' % intro)
    if incs:
        out.append('<div style="margin-top:1.8rem">%s</div>' % _checklist(incs))
    if excs:
        out.append('<div style="margin-top:1.4rem"><h4>Not included in this service</h4>%s</div>'
                   % _checklist(excs, excl=True))
    out.extend(cards_html)
    if blocks:
        if all(re.match(r"^\d+\+?$", str(b["t"])) for b in blocks) and len(blocks) >= 2:
            out.append('<div class="stat-row" style="margin-top:2.4rem">%s</div>' % "".join(
                '<div class="stat"><b>%s</b><span>%s</span>%s</div>'
                % (esc(b["t"]), inline(b["p"][0]) if b["p"] else "",
                   "<small>%s</small>" % inline(" ".join(b["p"][1:])) if len(b["p"]) > 1 else "")
                for b in blocks))
        elif _is_office_list(blocks):
            out.append('<div class="offices" style="margin-top:2.4rem">%s</div>' % "".join(
                '<div class="office"><h3>%s</h3><address>%s</address></div>'
                % (esc(b["t"]), "<br>".join(inline(p) for p in b["p"]))
                for b in blocks))
        elif len(blocks) >= 2:
            out.append('<div class="features" style="margin-top:2rem">%s</div>' % "".join(
                '<div class="feature"><span class="feature__ico" aria-hidden="true">%02d</span>'
                '<div><h3>%s</h3>%s</div></div>'
                % (n + 1, b["t"] if b.get("raw") else esc(b["t"]),
                   "".join("<p>%s</p>" % inline(p) for p in b["p"]))
                for n, b in enumerate(blocks)))
        else:
            b = blocks[0]
            out.append('<div class="prose prose--wide" style="margin-top:1.5rem"><h3>%s</h3>%s</div>'
                       % (b["t"] if b.get("raw") else esc(b["t"]),
                          "".join("<p>%s</p>" % inline(p) for p in b["p"])))
    out.extend(links_html)
    return "".join(out)


AREA_HINTS = ("available in", "service areas", "browse by city", "in your city",
              "find services in your city", "where we serve")


def render_sections(parsed):
    """Return (html, final_cta_html)."""
    out = []
    final_cta = None
    band = 0
    sections = parsed["sections"]
    for n, sec in enumerate(sections):
        title = sec["title"]
        tl = title.lower()
        if tl.startswith("guides for your next clean"):
            continue
        toks = tokenize(sec["lines"])

        last = n == len(sections) - 1
        if last and (tl.startswith("ready") or tl.startswith("get a") or
                     tl.startswith("let's") or "ready to" in tl):
            body = " ".join(t[1] for t in toks if t[0] == "p")
            final_cta = cta_band(inline(title), inline(body) if body else "")
            continue

        if tl == "full cleaning checklist":
            html, rest = r_rooms(sec, toks)
            # an "Available Add-Ons" h3 block often trails the checklist
            if rest:
                add_toks = rest[1:] if rest[0][0] == "h3" else rest
                if any(t[0] == "addon" for t in add_toks):
                    add_title = rest[0][1] if rest[0][0] == "h3" else "Available Add-Ons"
                    html += ('<div style="margin-top:3rem">%s</div>'
                             % r_addons(add_title, add_toks, level=3))
        elif tl.startswith("available add-ons"):
            html = r_addons(title, toks)
        elif tl.startswith("who it"):
            html = r_who(sec, toks)
        elif tl == "how it works":
            html = r_steps(sec, toks)
        elif "frequently asked questions" in tl or tl.endswith("faq"):
            html = r_faq(sec, toks)
        elif tl.startswith("what would you like help with"):
            html = r_picker(sec, toks)
        elif any(h in tl for h in AREA_HINTS) or \
                (sec["eyebrow"] or "").strip().lower() in ("service areas", "where we serve"):
            html = r_areas(sec, toks)
        else:
            html = r_generic(sec, toks)

        band_cls = BAND_CYCLE[band % len(BAND_CYCLE)]
        band += 1
        out.append('<section class="band%s"><div class="wrap" data-reveal>%s</div></section>'
                   % (band_cls, html))

    return "".join(out), final_cta


def render_intro(parsed):
    if not parsed["intro"]:
        return ""
    toks = tokenize(parsed["intro"])
    paras = [t[1] for t in toks if t[0] == "p"]
    links = [t[1] for t in toks if t[0] == "links"]
    cards = [t[1] for t in toks if t[0] == "cards"]
    html = []
    if paras:
        first = '<p class="lede">%s</p>' % inline(paras[0])
        rest = "".join("<p>%s</p>" % inline(p) for p in paras[1:])
        html.append('<div class="prose">%s%s</div>' % (first, rest))
    for c in cards:
        html.append(_cards(c))
    for l in links:
        html.append(_extralinks(l))
    if not html:
        return ""
    return ('<section class="band band--tight"><div class="wrap" data-reveal>%s</div></section>'
            % "".join(html))
