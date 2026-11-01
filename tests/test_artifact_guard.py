import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("check_site", Path(__file__).parents[1] / "bin/check_site.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

POLICY = "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; object-src 'none'; frame-src 'none'; base-uri 'none'; form-action 'none'"
HTML = '<!doctype html><meta http-equiv="Content-Security-Policy" content="' + POLICY + '"><h1>Portfolio</h1>'


class ArtifactGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        for route in ["", "cv", "publications"]:
            self.write((route + "/index.html").lstrip("/"), HTML)
        self.write("assets/pdf/Shun_Hsiang_Hsu_Resume.pdf", "public resume fixture")
        self.write(".nojekyll", "")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def test_known_artifact_is_accepted(self):
        self.assertEqual(checker.validate(self.root), [])

    def test_unexpected_generated_page_is_rejected(self):
        self.write("internal-planning/index.html", HTML)
        self.assertTrue(any("Unexpected public page" in e for e in checker.validate(self.root)))

    def test_retired_case_study_page_is_rejected(self):
        self.write("work/synthetic-data/index.html", HTML)
        self.assertTrue(any("Unexpected public page" in e for e in checker.validate(self.root)))

    def test_pages_publication_marker_is_required(self):
        (self.root / ".nojekyll").unlink()
        self.assertTrue(any("Missing public destination: .nojekyll" in e for e in checker.validate(self.root)))

    def test_private_notes_and_environment_files_are_rejected(self):
        self.write("docs/content-review.md", "editorial notes")
        self.write(".env.production", "example fixture")
        errors = checker.validate(self.root)
        self.assertTrue(any("docs/content-review.md" in e for e in errors))
        self.assertTrue(any(".env.production" in e for e in errors))

    def test_inline_script_and_external_runtime_are_rejected(self):
        self.write("index.html", HTML + '<script>window.example = true</script><script src="https://example.invalid/test.js"></script>')
        errors = checker.validate(self.root)
        self.assertTrue(any("Executable inline script" in e for e in errors))
        self.assertTrue(any("Non-local resource" in e for e in errors))

    def test_permissive_policy_cannot_pass_by_containing_safe_substrings(self):
        self.write("index.html", HTML.replace("script-src 'self'", "script-src 'self' https: 'unsafe-inline'"))
        self.assertTrue(any("content policy" in e for e in checker.validate(self.root)))

    def test_duplicate_policy_directives_are_rejected(self):
        self.write("index.html", HTML.replace("default-src 'self'", "script-src *; default-src 'self'"))
        self.assertTrue(any("content policy" in e for e in checker.validate(self.root)))

    def test_broken_local_evidence_link_is_rejected(self):
        self.write("index.html", HTML + '<a href="/missing.pdf">Paper</a>')
        self.assertTrue(any("Broken local link" in e for e in checker.validate(self.root)))

    def test_local_fragment_links_are_accepted_when_target_exists(self):
        self.write("index.html", HTML + '<section id="selected-work"></section>')
        self.write("cv/index.html", HTML + '<a href="/#selected-work">Selected work</a>')
        self.assertEqual(checker.validate(self.root), [])

    def test_local_fragment_link_to_removed_section_is_rejected(self):
        self.write("cv/index.html", HTML + '<a href="/#removed-section">Old section</a>')
        self.assertTrue(any("Broken local fragment" in e for e in checker.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
