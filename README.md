# Salt &amp; Slate Cleaning Company — website

A completely rebuilt, static marketing site for Salt & Slate Cleaning Company —
premium residential and commercial cleaning across Utah, Arizona, Nevada and Texas.

## Stack

Vanilla HTML, CSS and JavaScript. No build step is required to serve the site:
`index.html` is the entry point and every page is a pre-rendered `index.html`
under its own directory.

```
index.html                     home
services/                      residential overview + 9 service pages
commercial/                    commercial overview + 8 industry pages
locations/                     service areas + 4 state pages
about/                         about, offices, stats
assets/css/site.css            design system
assets/js/site.js              nav, hero slideshow, before/after sliders, forms
images/source/                 photography from the business
favicon.svg, robots.txt, sitemap.xml
tools/                         the Python generator used to produce the HTML
```

## Regenerating the HTML

The pages are generated from the business content by a small, dependency-free
Python script:

```
python3 tools/build.py
```

`tools/data.py` holds the business facts (phone numbers, offices, services,
reviews, image mappings), `tools/layout.py` the shared shell (header, footer,
hero, quote form), and `tools/parse.py` + `tools/render.py` turn the page
content into the design's section components.

## Forms

Every form posts to LeadrVision at
`https://vision.leadrai.com/api/forms/a152d8cf19bb1a85f595f17580def3b9`.
Submissions work with JavaScript disabled (plain `POST`, visitor returns with
`?submitted=1`) and with JavaScript enabled (`fetch` to the same URL, inline
confirmation).

## Contact

(385) 333-7737 · hello@saltandslatecleaning.com
