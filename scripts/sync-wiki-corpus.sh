#!/bin/bash
# sync-wiki-corpus.sh — Generate ARS passport from Wiki knowledge base
#
# Usage:
#   ./scripts/sync-wiki-corpus.sh                         # auto-detect wiki path
#   ./scripts/sync-wiki-corpus.sh --dry-run               # preview only
#   ./scripts/sync-wiki-corpus.sh --prefix my-project     # custom prefix
#
# Requires: python3, pyyaml

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ADAPTER="$SCRIPT_DIR/adapters/wiki.py"
OUTPUT_DIR="$REPO_ROOT/passports"

# Defaults
PREFIX="wiki-corpus"
DRY_RUN=""

# Parse args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --prefix) PREFIX="$2"; shift 2 ;;
        --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
        --dry-run) DRY_RUN="--dry-run" ; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

echo "=== Wiki Corpus Sync ==="
echo "Adapter: $ADAPTER"
echo "Output:  $OUTPUT_DIR"
echo "Prefix:  $PREFIX"
echo ""

python3 "$ADAPTER" \
    --wiki-root "$REPO_ROOT/wiki" \
    --output-dir "$OUTPUT_DIR" \
    --prefix "$PREFIX" \
    $DRY_RUN

echo ""
echo "Sync complete. Check $OUTPUT_DIR/ for output files."
