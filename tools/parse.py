# -*- coding: utf-8 -*-
"""Parse the scraped source pages into structured blocks."""

import re
from data import RESIDENTIAL, COMMERCIAL, STATES

EXISTING = set(["/", "/services/", "/commercial/", "/locations/", "/about/"])
for _s, _l, _t in RESIDENTIAL:
    EXISTING.add("/services/%s/" % _s)
for _s, _l, _d in COMMERCIAL[:8]:
    EXISTING.add("/commercial/%s/" % _s)
for _s, _l, _d in STATES:
    EXISTING.add("/locations/%s/" % _s)

STATE_SLUGS = set(s for s, _l, _d in STATES)
SERVICE_SLUGS = set(s for s, _l, _t in RESIDENTIAL)
COMM_SLUGS = set(s for s, _l, _d in COMMERCIAL[:8])

LINK_RE = re.compile(r"\[\s*(.*?)\s*\]\(([^)]*)\)")
CARD_RE = re.compile(r"#{3,4}\s*\[\s*(.*?)\s*\]\(([^)]*)\)")
TRAIL_CTA = re.compile(
    r"\s*(?:Learn More|Read guide|View all [^→]*|All \d+ (?:Services|Industries)"
    r"|All [A-Za-z ]+)\s*(?:→)?\s*$")


def map_href(href):
    """Return a valid internal href for this site, or None if the target does not exist."""
    if not href:
        return None
    href = href.strip()
    if href.startswith("#"):
        return href
    if href.startswith("mailto:") or href.startswith("tel:") or href.startswith("sms:"):
        return href
    if href.startswith("http"):
        return None
    if href.startswith("/cdn-cgi/l/email-protection"):
        return "mailto:hello@saltandslatecleaning.com"
    href = href.split("#")[0]
    if not href.endswith("/"):
        href += "/"
    if href in ("/book/", "/contact/"):
        return "#quote"
    if href in EXISTING:
        return href
    parts = [p for p in href.split("/") if p]
    if parts and parts[0] == "locations" and len(parts) >= 2 and parts[1] in STATE_SLUGS:
        if len(parts) == 3 and parts[2] in SERVICE_SLUGS:
            return "/services/%s/" % parts[2]
        if len(parts) == 3 and parts[2] in COMM_SLUGS:
            return "/commercial/%s/" % parts[2]
        return "/locations/%s/" % parts[1]
    if parts and parts[0] == "services" and len(parts) >= 2 and parts[1] in SERVICE_SLUGS:
        return "/services/%s/" % parts[1]
    if parts and parts[0] == "commercial" and len(parts) >= 2 and parts[1] in COMM_SLUGS:
        return "/commercial/%s/" % parts[1]
    return None


def inline(text):
    """Convert inline markdown links; drop links whose target does not exist."""
    def rep(m):
        label, href = m.group(1), m.group(2)
        if label.startswith("[email") or "email-protection" in href:
            return '<a href="mailto:hello@saltandslatecleaning.com">hello@saltandslatecleaning.com</a>'
        target = map_href(href)
        if target:
            return '<a href="%s">%s</a>' % (target, label)
        return label
    text = LINK_RE.sub(rep, text)
    text = text.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
    text = re.sub(r"&amp;(#?\w+;)", r"&\1", text)
    text = text.replace("<a href=", "\x00").replace("</a>", "\x01")
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("\x00", "<a href=").replace("\x01", "</a>")
    text = re.sub(r'<a href="([^"]*)"&gt;', r'<a href="\1">', text)
    return text.strip()


def esc(text):
    text = text.replace("&", "&amp;")
    text = re.sub(r"&amp;(#?\w+;)", r"&\1", text)
    return text.replace("<", "&lt;").replace(">", "&gt;").strip()


KNOWN_TITLES = []
for _s, _l, _t in RESIDENTIAL:
    KNOWN_TITLES.append(_l.replace("&amp;", "&"))
for _s, _l, _d in COMMERCIAL:
    KNOWN_TITLES.append(_l.replace("&amp;", "&"))
_base = list(KNOWN_TITLES)
for _t in _base:
    for _s, _n, _d in STATES:
        KNOWN_TITLES.append("%s in %s" % (_t, _n))
for _s, _n, _d in STATES:
    KNOWN_TITLES.append(_n)
KNOWN_TITLES.sort(key=len, reverse=True)


def split_card(inner):
    inner = re.sub(r"\s*→\s*$", "", inner.strip())
    prev = None
    while prev != inner:
        prev = inner
        inner = TRAIL_CTA.sub("", inner).strip()
    parts = re.split(r"\s{2,}", inner)
    if len(parts) >= 2:
        return parts[0].strip(), " ".join(p.strip() for p in parts[1:]).strip()
    for known in KNOWN_TITLES:
        if inner.startswith(known):
            rest = inner[len(known):].strip()
            if len(rest) >= 20:
                return known, rest
            break
    return inner, ""


def strip_shell(path):
    """Read a scraped page and return (title, lines) with header/footer removed."""
    raw = open(path, encoding="utf-8").read().split("\n")
    title = raw[1].replace("Title:", "").strip()
    start = None
    end = None
    for i, line in enumerate(raw):
        s = line.strip()
        if start is None and re.match(
                r"^\[ \(\d{3}\) \d{3}-\d{4} \]\(tel:\+1\d+\) \[ Book a Cleaning \]\(/book/\)$", s):
            start = i
        if s == "[ ![Salt & Slate Cleaning](/images/logo_white.png) ](/)":
            end = i
    return title, raw[start + 1:end]


