#!/usr/bin/env python3
"""Validate the actual public artifact before deployment (standard library only)."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

EXPECTED_CSP = {
    "default-src": {"'self'"},
    "script-src": {"'self'"},
    "style-src": {"'self'"},
    "img-src": {"'self'"},
    "font-src": {"'self'"},
    "connect-src": {"'none'"},
    "object-src": {"'none'"},
    "frame-src": {"'none'"},
    "base-uri": {"'none'"},
    "form-action": {"'none'"},
}


def restrictive_policy(value):
    directives = {}
    for part in value.split(";"):
        tokens = part.split()
        if not tokens:
            continue
        if tokens[0] in directives:
            return False
        directives[tokens[0]] = set(tokens[1:])
    return directives == EXPECTED_CSP


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.json_blocks = []
        self.json_buffer = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_buffer = ""

    def handle_data(self, data):
        if self.json_buffer is not None:
            self.json_buffer += data

    def handle_endtag(self, tag):
        if tag == "script" and self.json_buffer is not None:
            self.json_blocks.append(self.json_buffer)
            self.json_buffer = None


def validate(root):
    errors = []
    required = [".nojekyll", "index.html", "cv/index.html", "publications/index.html",
                "assets/pdf/Shun_Hsiang_Hsu_Resume.pdf"]
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing public destination: {name}")
    forbidden = {"docs", "tests", "bin", "vendor", "node_modules", ".git", ".claude",
                 ".github", "people", "teaching", "books", "blog", "repositories"}
    private_names = {"Gemfile", "Gemfile.lock", "package.json", "package-lock.json",
                     "requirements.txt", "README.md", "SECURITY.md", "AGENTS.md"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if set(rel.parts) & forbidden or path.name in private_names or path.name.startswith(".env"):
            errors.append(f"Non-public file in artifact: {rel}")
        if path.suffix.lower() != ".html":
            continue
        if rel.as_posix() not in set(required) | {"404.html"}:
            errors.append(f"Unexpected public page: {rel}")
        content = path.read_text()
        if re.search(r"555 your office|123 your address|Write your biography here|A growing collection of your cool projects", content):
            errors.append(f"Template placeholder: {rel}")
        page = Page()
        page.feed(content)
        policies = [a.get("content", "") for t, a in page.tags
                    if t == "meta" and a.get("http-equiv", "").lower() == "content-security-policy"]
        if len(policies) != 1 or not restrictive_policy(policies[0]):
            errors.append(f"Missing restrictive content policy: {rel}")
        for block in page.json_blocks:
            try:
                json.loads(block)
            except json.JSONDecodeError:
                errors.append(f"Invalid JSON-LD: {rel}")
        for tag, attrs in page.tags:
            if any(k.startswith("on") or k == "style" for k in attrs):
                errors.append(f"Inline event/style disallowed by policy: {rel} ({tag})")
            if tag == "script" and not attrs.get("src") and attrs.get("type") != "application/ld+json":
                errors.append(f"Executable inline script: {rel}")
            if tag == "style":
                errors.append(f"Inline stylesheet: {rel}")
            if tag == "img" and "alt" not in attrs:
                errors.append(f"Image without alternative text: {rel}")
            for attr in ["src", "href"]:
                value = attrs.get(attr, "")
                if not value:
                    continue
                url = urlsplit(value)
                is_resource = attr == "src" or (tag == "link" and attrs.get("rel") in {"stylesheet", "preload", "icon"})
                if is_resource and (url.netloc or url.scheme):
                    errors.append(f"Non-local resource: {rel} ({tag})")
                if url.scheme in {"javascript", "http"}:
                    errors.append(f"Unsafe URL scheme: {rel} ({tag})")
                if attrs.get("target") == "_blank" and "noopener" not in attrs.get("rel", ""):
                    errors.append(f"New-tab link without noopener: {rel}")
                if url.scheme or url.netloc:
                    continue
                if not url.path:
                    dest = path
                else:
                    dest = root / unquote(url.path.lstrip("/")) if url.path.startswith("/") else path.parent / unquote(url.path)
                if dest.is_dir():
                    dest = dest / "index.html"
                if not dest.is_file():
                    errors.append(f"Broken local link: {rel} -> {url.path}")
                elif url.fragment and dest.suffix.lower() == ".html":
                    target = Page()
                    target.feed(dest.read_text())
                    anchors = {a.get("id") for _, a in target.tags} | {a.get("name") for t, a in target.tags if t == "a"}
                    if unquote(url.fragment) not in anchors:
                        errors.append(f"Broken local fragment: {rel} -> {value}")
    return sorted(set(errors))


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not root.is_dir():
        raise SystemExit(f"Build directory not found: {root}")
    errors = validate(root)
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(f"FAILED: {len(errors)} public-artifact checks")
    print(f"PASS: public artifact, local links, content policies and JSON-LD ({len(list(root.rglob('*.html')))} HTML pages)")
