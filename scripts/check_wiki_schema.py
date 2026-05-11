#!/usr/bin/env python3
"""
Wiki Schema Validator — Check passport.yaml against expected schema.

Usage:
  python scripts/check_wiki_schema.py <passport.yaml>

Exit code 0 = valid, 1 = validation errors found.
"""

import sys
import yaml
import os
from pathlib import Path


EXPECTED_SCHEMA = {
    "passport": {
        "generated": str,
        "source": str,
        "total_scanned": int,
        "accepted": int,
        "rejected": int,
        "page_counts": dict,
    },
    "corpus": list,
}

CORPUS_ENTRY_REQUIRED = ["citation_key", "title", "type", "path"]
CORPUS_ENTRY_OPTIONAL = ["tags", "status", "updated", "year", "sources", "authors", "description"]


def validate_passport(data: dict) -> list:
    """Validate passport structure. Returns list of error messages."""
    errors = []

    # Top-level keys
    if "passport" not in data:
        errors.append("Missing top-level 'passport' key")
    if "corpus" not in data:
        errors.append("Missing top-level 'corpus' key")
        return errors  # cannot continue

    # Passport metadata
    pp = data["passport"]
    for key, expected_type in EXPECTED_SCHEMA["passport"].items():
        if key not in pp:
            errors.append(f"passport.{key}: missing")
        elif not isinstance(pp[key], expected_type):
            errors.append(f"passport.{key}: expected {expected_type.__name__}, got {type(pp[key]).__name__}")

    # Validate consistency
    if "total_scanned" in pp and "accepted" in pp and "rejected" in pp:
        if pp["total_scanned"] != pp["accepted"] + pp["rejected"]:
            errors.append(
                f"passport.total_scanned ({pp['total_scanned']}) != "
                f"accepted ({pp['accepted']}) + rejected ({pp['rejected']})"
            )

    # Corpus entries
    corpus = data["corpus"]
    if not isinstance(corpus, list):
        errors.append(f"corpus: expected list, got {type(corpus).__name__}")
        return errors

    citekeys = set()
    for i, entry in enumerate(corpus):
        prefix = f"corpus[{i}]"
        for key in CORPUS_ENTRY_REQUIRED:
            if key not in entry:
                errors.append(f"{prefix}.{key}: missing required field")

        # Check citekey uniqueness
        ck = entry.get("citation_key", "")
        if ck in citekeys:
            errors.append(f"{prefix}.citation_key: duplicate '{ck}'")
        citekeys.add(ck)

        # Type check tags
        if "tags" in entry and not isinstance(entry["tags"], list):
            errors.append(f"{prefix}.tags: expected list, got {type(entry['tags']).__name__}")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/check_wiki_schema.py <passport.yaml>")
        sys.exit(1)

    passport_path = sys.argv[1]
    if not os.path.exists(passport_path):
        print(f"ERROR: file not found: {passport_path}")
        sys.exit(1)

    with open(passport_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    errors = validate_passport(data)

    if errors:
        print(f"VALIDATION FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"VALID: {passport_path}")
        print(f"  Pages: {data['passport']['accepted']} accepted, {data['passport']['rejected']} rejected")
        print(f"  Types: {data['passport']['page_counts']}")


if __name__ == "__main__":
    main()
