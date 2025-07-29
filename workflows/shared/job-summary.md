---
tools:
  github:
    allowed: ["add_issue_comment"]
  Bash:
    allowed:
      ["gh api -X PATCH /repos/${{ github.repository }}/issues/comments/:*"]
---

### Output Report implemented via GitHub Action Job Summary

You will use the Job Summary for GitHub Actions run ${{ github.run_id }} in ${{ github.repository }} to report progess. This will be the "output report" for the workflow. This means writing to the special file `$GITHUB_STEP_SUMMARY` where GITHUB_STEP_SUMMARY is an environment variable set by GitHub Actions.

- At the end of the workflow, finalize the output report with your steps, analysis and findings.
- If any step fails, you should still finalize the output issue comment with an explanation of what was attempted and why it failed.
- Include this at the end of the output report:

  ```
  > AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
  ```
