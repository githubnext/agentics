import contextlib
import io
import itertools
import json
import os
from pathlib import Path
import tempfile
import textwrap
import unittest
from unittest.mock import patch


WORKFLOW = (Path(__file__).parents[1] / "workflows/repo-assist.md").read_text()
SELECTION = textwrap.dedent(
    WORKFLOW.split("      python3 - << 'EOF'\n", 1)[1].split("\n      EOF", 1)[0]
)
GENERIC_TASKS = [9, 8, 10, 7, 4, 5]


class GenericFallbackTests(unittest.TestCase):
    def select(self, selected=None, issues=None, command="", run_id="123",
               repo_assist_prs=0, event="schedule"):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "issues.json").write_text(json.dumps(issues or []))
            (root / "prs.json").write_text(json.dumps([
                {"title": f"[repo-assist] Fix {index}"}
                for index in range(repo_assist_prs)
            ]))
            original_open = open

            def local_open(path, *args, **kwargs):
                if str(path).startswith("/tmp/gh-aw/"):
                    path = root / Path(path).name
                return original_open(path, *args, **kwargs)

            with contextlib.ExitStack() as stack:
                stack.enter_context(patch("builtins.open", local_open))
                stack.enter_context(patch.dict(
                    os.environ, GITHUB_RUN_ID=run_id, REPO_ASSIST_COMMAND=command,
                    GITHUB_EVENT_NAME=event
                ))
                stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                if selected is not None:
                    random = stack.enter_context(patch("random.Random"))
                    random.return_value.choices.return_value = selected
                exec(compile(SELECTION, "task_selection", "exec"), {})
            return json.loads((root / "task_selection.json").read_text())

    def test_issue_only_selection_offers_unselected_generic_work(self):
        result = self.select([1, 2, 3])
        self.assertEqual(result["selected_tasks"], [1, 2, 3])
        self.assertEqual(result["generic_fallback_tasks"], GENERIC_TASKS)

    def test_selected_testing_performance_and_forward_work_are_not_repeated(self):
        result = self.select([9, 8, 10])
        self.assertEqual(result["generic_fallback_tasks"], [7, 4, 5])

    def test_other_generic_selection_still_falls_back_to_tests_perf_and_forward(self):
        result = self.select([7, 4, 5])
        self.assertEqual(result["generic_fallback_tasks"], [9, 8, 10])

    def test_every_initial_selection_has_a_bounded_nonrepeating_plan(self):
        for selected in itertools.combinations(range(1, 11), 3):
            with self.subTest(selected=selected):
                plan = self.select(list(selected))["generic_fallback_tasks"]
                self.assertEqual(plan, [task for task in GENERIC_TASKS if task not in selected])
                self.assertTrue(3 <= len(plan) <= 6)
                self.assertEqual(len(plan), len(set(plan)))
                self.assertFalse(set(plan).intersection(selected))

    def test_empty_issue_queue_does_not_disable_proactive_work(self):
        result = self.select(issues=[])
        self.assertTrue(result["generic_fallback_tasks"])
        self.assertEqual(
            result["generic_fallback_tasks"],
            [task for task in GENERIC_TASKS if task not in result["selected_tasks"]],
        )

    def test_issue_backlog_does_not_suppress_fallback_plan(self):
        result = self.select([1, 2, 3], issues=[{"number": 1, "labels": []}])
        self.assertEqual(result["generic_fallback_tasks"], GENERIC_TASKS)

    def test_explicit_commands_have_no_generic_fallback_plan(self):
        for command in ["Investigate this issue", "Run Task 9", "\nFix the regression\n"]:
            with self.subTest(command=command):
                result = self.select([1, 2, 3], command=command)
                self.assertEqual(result["generic_fallback_tasks"], [])
                self.assertEqual(result["selected_tasks"], [1, 2, 3])

    def test_blank_command_remains_normal_mode(self):
        self.assertEqual(
            self.select([1, 2, 3], command=" \n")["generic_fallback_tasks"], GENERIC_TASKS
        )

    def test_maintenance_only_mode_has_no_generic_fallback_plan(self):
        for count in [8, 20]:
            with self.subTest(count=count):
                result = self.select([9, 8, 10], repo_assist_prs=count)
                self.assertTrue(result["maintenance_only"])
                self.assertEqual(result["selected_tasks"], [6, 1, 2])
                self.assertEqual(result["generic_fallback_tasks"], [])
                self.assertEqual(result["new_pr_limit"], 0)

    def test_below_capacity_and_manual_runs_still_offer_generic_work(self):
        for count, event in [(7, "schedule"), (20, "workflow_dispatch")]:
            with self.subTest(count=count, event=event):
                result = self.select([1, 2, 3], repo_assist_prs=count, event=event)
                self.assertFalse(result["maintenance_only"])
                self.assertEqual(result["generic_fallback_tasks"], GENERIC_TASKS)

    def test_run_seed_is_still_reproducible(self):
        self.assertEqual(self.select(run_id="98765"), self.select(run_id="98765"))


if __name__ == "__main__":
    unittest.main()
