import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("check_secrets", Path(__file__).parents[1] / "bin/check_secrets.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class SecretCheckTests(unittest.TestCase):
    def test_github_token_reports_location_without_value(self):
        token = "gh" + "p_" + "a" * 36
        findings = checker.scan_text("public text\n" + token)
        self.assertEqual(findings, [("github-token", 2)])
        self.assertNotIn(token, repr(findings))

    def test_private_key_marker_is_detected(self):
        marker = "-----BEGIN " + "PRIVATE KEY-----"
        self.assertIn(("private-key", 1), checker.scan_text(marker))

    def test_public_contact_and_ci_secret_references_are_allowed(self):
        self.assertEqual(checker.scan_text("hsus2@illinois.edu\n217-979-3580\nsecrets.GITHUB_TOKEN"), [])

    def test_sensitive_file_paths(self):
        self.assertTrue(checker.sensitive_path(Path(".env.production")))
        self.assertTrue(checker.sensitive_path(Path("config/deploy.pem")))
        self.assertFalse(checker.sensitive_path(Path(".env.example")))
        self.assertFalse(checker.sensitive_path(Path("assets/json/resume.json")))


if __name__ == "__main__":
    unittest.main()
