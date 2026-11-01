# Portfolio recruiting refresh implementation plan

> Execute approved audit recommendations in this session. Use independent content/security investigations and a final code review. The owner subsequently authorized publication after the final security audit; this supersedes earlier publication holds in this plan.

**Goal:** Present verifiable research and engineering outcomes for U.S. 2027 full-time recruiting, remove template noise, and reduce accidental disclosure and unnecessary runtime dependencies.

**Architecture:** Retain Jekyll, Liquid, the bibliography, and JSON resume. Use static, accessible HTML for portfolio content and one shared local stylesheet. Case studies contain only resume-supported facts; confidential details and content review notes stay outside generated output.

**Baseline:** Main f344ac5; original package-lock.json is user-modified and must be preserved. Local bundle check currently fails because a Git-sourced jekyll-terser checkout is missing.

## Task 1 — Content evidence

- [x] Add four `_projects/*.md` case studies using the approved audit and resume; preserve research/prototype/pilot/under-review distinctions.
- [x] Add research projects to `assets/json/resume.json`, concise publication summaries, and independently verified public links in `_bibliography/papers.bib`.
- [x] Put unresolved content questions in `docs/content-review.md`, excluded from output.

## Task 2 — Public interface

- [x] Replace `_pages/about.md` and `_layouts/about.liquid` with a compact hero, real metrics, selected work, experience, research and contact.
- [x] Add a reusable work-card include, project layout and a Work index; improve CV and publication navigation.
- [x] Build responsive light/dark styles in `_sass/custom.scss`; use existing research imagery and a resized portrait.
- [x] Keep all core content visible without JavaScript. Add semantic main/skip link, accessible navigation, explicit link labels and descriptive image alternatives.

## Task 3 — Security and build

- [x] Inspect tracked files and reachable history for credential patterns without printing matching secret values. Record scope and confidence limits.
- [x] Exclude docs/tests/config artifacts and unused template pages/assets from output; remove external post fetching and unnecessary runtime integrations.
- [x] Resolve build dependencies reproducibly; tighten Actions permissions and deployment trigger separation.
- [x] Add meaningful build-artifact checks for accidentally published files, placeholder content, broken local links and insecure resources; run before and after fixes where baseline build is possible.
- [x] Apply a tested browser content policy and referrer policy compatible with GitHub Pages; distinguish HTML meta protections from unsupported HTTP header protections.

## Task 4 — Verification and handoff

- [x] Build real Jekyll output, serve on loopback, inspect desktop/mobile and light/dark modes with Chromium, test navigation and no-JS content.
- [x] Check secrets/dependencies and generated output; document what cannot be established locally.
- [x] Obtain a separate spec/code review, fix material findings and rerun affected checks.
- [x] Transfer the reviewed source changes to the user's checkout without touching their package-lock.json; provide local preview and content-review notes. Do not push or deploy.
