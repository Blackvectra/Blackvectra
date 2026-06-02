#!/usr/bin/env python3
"""Validate LinkedIn post files: frontmatter shape and body length.

Pure standard library (no dependencies). Walks posts/, checks each markdown file's
YAML-ish frontmatter and body, and exits non-zero if anything is wrong so it can be
wired into CI later.

Usage:
    python scripts/check.py            # check posts/ relative to repo root
    python scripts/check.py path ...   # check specific files or directories
"""

import sys
from pathlib import Path

REQUIRED_KEYS = {"title", "status", "audience", "tags", "published_date", "permalink"}
VALID_STATUS = {"draft", "published"}
VALID_AUDIENCE = {"PUBLIC", "CONNECTIONS"}
MAX_BODY_CHARS = 3000


def split_frontmatter(text):
    """Return (frontmatter_lines, body) or (None, None) if no frontmatter block."""
    if not text.startswith("---"):
        return None, None
    lines = text.splitlines()
    # First line is the opening '---'; find the closing one.
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, None


def strip_inline_comment(value):
    """Drop a trailing YAML-style comment (whitespace followed by '#').

    Only ' #' (space before hash) starts a comment, so URLs containing '#' such
    as 'https://example.com/a#b' are preserved.
    """
    idx = value.find(" #")
    return value[:idx].strip() if idx != -1 else value


def parse_frontmatter(fm_lines):
    """Minimal `key: value` parser. Values are returned as raw strings."""
    data = {}
    for line in fm_lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = strip_inline_comment(value.strip())
    return data


def check_file(path):
    """Return a list of error strings for a single post file (empty == ok)."""
    errors = []
    text = path.read_text(encoding="utf-8")
    fm_lines, body = split_frontmatter(text)

    if fm_lines is None:
        return [f"{path}: missing or unterminated YAML frontmatter block (--- ... ---)"]

    data = parse_frontmatter(fm_lines)

    missing = REQUIRED_KEYS - set(data)
    if missing:
        errors.append(f"{path}: missing frontmatter keys: {', '.join(sorted(missing))}")

    status = data.get("status", "")
    if status and status not in VALID_STATUS:
        errors.append(f"{path}: invalid status {status!r} (expected one of {sorted(VALID_STATUS)})")

    audience = data.get("audience", "")
    if audience and audience not in VALID_AUDIENCE:
        errors.append(f"{path}: invalid audience {audience!r} (expected one of {sorted(VALID_AUDIENCE)})")

    # A published post should record when and where it went out.
    if status == "published":
        for key in ("published_date", "permalink"):
            if not data.get(key):
                errors.append(f"{path}: status is 'published' but '{key}' is empty")

    body_len = len((body or "").strip())
    if body_len == 0:
        errors.append(f"{path}: post body is empty")
    elif body_len > MAX_BODY_CHARS:
        errors.append(f"{path}: body is {body_len} chars (LinkedIn limit is {MAX_BODY_CHARS})")

    return errors


def gather_files(targets):
    files = []
    for target in targets:
        p = Path(target)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.suffix == ".md":
            files.append(p)
    return files


def main(argv):
    if argv:
        targets = argv
    else:
        # Default to posts/ relative to this script's repo root.
        repo_root = Path(__file__).resolve().parent.parent
        targets = [repo_root / "posts"]

    files = gather_files(targets)
    if not files:
        print("No post files (*.md) found.")
        return 0

    all_errors = []
    for f in files:
        all_errors.extend(check_file(f))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        print(f"\n{len(all_errors)} problem(s) in {len(files)} file(s).")
        return 1

    print(f"OK: {len(files)} file(s) checked, no problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
