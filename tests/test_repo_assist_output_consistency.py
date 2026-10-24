from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


WORKFLOW = (Path(__file__).parents[1] / "workflows/repo-assist.md").read_text()
VALIDATOR = textwrap.dedent(
    WORKFLOW.split("          node <<'EOF'\n", 1)[1].split("\n          EOF", 1)[0]
)
MONTH = datetime.now(timezone.utc).strftime("%Y-%m")
TITLE = f"[repo-assist] Monthly Activity {MONTH}"
RUN_URL = "https://github.com/example/project/actions/runs/123"
BODY = f"## Run History\n\n### Now - [Run]({RUN_URL})"


class OutputConsistencyTests(unittest.TestCase):
    def check_outputs(self, items, command="", issues=None, api_failure=False):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output.json"
            monthly = Path(directory) / "monthly.json"
            gh = Path(directory) / "gh"
            gh.write_text(
                "#!/usr/bin/env python3\n"
                "import os, pathlib, sys\n"
                "if os.environ['API_FAILURE'] == 'true':\n"
                "    sys.exit('GitHub API unavailable')\n"
                "print(pathlib.Path(os.environ['MONTHLY_ISSUES_FILE']).read_text())\n"
            )
            gh.chmod(0o755)
            output.write_text(json.dumps({"items": items}))
            monthly.write_text("\n".join(
                json.dumps([issue["number"], issue["title"]])
                for issue in ([{"number": 42, "title": TITLE}] if issues is None else issues)
            ))
            return subprocess.run(
                ["node", "-e", VALIDATOR],
                env=dict(
                    os.environ, OUTPUT_FILE=str(output), MONTHLY_ISSUES_FILE=str(monthly),
                    COMMAND_TEXT=command, GITHUB_SERVER_URL="https://github.com",
                    GITHUB_REPOSITORY="example/project", GITHUB_RUN_ID="123",
                    PATH=f"{directory}{os.pathsep}{os.environ['PATH']}",
                    API_FAILURE=str(api_failure).lower(),
                ),
                capture_output=True, text=True, check=False,
            )

    def assert_allowed(self, items, **kwargs):
        result = self.check_outputs(items, **kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_rejected(self, items, message, **kwargs):
        result = self.check_outputs(items, **kwargs)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(message, result.stderr)

    def test_genuine_noop_and_memory_only_checks_are_allowed(self):
        self.assert_allowed([{"type": "noop"}])
        self.assert_allowed([])

    def test_noop_is_incompatible_with_every_enabled_mutation(self):
        for kind in [
            "add_comment", "add_labels", "remove_labels", "create_issue",
            "update_issue", "create_pull_request", "push_to_pull_request_branch",
        ]:
            with self.subTest(kind=kind):
                self.assert_rejected(
                    [{"type": kind}, {"type": "noop"}], "cannot emit noop",
                    command="Even command mode must be consistent",
                )

    def test_incomplete_is_not_a_successful_noop(self):
        self.assert_rejected(
            [{"type": "report_incomplete"}, {"type": "noop"}], "cannot emit noop"
        )

    def test_labels_without_code_changes_still_require_reporting(self):
        self.assert_rejected([{"type": "add_labels"}], "require a current-month activity")

    def test_audited_label_then_noop_regression(self):
        self.assert_rejected([
            {"type": "add_labels", "item_number": 4461, "labels": [{"name": "bug"}]},
            {"type": "noop", "message": "Labelled issue; no further safe action"},
        ], "cannot emit noop")

    def test_audited_comment_without_monthly_report_regression(self):
        self.assert_rejected([
            {"type": "add_comment", "item_number": 134, "body": "Verified implementation guidance"},
        ], "require a current-month activity")

    def test_current_month_creation_with_run_history_is_allowed(self):
        self.assert_allowed([
            {"type": "add_comment"},
            {"type": "create_issue", "title": TITLE, "body": BODY},
        ])

    def test_create_issue_prefix_is_normalized_like_safe_output_handler(self):
        self.assert_allowed([{
            "type": "create_issue", "title": TITLE.removeprefix("[repo-assist] "), "body": BODY,
        }])

    def test_existing_monthly_issue_update_is_allowed(self):
        self.assert_allowed([
            {"type": "push_to_pull_request_branch"},
            {"type": "update_issue", "issue_number": 42, "body": BODY},
        ])

    def test_old_month_or_unrelated_issue_does_not_satisfy_reporting(self):
        for title in ["[repo-assist] Monthly Activity 2000-01", "[repo-assist] Other issue"]:
            with self.subTest(title=title):
                self.assert_rejected(
                    [{"type": "update_issue", "issue_number": 42, "body": BODY}],
                    "require a current-month activity", issues=[{"number": 42, "title": title}],
                )

    def test_closing_the_tracker_does_not_satisfy_reporting(self):
        self.assert_rejected([{
            "type": "update_issue", "issue_number": 42, "body": BODY, "status": "closed",
        }], "require a current-month activity")

    def test_other_repository_tracker_does_not_satisfy_reporting(self):
        self.assert_rejected([{
            "type": "update_issue", "issue_number": 42, "body": BODY, "repo": "other/project",
        }], "require a current-month activity")

    def test_report_requires_history_and_current_run_link(self):
        for body in [
            "", f"Only a link: {RUN_URL}", "## Run History\nOld run",
            f"## Suggested Actions\n[Run]({RUN_URL})\n## Run History\nOld run",
            f"## Run History\n- [Run]({RUN_URL})",
            f"## Run History\nOld run\n## Other\n### Now - [Run]({RUN_URL})",
        ]:
            with self.subTest(body=body):
                self.assert_rejected(
                    [{"type": "update_issue", "issue_number": 42, "body": body}],
                    "require a current-month activity",
                )

    def test_month_rollover_can_close_old_tracker_and_create_current_one(self):
        self.assert_allowed([
            {"type": "update_issue", "issue_number": 41, "status": "closed"},
            {"type": "create_issue", "title": TITLE, "body": BODY},
        ], issues=[{"number": 41, "title": "[repo-assist] Monthly Activity 2000-01"}])

    def test_command_mode_is_exempt_from_monthly_reporting(self):
        self.assert_allowed([{"type": "add_comment"}], command="Investigate this issue")

    def test_blank_command_retains_non_command_reporting(self):
        self.assert_rejected(
            [{"type": "add_comment"}], "require a current-month activity", command=" \n"
        )

    def test_truthful_incomplete_run_can_preserve_partial_work(self):
        self.assert_allowed([
            {"type": "add_comment"},
            {"type": "report_incomplete", "message": "Monthly report blocked"},
        ])

    def test_diagnostics_alone_do_not_require_monthly_reporting(self):
        self.assert_allowed([{"type": "missing_tool"}])
        self.assert_allowed([{"type": "report_incomplete"}])

    def test_lookup_failures_are_explicit(self):
        self.assert_rejected(
            [{"type": "add_comment"}], "GitHub API unavailable", api_failure=True
        )

    def test_exempt_runs_do_not_depend_on_monthly_issue_lookup(self):
        self.assert_allowed([{"type": "noop"}], api_failure=True)
        self.assert_allowed([{"type": "add_comment"}], command="Investigate", api_failure=True)
        self.assert_allowed(
            [{"type": "add_comment"}, {"type": "report_incomplete"}], api_failure=True
        )


if __name__ == "__main__":
    unittest.main()
