#!/usr/bin/env python3
"""
Wiki → ARS Passport Adapter

Scans the wiki/ directory, parses YAML frontmatter from every .md file,
classifies pages by type, and produces:
  - passports/<prefix>-<timestamp>.passport.yaml
  - passports/<prefix>-<timestamp>.rejection_log.yaml

Page types: book, concept, entity, topic_guide, policy, case_study, source, meta, analysis_artifact

Usage:
  python scripts/adapters/wiki.py [--prefix wiki-corpus] [--output-dir ./passports]
"""

import os
import sys
import re
import yaml
import argparse
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


def parse_frontmatter(text: str):
    """Parse YAML frontmatter from markdown text. Returns (meta, body)."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}, text
    return meta, parts[2].strip()


def extract_h1(body: str):
    """Extract first H1 title from markdown body."""
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def extract_authors_from_sources(sources):
    """Try to extract author patterns from sources list."""
    authors = []
    if isinstance(sources, list):
        for s in sources:
            m = re.findall(r'([A-Z][a-z]+(?:\s+[A-Z]\.?)?)\s*[\(\d]', str(s))
            authors.extend(m)
    if not authors:
        return None
    seen = set()
    unique = []
    for a in authors:
        if a not in seen:
            seen.add(a)
            unique.append(a)
    return unique


def classify_page(relpath: str, meta: dict):
    """Return page type based on path and frontmatter."""
    p = relpath.replace("\\", "/")
    if "/books/" in p:
        return "book"
    if "/entities/" in p:
        return "entity"
    if "/topics/" in p:
        return "topic_guide"
    if "/concepts/" in p:
        return "concept"
    if "/policies/" in p:
        return "policy"
    if "/cases/" in p:
        return "case_study"
    if p.startswith("raw/") or "/raw/" in p:
        if "_analysis_" in p:
            return "analysis_artifact"
        return "source"
    # Top-level meta pages (path is relative to wiki/, so no "wiki/" prefix)
    if p in ("index.md", "log.md", "state.md"):
        return "meta"
    # Top-level concepts/entities/topics
    if p.startswith("concepts/"):
        return "concept"
    if p.startswith("entities/"):
        return "entity"
    if p.startswith("topics/"):
        return "topic_guide"
    return "unknown"


def extract_year(meta: dict, body: str):
    """Extract year from frontmatter or body."""
    published = meta.get("published", "")
    if published:
        m = re.search(r"(\d{4})", str(published))
        if m:
            return int(m.group(1))
    created = meta.get("created", "")
    if created:
        m = re.search(r"(\d{4})", str(created))
        if m:
            return int(m.group(1))
    return None


def validate_page(meta: dict, body: str, pagetype: str):
    """Return list of missing/warning fields."""
    issues = []

    # Skip validation for analysis artifacts and meta pages
    if pagetype in ("meta", "analysis_artifact"):
        return issues

    # Title check (from H1 or frontmatter)
    title = meta.get("title") or extract_h1(body)
    if not title:
        issues.append("missing_title")

    # Tags: required for knowledge pages, optional for raw sources
    if pagetype not in ("meta", "source", "analysis_artifact") and not meta.get("tags"):
        issues.append("missing_tags")

    # Status: required for knowledge pages, optional for sources
    if pagetype not in ("meta", "source", "analysis_artifact") and not meta.get("status"):
        issues.append("missing_status")

    # Sources: required for concept/topic/book pages
    if pagetype in ("concept", "topic_guide", "book") and not meta.get("sources"):
        issues.append("missing_sources")

    return issues


def scan_wiki(wiki_root: str):
    """Walk wiki/ directory, parse all .md files, return corpus entries + rejections."""
    accepted = []
    rejected = []
    page_counts = defaultdict(int)

    for root, dirs, files in os.walk(wiki_root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for fname in files:
            if not fname.endswith(".md"):
                continue

            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, wiki_root)

            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception as e:
                rejected.append({"path": relpath, "reason": f"read_error: {e}"})
                continue

            meta, body = parse_frontmatter(text)
            pagetype = classify_page(relpath, meta)
            page_counts[pagetype] += 1

            # Skip meta and analysis artifacts
            if pagetype in ("meta", "analysis_artifact"):
                continue

            # Validate
            issues = validate_page(meta, body, pagetype)
            if issues:
                rejected.append({
                    "path": relpath,
                    "type": pagetype,
                    "issues": issues,
                    "frontmatter_keys": list(meta.keys()) if meta else []
                })
                continue

            # Build corpus entry — use relative path (sans .md) as unique citekey
            citekey = relpath.replace("\\", "/").replace(".md", "")
            title = meta.get("title") or extract_h1(body) or fname.replace(".md", "")
            tags = meta.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]

            entry = {
                "citation_key": citekey,
                "title": title,
                "type": pagetype,
                "path": relpath,
                "tags": tags,
                "status": meta.get("status", "unknown"),
                "updated": str(meta.get("updated", meta.get("created", ""))),
            }

            year = extract_year(meta, body)
            if year:
                entry["year"] = year

            sources = meta.get("sources", [])
            if sources:
                entry["sources"] = sources if isinstance(sources, list) else [sources]
                authors = extract_authors_from_sources(sources)
                if authors:
                    entry["authors"] = authors

            if meta.get("description"):
                entry["description"] = meta["description"]

            accepted.append(entry)

    return accepted, rejected, dict(page_counts)


def write_passport(accepted, rejected, page_counts, output_dir, prefix):
    """Write passport.yaml and rejection_log.yaml."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    os.makedirs(output_dir, exist_ok=True)

    passport = {
        "passport": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "source": "wiki-adapter v1.0",
            "total_scanned": len(accepted) + len(rejected),
            "accepted": len(accepted),
            "rejected": len(rejected),
            "page_counts": page_counts,
        },
        "corpus": accepted,
    }

    rejection_log = {
        "rejection_log": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "total_rejected": len(rejected),
        },
        "rejected": rejected,
    }

    passport_path = os.path.join(output_dir, f"{prefix}-{timestamp}.passport.yaml")
    rejection_path = os.path.join(output_dir, f"{prefix}-{timestamp}.rejection_log.yaml")

    with open(passport_path, "w", encoding="utf-8") as f:
        yaml.dump(passport, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    with open(rejection_path, "w", encoding="utf-8") as f:
        yaml.dump(rejection_log, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return passport_path, rejection_path


def main():
    parser = argparse.ArgumentParser(description="Wiki → ARS Passport Adapter")
    parser.add_argument("--wiki-root", default=None, help="Path to wiki/ directory")
    parser.add_argument("--output-dir", default="./passports", help="Output directory")
    parser.add_argument("--prefix", default="wiki-corpus", help="Passport filename prefix")
    parser.add_argument("--dry-run", action="store_true", help="Print stats without writing files")
    args = parser.parse_args()

    if args.wiki_root:
        wiki_root = args.wiki_root
    else:
        script_dir = Path(__file__).resolve().parent
        repo_root = script_dir.parent.parent
        wiki_root = repo_root / "wiki"

    wiki_root = str(wiki_root)
    if not os.path.isdir(wiki_root):
        print(f"ERROR: wiki directory not found: {wiki_root}")
        sys.exit(1)

    print(f"Scanning: {wiki_root}")
    accepted, rejected, page_counts = scan_wiki(wiki_root)

    print(f"\n--- Scan Results ---")
    print(f"Accepted: {len(accepted)}")
    print(f"Rejected: {len(rejected)}")
    print(f"\nPage counts by type:")
    for t, c in sorted(page_counts.items()):
        print(f"  {t}: {c}")

    if rejected:
        print(f"\nRejection reasons:")
        reason_counts = defaultdict(int)
        for r in rejected:
            for issue in r.get("issues", ["unknown"]):
                reason_counts[issue] += 1
        for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
            print(f"  {reason}: {count}")

    if args.dry_run:
        print("\n[Dry run - no files written]")
        return

    passport_path, rejection_path = write_passport(
        accepted, rejected, page_counts, args.output_dir, args.prefix
    )
    print(f"\nPassport: {passport_path}")
    print(f"Rejection log: {rejection_path}")


if __name__ == "__main__":
    main()
