#!/usr/bin/env python3
"""
Suggest potential glossary terms from curriculum markdown content.

This script is intentionally advisory: it prints suggestions and exits 0.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_ROOT = REPO_ROOT / "content"
GLOSSARY_PATH = REPO_ROOT / "content" / "ops" / "basic" / "glossary.md"

# Common all-caps tokens that are usually not glossary-worthy in this repo context.
STOPWORDS = {
    "AI",
    "API",
    "CLI",
    "JSON",
    "HTML",
    "HTTP",
    "CSS",
    "JS",
    "URL",
    "MD",
    "LCLS",
    "OPS",
    "S3DF",
}

# Tokens commonly used as shell commands, paths, or implementation specifics.
NOISY_TOKENS = {
    "grep",
    "rg",
    "cat",
    "head",
    "tail",
    "ls",
    "cd",
    "bash",
    "python",
    "python3",
    "git",
    "gh",
    "chmod",
    "mkdir",
    "curl",
    "wget",
    "squeue",
    "sinfo",
    "slurmdbd",
    "docs-index",
    "path",
    "select",
}


def normalize(term: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", term.lower())


def glossary_terms(path: Path) -> set[str]:
    if not path.exists():
        return set()

    terms: set[str] = set()
    heading_re = re.compile(r"^##\s+(.+?)\s*$")
    paren_re = re.compile(r"\(([^)]+)\)")
    for line in path.read_text(encoding="utf-8").splitlines():
        m = heading_re.match(line.strip())
        if not m:
            continue
        title = m.group(1).strip()
        # Ignore editorial sections if ever reintroduced.
        if title.lower().startswith("editorial"):
            continue
        terms.add(normalize(title))
        for alias in paren_re.findall(title):
            terms.add(normalize(alias))
    return terms


def curriculum_files(root: Path) -> list[Path]:
    files = sorted(root.glob("**/*.md"))
    return [p for p in files if p != GLOSSARY_PATH]


def extract_candidates(text: str) -> list[str]:
    candidates: list[str] = []

    # Backticked tokens often denote explicit concepts.
    for token in re.findall(r"`([A-Za-z][A-Za-z0-9_\-/]{1,40})`", text):
        candidates.append(token)

    # Acronyms and protocol-like tokens.
    for token in re.findall(r"\b[A-Z][A-Z0-9]{1,}\b", text):
        if token in STOPWORDS:
            continue
        candidates.append(token)

    return candidates


def is_noisy_candidate(token: str) -> bool:
    low = token.lower()
    norm = normalize(token)

    if low in NOISY_TOKENS or norm in {normalize(t) for t in NOISY_TOKENS}:
        return True

    # Path-like or command flag-ish tokens.
    if "/" in token or token.startswith("-"):
        return True

    # Mostly numeric or too short to be meaningful as glossary term.
    if len(norm) < 3 or norm.isdigit():
        return True

    return False


def main() -> int:
    known = glossary_terms(GLOSSARY_PATH)
    counter: Counter[str] = Counter()
    pretty: dict[str, str] = {}

    for md in curriculum_files(CURRICULUM_ROOT):
        text = md.read_text(encoding="utf-8")
        for token in extract_candidates(text):
            norm = normalize(token)
            if not norm or norm in known or is_noisy_candidate(token):
                continue
            counter[norm] += 1
            pretty.setdefault(norm, token)

    suggestions = []
    for n, c in counter.items():
        token = pretty[n]
        # Higher bar for short acronyms to reduce false positives.
        min_count = 3 if token.isupper() and len(token) <= 4 else 2
        if c >= min_count:
            suggestions.append((token, c))
    suggestions.sort(key=lambda x: (-x[1], x[0].lower()))

    if not suggestions:
        print("Glossary check: no new high-signal term suggestions.")
        return 0

    print("Glossary check: candidate terms to consider adding:")
    for term, count in suggestions[:15]:
        print(f"  - {term} (seen {count} times)")
    print("Note: advisory only; commit is not blocked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
