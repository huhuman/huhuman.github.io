# Portfolio visual revision implementation plan

User-approved scope: the nine review requests in the current conversation. This initially revised the local review version; the owner subsequently authorized committing, pushing, and publishing after the final security audit. Preserve the user's package-lock changes.

**Goal:** A vivid, concise portfolio with direct project evidence, a chronological experience section, and skills attached to actual work.

**Architecture:** Keep static Jekyll, the strict CSP and local-only runtime. Replace the project collection and case-study pages with a data-driven list on the homepage. Existing CV and publications remain separate pages.

## Changes

- [x] 1. Apply the user's confirmed saturated orange-red and deep navy palette in `_sass/custom.scss`, including both light/dark modes, buttons, icons, project illustrations, and favicon. Verify text contrast after the palette change.
- [x] 2. Remove availability/recruiting messages from `_pages/about.md`.
- [x] 3. Add local inline SVG icons with visible text to the top profile links. Keep lab/contact/profile information at the top.
- [x] 4. Delete the standalone metrics strip and its styles.
- [x] 5. Use `Selected Work` as the sole section heading, with no decorative category label or extra tagline.
- [x] 6. Create `_data/selected_work.yml` and a full-width row include: image or decorative icon, short title, one short summary, and direct public project/paper/code links when available. Use existing resume-supported topics; add the existing vision-language project artifacts. Do not fabricate links for internal company work. Delete `_projects/`, its layout and the redundant Work index. Rewrite CV URLs to public artifacts or homepage anchors.
- [x] 7. Replace the experience block with an accessible ordered timeline, dates, roles and concise resume-supported contributions. Use the simple heading `Experience` and remove case/full-experience links.
- [x] 8. Following the user's compactness revision, remove the standalone homepage Skills section. Add 2–3 resume-supported applied skills beneath each selected project and experience using `_includes/skill-tags.liquid`; keep complete categories in the CV. Do not assign tools to projects without evidence.
- [x] 9. Delete the bottom contact/quote section. Keep the footer minimal and all contact/profile links at the top. Simplify the remaining publications heading consistently.

## Files and navigation

Update `_pages/about.md`, `_includes/header.liquid`, `_includes/footer.liquid`, `_pages/404.md`, `_config.yml`, `assets/json/resume.json`, `_sass/custom.scss`, and `assets/img/favicon.svg`. Create `_includes/icon.liquid`, `_includes/work-row.liquid` and `_data/selected_work.yml`. Remove the unused project layout/include and case documents. Keep public routes `/`, `/cv/`, `/publications/`, and `/404.html`; preserve `.nojekyll`, the resume PDF, sitemap and asset allowlist.

## Verification and documentation

- [x] Update existing artifact-check fixtures to the intended public routes, reject leftover generated case pages, and verify local fragment targets after navigation changes.
- [x] Build with the already prepared frozen offline Docker image. Run `python -m unittest discover -s tests`, `python bin/check_site.py _site`, source/generated secret checks, Prettier for touched files, and `git diff --check`.
- [x] Inspect real Chromium screenshots at desktop/tablet/390px/320px in light and dark modes. Check single-column work rows, timeline, icons, skill items, no removed copy/sections, no overflow, no-JS readability, publication filtering, theme persistence and no third-party requests. Recheck text contrast for the new palette.
- [x] Update README and content-review/build notes to reflect the homepage structure and removed routes. Preserve the original PDF and package-lock.json byte-for-byte. Leave local generated output ready for user review and stop only the preview server owned by this task.
