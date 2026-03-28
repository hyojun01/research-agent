#!/usr/bin/env python3
"""
Extract, deduplicate, and format all sources from research note files.
Usage: python3 extract_sources.py <sources_directory> [output_file]
"""

import sys
import os
import re
import json
from pathlib import Path
from urllib.parse import urlparse


def extract_sources_from_file(filepath: str) -> list[dict]:
    """Extract source entries from a single research note markdown file."""
    sources = []
    content = Path(filepath).read_text(encoding="utf-8")

    # Pattern: captures URL, title-like text nearby, and date patterns
    url_pattern = re.compile(
        r'(?:Source:\s*(.+?)\s*—\s*)?(https?://[^\s\)]+)(?:\s*—\s*(\d{4}[-/]\d{2}[-/]\d{2}|\w+\s+\d{4}))?',
        re.MULTILINE
    )

    for match in url_pattern.finditer(content):
        name = match.group(1) or ""
        url = match.group(2).rstrip(".,;)")
        date = match.group(3) or ""
        domain = urlparse(url).netloc.replace("www.", "")

        sources.append({
            "name": name.strip(),
            "url": url.strip(),
            "date": date.strip(),
            "domain": domain,
            "file": os.path.basename(filepath)
        })

    return sources


def deduplicate(sources: list[dict]) -> list[dict]:
    """Remove duplicate sources by URL."""
    seen_urls = set()
    unique = []
    for s in sources:
        normalized = s["url"].rstrip("/").lower()
        if normalized not in seen_urls:
            seen_urls.add(normalized)
            unique.append(s)
    return unique


def format_bibliography(sources: list[dict]) -> str:
    """Format sources as a numbered bibliography."""
    lines = ["# Source Bibliography", "", f"**Total unique sources:** {len(sources)}", ""]
    for i, s in enumerate(sources, 1):
        entry = f'{i}. '
        if s["name"]:
            entry += f'{s["name"]}. '
        if s["date"]:
            entry += f'({s["date"]}). '
        entry += s["url"]
        entry += f'  \n   Domain: {s["domain"]} | Found in: {s["file"]}'
        lines.append(entry)
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_sources.py <sources_directory> [output_file]")
        sys.exit(1)

    sources_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    all_sources = []
    for f in sorted(Path(sources_dir).glob("*.md")):
        all_sources.extend(extract_sources_from_file(str(f)))

    unique_sources = deduplicate(all_sources)
    bibliography = format_bibliography(unique_sources)

    if output_file:
        Path(output_file).write_text(bibliography, encoding="utf-8")
        print(f"Extracted {len(unique_sources)} unique sources → {output_file}")
    else:
        print(bibliography)

    # Also output as JSON for programmatic use
    json_output = output_file.replace(".md", ".json") if output_file else None
    if json_output:
        Path(json_output).write_text(
            json.dumps(unique_sources, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )


if __name__ == "__main__":
    main()
