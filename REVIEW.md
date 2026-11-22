# EdgeTX Website 3.0 review preview

This branch keeps MkDocs and Material for MkDocs. It adds a custom homepage template while retaining the existing Markdown pages. There is no frontend framework migration.

## Run locally

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

## Review URL

https://jimb40.github.io/edgetx.github.io/

GitHub Pages deploys the `website-3.0` branch through `.github/workflows/ci.yml`. The workflow runs only in `JimB40/edgetx.github.io`. The official website is unaffected.

## Search indexing

Every generated page includes `noindex, nofollow, noarchive`; robots.txt requests no crawling. The CI check verifies these directives. The site is still public and is not access-controlled.

## Review scope

- Redesigned homepage, navigation, light/dark themes, galleries, community, Fest, support and manufacturers.
- Existing Markdown pages share the homepage header, footer, design tokens and light/dark theme. MkDocs still provides sidebar navigation, table of contents and search. The Docs and Help directory links to every existing content page.
- Donation links open the existing Open Collective page. The planned shop button is disabled.
- The Fest 2027 destination and example countdown are concept content, not a confirmed event date.
- The radio count is concept copy based on the current compatibility list; a shared catalog remains future work.
- Subpath-safe assets and homepage links support the fork's GitHub Pages address.

## Source files

- overrides/home.html: homepage template
- docs/assets/website-3.0/homepage.css: approved visual direction
- docs/assets/website-3.0/homepage.js: local interactions
- docs/*.md: existing content
- overrides/main.html: preview announcement and noindex on documentation pages

Team review can be collected as GitHub issues and on the upstream draft pull request. Do not merge the fork-specific preview deployment configuration into production unchanged.

## Current review scope

Desktop layout and content approval only. Custom mobile/tablet breakpoints and width-based menu collapsing have been removed. Responsive layouts will be designed after the desktop version and content are approved.
