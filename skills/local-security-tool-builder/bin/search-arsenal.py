#!/usr/bin/env python3
"""Search the Sectinel security-skill arsenal by keyword.

Scans SKILL.md frontmatter (name, description, tags, subdomain) across the
vendored arsenal and prints matching skills with their paths.

Usage:
    search-arsenal.py <keyword> [keyword ...] [--root ~/workspace/sectinel] [--limit 20]
"""
import os
import re
import sys

DEFAULT_ROOT = os.path.expanduser("~/workspace/sectinel")


def parse_frontmatter(path):
    """Lightweight frontmatter parse: name, description, subdomain, tags."""
    data = {"name": "", "description": "", "subdomain": "", "tags": []}
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return data
    if not lines or lines[0].strip() != "---":
        return data
    in_tags = False
    desc_cont = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if in_tags:
            m = re.match(r"\s*-\s*(.+)", line)
            if m:
                data["tags"].append(m.group(1).strip())
                continue
            in_tags = False
        if desc_cont:
            if re.match(r"\s+\S", line):
                data["description"] += " " + line.strip()
                continue
            desc_cont = False
        m = re.match(r"^(name|description|subdomain):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip("'\"")
            if key == "description" and not val:
                desc_cont = True
            data[key] = val
        elif re.match(r"^tags:\s*$", line):
            in_tags = True
    return data


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = DEFAULT_ROOT
    limit = 20
    for i, a in enumerate(sys.argv[1:]):
        if a == "--root" and i + 1 < len(sys.argv[1:]):
            root = os.path.expanduser(sys.argv[1:][i + 1])
        if a == "--limit" and i + 1 < len(sys.argv[1:]):
            limit = int(sys.argv[1:][i + 1])
    if not args:
        print(__doc__)
        return 1
    keywords = [k.lower() for k in args]
    hits = []
    for dirpath, _, filenames in os.walk(root):
        if "SKILL.md" not in filenames:
            continue
        path = os.path.join(dirpath, "SKILL.md")
        fm = parse_frontmatter(path)
        name_h = fm["name"].lower()
        tag_h = " ".join([fm["subdomain"]] + fm["tags"]).lower()
        desc_h = fm["description"].lower()
        score = (3 * sum(1 for k in keywords if k in name_h)
                 + 2 * sum(1 for k in keywords if k in tag_h)
                 + sum(1 for k in keywords if k in desc_h))
        if score:
            hits.append((score, fm["name"], fm["description"][:120], path))
    hits.sort(key=lambda h: (-h[0], h[1]))
    for score, name, desc, path in hits[:limit]:
        rel = os.path.relpath(path, root)
        print(f"- {name}  [{rel}]\n  {desc}\n")
    print(f"{len(hits)} match(es), showing {min(limit, len(hits))}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
