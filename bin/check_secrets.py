#!/usr/bin/env python3
"""Conservative credential-pattern guard; not a full secret scanner or certification."""

import argparse
import re
import subprocess
from pathlib import Path

RULES = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})\b"),
    "aws-access-key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "google-api-key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "slack-token": re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{20,}\b"),
    "service-secret-key": re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b"),
}


def scan_text(text):
    findings = []
    for rule, pattern in RULES.items():
        for match in pattern.finditer(text):
            findings.append((rule, text.count("\n", 0, match.start()) + 1))
    return sorted(set(findings))


def sensitive_path(path):
    name = path.name.lower()
    if name in {".env.example", ".env.sample", ".env.template"}:
        return False
    return name == ".env" or name.startswith(".env.") or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"} or name in {"id_rsa", "id_ed25519"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, help="Scan a generated site instead of Git source files")
    args = parser.parse_args()
    if args.site:
        root = args.site.resolve()
        if not root.is_dir():
            parser.error("Site directory does not exist")
        paths = [p.relative_to(root) for p in root.rglob("*") if p.is_file()]
    else:
        root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
        names = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root)
        paths = [Path(name.decode()) for name in names.split(b"\0") if name]
    findings = 0
    count = 0
    for relative in sorted(set(paths)):
        path = root / relative
        if not path.exists():
            continue
        if path.is_symlink():
            print(f"{relative}: symlink requires review")
            findings += 1
            continue
        if not path.is_file():
            continue
        count += 1
        if sensitive_path(relative):
            print(f"{relative}: sensitive filename requires review")
            findings += 1
        for rule, line in scan_text(path.read_bytes().decode("utf-8", errors="ignore")):
            print(f"{relative}:{line}: {rule} (value redacted)")
            findings += 1
    if findings:
        raise SystemExit(f"FAILED: {findings} credential-pattern/path findings")
    print(f"PASS: no configured credential patterns in {count} files; this is not an exhaustive secret scan")


if __name__ == "__main__":
    main()
