# Agentic AI Curriculum Website (LCLS)

This folder contains a small static website to host the curriculum for:

**Agentic AI for Science and Operations at LCLS**

## Preview locally

From this directory:

```bash
python3 -m http.server 8000
```

Then open:

`http://localhost:8000`

The website loads markdown content from `content/ops/*.md`.

## Enable repository hooks

This repository includes a pre-commit hook at `.githooks/pre-commit` that suggests potential new glossary terms from curriculum content.

Enable it once per clone:

```bash
git config core.hooksPath .githooks
```

## Adding more curriculum pages

To add more Ops sections, create markdown files under `content/ops/` and update the mapping in `index.html`:

`CATEGORY_TO_MD`.

