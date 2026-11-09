import copy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


WORKFLOW = (Path(__file__).parents[1] / "workflows/repo-assist.md").read_text()
OUTCOME = textwrap.dedent(
    WORKFLOW.split("      - name: Validate Repo Assist outcome\n", 1)[1]
    .split("          node <<'EOF'\n", 1)[1].split("\n          EOF", 1)[0]
)
MEMORY = textwrap.dedent(
    WORKFLOW.split("      script: |\n", 1)[1].split("\nsafe-outputs:", 1)[0]
)


def assessment(task, command="sed -n '1,160p' tests/Tests.fs", path="tests/Tests.fs",
               kind="test"):
    return {
        "task": task,
        "result": "Inspected concrete assertions; no justified change identified",
        "evidence": [{"command": command, "path": path, "kind": kind}],
    }


def trace(command, content="<shellId: 1 completed with exit code 0>", success=True):
    return [
        {"type": "tool.execution_start", "data": {
            "toolCallId": "read-tests", "toolName": "bash",
            "arguments": {"command": command},
        }},
        {"type": "tool.execution_complete", "data": {
            "toolCallId": "read-tests", "success": success,
            "result": {"content": content},
        }},
    ]


class OutcomeTests(unittest.TestCase):
    def check(self, items=None, assessments=None, selection=None, events=None,
              command="", omit=None):
        entries = assessments if assessments is not None else [
            assessment(task) for task in range(1, 11)
        ]
        if items is None:
            items = [{"type": "noop", "message": json.dumps({
                "outcome": "justified_noop", "assessments": entries,
            })}]
        state = selection or {
            "selected_tasks": [1, 2, 3],
            "generic_fallback_tasks": [9, 8, 10, 7, 4, 5],
            "maintenance_only": False,
        }
        calls = trace("sed -n '1,160p' tests/Tests.fs") if events is None else events
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = {
                "agent_output.json": json.dumps({"items": items}),
                "task_selection.json": json.dumps(state),
                "agent-session.jsonl": "\n".join(map(json.dumps, calls)),
            }
            for name, value in files.items():
                if name != omit:
                    (root / name).write_text(value)
            return subprocess.run(
                ["node", "-e", OUTCOME],
                env=dict(os.environ, OUTPUT_DIR=directory, REPO_ASSIST_COMMAND=command),
                capture_output=True, text=True, check=False,
            )

    def report(self):
        return {
            "type": "update_issue", "issue_number": 10,
            "body": "## Suggested Actions for Maintainer\n\n## Run History\n",
        }

    def test_complete_recorded_noop_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_issue_queue_does_not_excuse_missing_generic_work(self):
        result = self.check(assessments=[assessment(task) for task in [1, 2, 3]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("was not assessed", result.stderr)

    def test_issue_metadata_cannot_substitute_for_source_assessment(self):
        command = "gh api repos/example/project/issues"
        entries = [assessment(task, command, "repos/example/project/issues", "github")
                   for task in range(1, 11)]
        result = self.check(assessments=entries, events=trace(command))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("concrete source/test/docs/check", result.stderr)

    def test_unobserved_command_cannot_support_a_completion_claim(self):
        result = self.check(events=[])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("absent or failed command", result.stderr)

    def test_failed_shell_edit_does_not_become_success_from_tool_envelope(self):
        result = self.check(events=trace(
            "sed -n '1,160p' tests/Tests.fs",
            "jq: Cannot index array with string\n<shellId: 1 completed with exit code 5>",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("absent or failed command", result.stderr)

    def test_failed_tool_is_not_evidence(self):
        result = self.check(events=trace(
            "sed -n '1,160p' tests/Tests.fs", success=False,
        ))
        self.assertNotEqual(result.returncode, 0)

    def test_running_command_is_not_completed_evidence(self):
        result = self.check(events=trace(
            "sed -n '1,160p' tests/Tests.fs", "Process still running",
        ))
        self.assertNotEqual(result.returncode, 0)

    def test_error_text_in_source_is_not_the_commands_exit_status(self):
        result = self.check(events=trace(
            "sed -n '1,160p' tests/Tests.fs",
            'let message = "exit code 5"\n<shellId: 1 completed with exit code 0>',
        ))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_listing_files_is_not_source_inspection(self):
        command = "ls tests/Tests.fs"
        result = self.check(
            assessments=[assessment(task, command) for task in range(1, 11)],
            events=trace(command),
        )
        self.assertNotEqual(result.returncode, 0)

    def test_task_selection_file_is_not_source_evidence(self):
        command = "cat /tmp/gh-aw/task_selection.json"
        result = self.check(
            assessments=[assessment(task, command, "/tmp/gh-aw/task_selection.json")
                         for task in range(1, 11)],
            events=trace(command),
        )
        self.assertNotEqual(result.returncode, 0)

    def test_duplicate_tasks_cannot_hide_a_skipped_task(self):
        result = self.check(assessments=[assessment(1), assessment(1)])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unique integers", result.stderr)

    def test_missing_result_or_evidence_is_rejected(self):
        for field in ["result", "evidence"]:
            with self.subTest(field=field):
                entry = assessment(1)
                del entry[field]
                result = self.check(assessments=[entry])
                self.assertNotEqual(result.returncode, 0)

    def test_path_must_appear_in_recorded_command(self):
        entries = [assessment(task, path="docs/nonexistent.md") for task in range(1, 11)]
        result = self.check(assessments=entries)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inspected path", result.stderr)

    def test_invalid_evidence_kind_is_rejected(self):
        result = self.check(assessments=[assessment(1, kind="guess")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid evidence kind", result.stderr)

    def test_maintenance_noop_needs_no_generic_sweep(self):
        command = "gh api repos/example/project/issues"
        result = self.check(
            selection={"selected_tasks": [6, 1, 2], "generic_fallback_tasks": [],
                       "maintenance_only": True},
            assessments=[assessment(task, command, "repos/example/project/issues", "github")
                         for task in [6, 1, 2]],
            events=trace(command),
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_corrupted_selection_cannot_skip_assessments(self):
        for selected, fallback in [([], []), ([1, 2, 3], []), ([1, 1, 2], [])]:
            with self.subTest(selected=selected, fallback=fallback):
                result = self.check(selection={
                    "selected_tasks": selected, "generic_fallback_tasks": fallback,
                    "maintenance_only": False,
                })
                self.assertNotEqual(result.returncode, 0)

    def test_explicit_stop_is_exempt_and_needs_no_session_or_selection(self):
        result = self.check(
            items=[{"type": "noop", "message": "Explicit stop: no action taken"}],
            command="Do not do anything. No PR or comments.", omit="agent-session.jsonl",
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blank_command_is_still_normal_mode(self):
        result = self.check(items=[{"type": "noop", "message": "Nothing to do"}], command=" \n")
        self.assertNotEqual(result.returncode, 0)

    def test_incomplete_is_distinct_from_justified_noop(self):
        result = self.check(items=[{
            "type": "report_incomplete", "message": "Memory could not be saved",
        }], omit="agent-session.jsonl")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("not a justified noop", result.stdout)

    def test_missing_evidence_artifact_fails_explicitly(self):
        for name in ["task_selection.json", "agent-session.jsonl", "agent_output.json"]:
            with self.subTest(name=name):
                self.assertNotEqual(self.check(omit=name).returncode, 0)

    def test_label_work_requires_monthly_reporting(self):
        result = self.check(items=[{"type": "add_labels", "labels": ["bug"]}])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Monthly Activity update", result.stderr)

    def test_label_changes_with_reporting_are_not_noops(self):
        result = self.check(items=[
            {"type": "add_labels", "labels": ["bug"]}, self.report(),
        ])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_monthly_bookkeeping_alone_cannot_bypass_assessment(self):
        result = self.check(items=[self.report()])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("bookkeeping alone", result.stderr)

    def test_mutation_and_noop_batch_is_rejected_even_with_report(self):
        result = self.check(items=[
            {"type": "add_labels"}, self.report(), {"type": "noop", "message": "No PR"},
        ])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("do not emit noop", result.stderr)

    def test_unrelated_issue_is_not_a_monthly_report(self):
        result = self.check(items=[{
            "type": "create_issue", "title": "[repo-assist] Other issue",
            "body": self.report()["body"],
        }])
        self.assertNotEqual(result.returncode, 0)

    def test_new_monthly_tracker_allows_handler_applied_prefix(self):
        month = datetime.now(timezone.utc).strftime("%Y-%m")
        for prefix in ["", "[repo-assist] "]:
            with self.subTest(prefix=prefix):
                result = self.check(items=[
                    {"type": "add_labels", "labels": ["bug"]},
                    {"type": "create_issue", "title": f"{prefix}Monthly Activity {month}",
                     "body": self.report()["body"]},
                ])
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_information_only_command_needs_no_monthly_reporting(self):
        result = self.check(items=[{
            "type": "add_comment", "body": "Requested investigation",
        }], command="Investigate and reply; do not open a PR")
        self.assertEqual(result.returncode, 0, result.stderr)


class MemoryContractTests(unittest.TestCase):
    def initial(self):
        return {
            "version": 1, "cursors": {"labelling_after": None, "investigation_after": None},
            "issues": [], "fixes": [], "checks": [], "completed_actions": [], "priorities": [],
        }

    def validate(self, notes):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "notes.json").write_text(json.dumps(notes))
            return subprocess.run(
                ["node", "-e", 'const memoryRoot = process.env.MEMORY_ROOT;\n' + MEMORY],
                env=dict(os.environ, MEMORY_ROOT=directory),
                capture_output=True, text=True, check=False,
            )

    def test_prompt_examples_match_the_actual_memory_validator(self):
        notes = self.initial()
        table = WORKFLOW.split("### Exact memory contract\n", 1)[1].split(
            "Use the actual current date", 1)[0]
        for line in table.splitlines():
            if line.startswith("| `"):
                name = line.split("`")[1]
                notes[name] = [json.loads(line.split("`")[3])]
        self.assertTrue(all(notes[name] for name in [
            "issues", "fixes", "checks", "completed_actions", "priorities",
        ]))
        result = self.validate(notes)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_checks_are_an_array_not_a_map(self):
        notes = self.initial()
        notes["checks"] = {"issue_sweep": "looked at issue titles"}
        result = self.validate(notes)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("checks must contain", result.stderr)

    def test_bad_issue_state_reports_allowed_enum(self):
        notes = self.initial()
        notes["issues"] = [{
            "number": 473, "state": "blocked by compiler",
            "updated_at": "2026-11-09", "note": "Upstream fix pending",
        }]
        result = self.validate(notes)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("state must be one of", result.stderr)
        self.assertIn("deferred", result.stderr)

    def test_schema_errors_name_missing_fields_without_erasing_state(self):
        notes = self.initial()
        notes["issues"] = [{"number": 473, "state": "deferred"}]
        before = copy.deepcopy(notes)
        result = self.validate(notes)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires exactly number, state, updated_at, note", result.stderr)
        self.assertEqual(notes, before)


if __name__ == "__main__":
    unittest.main()