def parse(path):
    """Return dict(title, eyebrow, h1, lede, intro[], sections[])."""
    title, lines = strip_shell(path)
    body = []
    eyebrow = None
    h1 = None
    lede = None
    pre_rating = []

    i = 0
    seen_rating = False
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        i += 1
        if not s:
            continue
        if re.match(r"^\d+\.\s", s) or re.match(r"^\d+\.$", s):
            continue
        if re.match(r"^!\[.*\]\(.*\)$", s):
            continue
        s = re.sub(r"!\[[^\]]*\]\([^)]*\)\s*", "", s).strip()
        if not s:
            continue
        if s.startswith("[5.0 on Google") or s.startswith("[" + "5.0"):
            seen_rating = True
            continue
        if s.startswith("Across all") and "locations" in s:
            continue
        if h1 is None and s.startswith("# "):
            h1 = s[2:].strip()
            continue
        if h1 is None:
            if not seen_rating:
                pre_rating.append(s)
            continue
        if lede is None:
            lede = s
            continue
        # drop hero CTA / anchor-nav rows
        if re.match(r"^(\[[^\]]*\]\([^)]*\)\s*)+$", s) and (
                "/book/" in s or "/contact/" in s or s.startswith("[Explore ")):
            continue
        body.append(s)

    if pre_rating:
        eyebrow = pre_rating[-1]

    # split into sections at "## " headings
    sections = []
    intro = []
    cur = None
    pending_eyebrow = None
    for idx, s in enumerate(body):
        if s.startswith("## "):
            sections.append({"eyebrow": pending_eyebrow, "title": s[3:].strip(), "lines": []})
            cur = sections[-1]
            pending_eyebrow = None
            continue
        nxt = body[idx + 1] if idx + 1 < len(body) else ""
        plain = not s.startswith(("#", "[", "  *", "✓", "*")) and "](" not in s
        if plain and nxt.startswith("## ") and len(s) < 60:
            pending_eyebrow = s
            continue
        if cur is None:
            intro.append(s)
        else:
            cur["lines"].append(s)

    return {"title": title, "eyebrow": eyebrow, "h1": h1, "lede": lede,
            "intro": intro, "sections": sections}


# ---------------------------------------------------------------- tokenizing
def tokenize(lines):
    """Turn a section's raw lines into ordered tokens."""
    toks = []
    i = 0
    n = len(lines)
    while i < n:
        s = lines[i]
        i += 1

        if s.startswith("#### "):
            label = re.sub(r"^#+\s*", "", s)
            m = LINK_RE.match(label)
            if m:
                label = m.group(1)
            toks.append(("h4", label))
            continue
        if s.startswith("### ") and "](" not in s:
            toks.append(("h3", s[4:].strip()))
            continue
        if re.match(r"^#{3,4}\s*\[", s):
            cards = [(m.group(1), m.group(2)) for m in CARD_RE.finditer(s)]
            rest = CARD_RE.sub("", s)
            if len(cards) == 1 and not split_card(cards[0][0])[1]:
                toks.append(("h3link", cards[0][0], cards[0][1]))
            else:
                toks.append(("cards", cards))
            extras = [(m.group(1), m.group(2)) for m in LINK_RE.finditer(rest)]
            if extras:
                toks.append(("extralinks", extras))
            continue
        if re.match(r"^\s*\*\s*✓", s):
            toks.append(("inc", re.sub(r"^\s*\*\s*✓\s*", "", s).strip()))
            continue
        if re.match(r"^\s*\*\s*—", s):
            toks.append(("exc", re.sub(r"^\s*\*\s*—\s*", "", s).strip()))
            continue
        if re.match(r"^\s*\*\s*→", s):
            toks.append(("arr", re.sub(r"^\s*\*\s*→\s*", "", s).strip()))
            continue
        if s.startswith("✓"):
            toks.append(("inc", s[1:].strip()))
            continue
        if re.match(r"^\*{1,2}\s+\S", s):
            toks.append(("note", s))
            continue
        if s == "Included":
            toks.append(("mode", "inc"))
            continue
        if s.startswith("Not included"):
            toks.append(("mode", "exc"))
            continue
        if re.match(r"^\d{2}$", s):
            toks.append(("stepnum", s))
            continue
        if re.match(r"^\d+\s+(county|counties)$", s):
            toks.append(("meta", s))
            continue
        links = [(m.group(1), m.group(2)) for m in LINK_RE.finditer(s)]
        if links and re.match(r"^(\[[^\]]*\]\([^)]*\)\s*)+$", s):
            if len(links) == 1 and "/" in links[0][1] and links[0][1].count("/") >= 3 \
                    and links[0][0].strip() == links[0][0] and "→" not in links[0][0] \
                    and re.search(r"(County|Counties)$", links[0][0]):
                toks.append(("h4", links[0][0]))
            elif any(split_card(lbl)[1] for lbl, _h in links):
                toks.append(("cards", links))
            else:
                toks.append(("links", links))
            continue
        if re.search(r"\$\d", s) and "](" not in s and len(s) < 110:
            m = re.match(r"^(.*?)(\$[\d,]+(?:/[a-z]+)?)$", s.strip())
            if m:
                toks.append(("addon", (m.group(1).strip(), m.group(2).strip())))
                continue
        toks.append(("p", s))
    return toks
