import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest
from unittest.mock import patch


WORKFLOW = (Path(__file__).parents[1] / "workflows/repo-assist.md").read_text()


def script_after(marker, indent):
    return textwrap.dedent(WORKFLOW.split(marker, 1)[1].split(f"\n{' ' * indent}EOF", 1)[0])


SELECTION = script_after("      python3 - << 'EOF'\n", 6)
CAPACITY = script_after("          node <<'EOF'\n", 10)


class MaintenanceModeTests(unittest.TestCase):
    def select(self, count, event="schedule", other_prs=0):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "issues.json").write_text("[]")
            prs = [{"title": f"[repo-assist] Fix {i}"} for i in range(count)]
            prs += [{"title": f"Human PR {i}"} for i in range(other_prs)]
            (root / "prs.json").write_text(json.dumps(prs))
            original_open = open

            def local_open(path, *args, **kwargs):
                if str(path).startswith("/tmp/gh-aw/"):
                    path = root / Path(path).name
                return original_open(path, *args, **kwargs)

            with patch("builtins.open", local_open), patch.dict(
                os.environ, GITHUB_EVENT_NAME=event, GITHUB_RUN_ID="123"
            ), contextlib.redirect_stdout(io.StringIO()):
                exec(compile(SELECTION, "task_selection", "exec"), {})
            return json.loads((root / "task_selection.json").read_text())

    def test_below_capacity_preserves_three_weighted_tasks(self):
        for count, slots in [(0, 4), (4, 4), (7, 1)]:
            with self.subTest(count=count):
                result = self.select(count)
                self.assertFalse(result["maintenance_only"])
                self.assertEqual(result["new_pr_limit"], slots)
                self.assertEqual(len(set(result["selected_tasks"])), 3)
                self.assertEqual(result, self.select(count))

    def test_at_and_above_capacity_prioritizes_maintenance_and_triage(self):
        for count in [8, 9, 200]:
            with self.subTest(count=count):
                result = self.select(count)
                self.assertTrue(result["maintenance_only"])
                self.assertEqual(result["new_pr_limit"], 0)
                self.assertEqual(result["selected_tasks"], [6, 1, 2])

    def test_human_prs_do_not_consume_capacity(self):
        self.assertFalse(self.select(7, other_prs=250)["maintenance_only"])

    def test_manual_and_command_events_remain_exempt(self):
        for event in ["workflow_dispatch", "issue_comment", "issues"]:
            with self.subTest(event=event):
                result = self.select(20, event)
                self.assertFalse(result["maintenance_only"])
                self.assertEqual(result["new_pr_limit"], 4)

    def test_cap_no_longer_gates_activation(self):
        self.assertNotIn("needs.pre_activation.outputs.check_result", WORKFLOW)
        self.assertEqual(WORKFLOW.count("if: github.event_name == 'schedule'"), 2)
        self.assertIn('--paginate "repos/$GITHUB_REPOSITORY/pulls', WORKFLOW)

    def check_capacity(self, count, requests, other_prs=0, api_failure=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "output.json"
            prs_file = root / "prs.json"
            gh = root / "gh"
            gh.write_text(
                "#!/usr/bin/env python3\n"
                "import os, pathlib, sys\n"
                "if os.environ['API_FAILURE'] == 'true':\n"
                "    sys.exit('GitHub API unavailable')\n"
                "print(pathlib.Path(os.environ['PRS_FILE']).read_text())\n"
            )
            gh.chmod(0o755)
            output.write_text(json.dumps({"items": requests}))
            prs_file.write_text("\n".join(
                [json.dumps("[repo-assist] Fix")] * count
                + [json.dumps("Human PR")] * other_prs
            ))
            return subprocess.run(
                ["node", "-e", CAPACITY],
                env=dict(
                    os.environ, OUTPUT_FILE=str(output), PRS_FILE=str(prs_file),
                    PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                    GITHUB_SERVER_URL="https://github.com", GITHUB_REPOSITORY="example/project",
                    API_FAILURE=str(api_failure).lower(),
                ),
                capture_output=True, text=True, check=False,
            )

    def test_gate_allows_new_prs_within_available_slots(self):
        for count, requested in [(0, 4), (7, 1)]:
            with self.subTest(count=count):
                result = self.check_capacity(count, [{"type": "create_pull_request"}] * requested)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_gate_rejects_full_capacity_and_oversized_batches(self):
        for count, requested in [(7, 2), (8, 1), (9, 1)]:
            with self.subTest(count=count):
                result = self.check_capacity(count, [{"type": "create_pull_request"}] * requested)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("capacity exceeded", result.stderr)

    def test_gate_allows_maintenance_and_triage_above_capacity(self):
        result = self.check_capacity(12, [
            {"type": "push_to_pull_request_branch"},
            {"type": "add_labels"},
            {"type": "update_issue"},
        ])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_gate_allows_noop_above_capacity(self):
        result = self.check_capacity(12, [{"type": "noop"}])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_gate_does_not_count_human_prs(self):
        result = self.check_capacity(7, [{"type": "create_pull_request"}], other_prs=250)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_api_failure_does_not_become_zero_open_prs(self):
        result = self.check_capacity(8, [{"type": "create_pull_request"}], api_failure=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("GitHub API unavailable", result.stderr)

    def test_maintenance_does_not_need_a_creation_capacity_api_call(self):
        result = self.check_capacity(8, [{"type": "add_labels"}], api_failure=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
