# Build and security

## Local review

Use Ruby 3.4 and Bundler 2.6.9, matching CI. From the repository root:

```sh
bundle install
python -m unittest discover -s tests
python bin/check_secrets.py
JEKYLL_ENV=production bundle exec jekyll build
python bin/check_site.py _site
python bin/check_secrets.py --site _site
python -m http.server 8765 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8765/`. Serve only the generated `_site` directory, bound to loopback; do not serve the repository root. The local review does not publish anything. Keep `Gemfile.lock` committed; frozen dependency installation is required in CI. Changes to source require a rebuild before refreshing this static preview.

Content starts in `_pages/about.md`, `_data/selected_work.yml`, `assets/json/resume.json`, and `_bibliography/papers.bib`. The final editorial checklist is [content-review.md](content-review.md). The PDF remains the supplied resume; replacing it should include another metadata and attachment review.

The current workspace already has a generated `_site`. To review it, run only the final HTTP-server command above. A local Docker image prepared during this task can rebuild without network access or host Ruby installation:

```sh
mkdir -p _site
docker run --rm --network none --user "$(id -u):$(id -g)" \
  -e BUNDLE_FROZEN=true -e JEKYLL_ENV=production --entrypoint bundle \
  -v "$PWD:/srv/jekyll:ro" -v "$PWD/_site:/preview" -w /srv/jekyll \
  huhuman-portfolio-build:release-2026-10-31 \
  exec jekyll build --disable-disk-cache --destination /preview
```

This image is local to the reviewed machine, not a published dependency or requirement for CI. Its ID is `sha256:c9f20f4b9d51ba2d3135aa4ed49f1138d6b627995252bd5c04204eed1033bfe4`. Native builds and CI use the committed lock.

The final local release checks passed 15 guard tests and 32 Chromium route/viewport/theme combinations (1440px, 820px, 390px, and 320px; light and dark). The four public HTML pages are `/`, `/cv/`, `/publications/`, and `/404.html`; the complete artifact contains 22 files. The artifact guard also checks local fragment targets so navigation cannot silently point at removed sections. Browser checks cover work rows, profile icons, the timeline, skills attached to projects/experience, complete skill categories in the CV, removed routes/copy, no-JavaScript content, publication filtering, theme persistence, blocked storage, and CSP inline-script rejection. No horizontal overflow, page errors, or third-party resource requests were observed. Seven representative text/button color pairs in both themes exceeded 4.5:1 contrast; this is not a complete accessibility audit. Hosted release results are recorded in the repository's Actions runs.

## Public output and browser controls

The site renders its core content in static HTML, with local CSS, JavaScript, images and PDF. It has no application backend, login, upload form, analytics or third-party runtime requests. Publication filtering and theme selection are progressive enhancements; disabling JavaScript leaves the content and navigation readable.

`_plugins/public-files.rb` copies only assets named in `_config.yml`'s `public_assets`. Review notes, scripts, environment files and unused template files are excluded. New images or downloads must be added to the allowlist. `bin/check_site.py` separately rejects unexpected HTML routes, known non-public paths, broken local links, inline code/styles, third-party resources and a missing or relaxed CSP in the actual artifact.

