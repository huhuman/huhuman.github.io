# Shun-Hsiang Hsu — portfolio

Personal research and engineering portfolio. Built with Jekyll, Liquid, structured resume data, and a BibTeX publication list.

## Review and build

See [local build and security notes](docs/build-and-security.md) for the tested build, validation, and preview commands. Use Ruby 3.4, Bundler 2.6.9, and the committed `Gemfile.lock`. Serve only the generated `_site` directory on loopback.

Content is ready for owner review; open [the editorial checklist](docs/content-review.md) before finalizing claims or publication status.

| Content                           | Source                                         |
| --------------------------------- | ---------------------------------------------- |
| Homepage and profile              | `_pages/about.md`                              |
| Selected work summaries and links | `_data/selected_work.yml`                      |
| Web resume                        | `assets/json/resume.json`                      |
| Publications and evidence links   | `_bibliography/papers.bib`                     |
| Downloadable resume               | `assets/pdf/Shun_Hsiang_Hsu_Resume.pdf`        |
| Layout and styling                | `_layouts/`, `_includes/`, `_sass/custom.scss` |
| Approved public files             | `public_assets` in `_config.yml`               |

The build checks public output, local links, content policy, and a limited set of credential patterns. Review notes and build tooling are excluded from generated pages. Source files and Git history remain public if this repository is public; exclusions are not a place to store secrets.

## Publication

The workflow builds and validates pull requests without deploying them. A push to `main`/`master`, or a manual run on those branches, publishes validated output to `gh-pages`. The owner authorized this release after the final security review. Future content edits should keep resume-backed claims and the editorial checklist consistent.

## Attribution

Originally based on [al-folio](https://github.com/alshedivat/al-folio). The portfolio retains Jekyll and bibliography integration with a customized interface. See [LICENSE](LICENSE) for the inherited license.