The early CSP meta element permits scripts and styles only from the same origin and blocks network connections, plugins, frames, form submissions and base URL changes. It is defense in depth, not protection against a compromised repository or hosting account. A meta policy cannot supply HTTP-only protections such as `frame-ancestors`, HSTS or `X-Content-Type-Options`; no claim is made that those hosting headers were configured. See [MDN's CSP reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy).

## Security review scope

The 2026-10-31 release review covered current source, all 24 reachable Git commits and 1,165 distinct blobs after refreshing remote refs, the 22-file public artifact, retained workflows, dependencies, images, and resume PDFs. Gitleaks v8.30.1 returned no candidates in separate source, output, refreshed history, complete blob, and extracted document/metadata scans. Supplemental raw-byte and commit scans found no confirmed credentials. Temporary raw scanner inputs and redacted reports remain outside the repository; they are not published artifacts. These results supersede the earlier review in which the standard scanner was unavailable.

Gitleaks used the upstream-documented Docker image pinned by digest, with networking disabled and source mounted read-only. Standard detection has binary and pattern limitations. Supplemental inspection covered three distinct historical PDFs and 112 historical images, plus current and generated copies: no GPS/XMP location metadata, embedded PDF attachments, or executable JavaScript/Launch action keys were found. Public contact information in the supplied resume remains intentional public content. The scan does not prove that every arbitrary, obfuscated, or semantically confidential value has been identified; no OCR, steganography analysis, or credential validation against issuers was performed.

`bin/check_secrets.py` is the smaller, redacting guard retained in CI for high-confidence token/private-key patterns and sensitive filenames. Its tests verify that findings show location and rule without printing a matched value. It scans tracked and nonignored untracked source files, or a generated directory with `--site`; it does not replace the separate full-history audit or inspect PDF text and metadata.

Generated-site exclusions and `.gitignore` do **not** make a public source repository or its history private. Never place credentials, private company material or personal sensitive data in content-review notes. If a credential is discovered later, revoke it at its issuer first and then remove it from public source/history and deployed artifacts. The audit covers locally reachable refs, not dangling objects, unfetched remote refs, unrelated repositories, ignored caches, or external storage.

Authenticated, read-only GitHub checks confirmed public repository hosting, HTTPS enforcement, enabled secret scanning and push protection, zero open secret alerts, and zero repository Actions secrets. There are no main-branch rulesets or branch protection. Repository-wide Actions defaults still permit write access, while both retained workflows explicitly reduce permissions and isolate publication writes to the deployment job. Dependabot security updates are disabled at the repository setting, with weekly version updates configured in source. Dependabot alert listing was unavailable to the existing token; the complete lockfile advisory checks below provide separate coverage. Account MFA could not be verified. No repository/account security settings were changed.

Eight existing CodeQL alerts all pointed to the unused `assets/js/distillpub/template.v2.js` library: four regular-expression denial-of-service findings, two prototype-pollution findings, incomplete sanitization, and DOM XSS. The entire inactive Distill script directory and its unused layout/include were removed. They were already excluded from the public artifact; removal also eliminates their vulnerable source from the current branch. The post-push CodeQL run determines remote alert closure; no alert was manually dismissed or suppressed.

## Dependency remediation

Unused theme plugins and their dependency trees were removed. The retained lock was patched for five confirmed upstream advisory version ranges:

| Build dependency | Previous | Patched | Primary reference                                                                              |
| ---------------- | -------- | ------- | ---------------------------------------------------------------------------------------------- |
| Addressable      | 2.8.7    | 2.9.0   | [GHSA-h27x-rffw-24p4](https://github.com/advisories/GHSA-h27x-rffw-24p4)                       |
| concurrent-ruby  | 1.3.5    | 1.3.7   | [Upstream advisories](https://github.com/ruby-concurrency/concurrent-ruby/security/advisories) |
| REXML            | 3.4.1    | 3.4.2   | [CVE-2025-58767](https://www.ruby-lang.org/en/news/2025/09/18/dos-rexml-cve-2025-58767/)       |
| URI              | 1.0.3    | 1.0.4   | [CVE-2025-61594](https://www.ruby-lang.org/en/news/2025/10/07/uri-cve-2025-61594/)             |
| json             | 2.12.2   | 2.19.9  | [CVE-2026-54696 fix](https://github.com/ruby/json/releases/tag/v2.19.9)                        |

These gems run during build/development; GitHub Pages serves the resulting static files. No remotely reachable exploit was demonstrated in this portfolio. The final OSV advisory query covered all 55 unique locked gem/version pairs with 55 successful responses and zero remaining matches; Bundler 2.6.9 also returned no match. A fresh npm audit reported zero advisories across eight development dependencies. The json gem checksum matched the RubyGems version API, the loaded version was verified, and the frozen build passed with networking disabled. This supersedes the earlier partial 52/55 version-page review. It is a dated check against known advisories, not a complete `bundler-audit` run, operating-system/container audit, or guarantee against unknown vulnerabilities.

## CI and deployment

`.github/workflows/deploy.yml` keeps the existing `gh-pages` branch hosting. Pushes and pull requests targeting `main` or `master` run a read-only build; manual runs are also supported. The build checks committed-secret patterns, runs the Python validation tests, installs the locked Ruby dependencies with Bundler frozen mode, builds Jekyll, and validates `_site` and scans its files for credential patterns before uploading it. Ruby 3.4 and Bundler 2.6.9 are configured, and the dependency cache is keyed by `ruby/setup-ruby`.

The separate deployment job receives `contents: write` only after the build succeeds, and only for a push or manual run on `main`/`master`. It checks out `gh-pages` for Git metadata, downloads the artifact named for the current run and attempt, and publishes that artifact. It does not install dependencies or execute source scripts. Artifact download uses the action's current-run scope without a cross-run token. Only `_site` is uploaded; hidden files are included to retain `.nojekyll`. Deployment preserves branch history (`force: false`) and serializes writes to `gh-pages`.

Every retained action is pinned to a full commit SHA. The additional release pins were verified against the official commit links for [ruby/setup-ruby v1.336.0](https://github.com/ruby/setup-ruby/commit/de492cf36cbab201753d720ce4f4e336cd688c94), [GitHub Pages Deploy Action v4.8.0](https://github.com/JamesIves/github-pages-deploy-action/commit/d92aa235d04922e8f08b40ce78cc5442fcfbfa2f), and [CodeQL v4.39.0](https://github.com/github/codeql-action/commit/6f2ac81f5cd81fe351a197ba0b00d91d03cd2aee). Dependabot proposes weekly Bundler, npm, and GitHub Actions updates. CodeQL analyzes JavaScript, Ruby, and Python on relevant pushes, pull requests, and a weekly schedule; it has no repository-content write permission.

The old Docker publication, remote TOC script, formatter auto-dispatch, generated-HTML formatting, Lighthouse, and duplicate link/accessibility workflows were retired. Local-link and public-artifact validation now gate the build artifact itself.

Local checks verify YAML parsing, action pin shapes, permission boundaries, deployment gating, artifact scoping, and the build/validation commands. The owner authorized publication after the final security review. Hosted build, deployment, and CodeQL results must be checked against the pushed commit; a successful local build alone does not establish that the production site has updated.
