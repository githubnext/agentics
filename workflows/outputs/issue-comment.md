---
tools:
  github:
    allowed: ["add_issue_comment"]
  Bash:
    allowed:
      ["gh api -X PATCH /repos/${{ github.repository }}/issues/comments/:*"]
---

### Output Report implemented via GitHub Issue Comment

You will create one "output issue comment" on the GitHub issue, and update it as you progress. This will be the "output report" for the workflow.

Initially:

- The output issue comment should initially a checklist with only one entry indicating the first step you are about to perform. There should be no other items in the checklist.

During the workflow:

- Before each tool use, update the output issue comment, with a partial the checklist, where the last entry is the tool you are about to use and a phrase explaining why. To update the output issue comment, use the `gh api` command to PATCH the comment with new content. Here's how you can do it:
  ```
  gh api -X PATCH /repos/${{ github.repository }}/issues/comments/NNNN -f body='Your updated comment text here'
  ```

At the end of the workflow:

- Finalize the output issue comment by replacing the entire content of the output issue comment with your analysis and findings, removing the progress reporting.
- If any step fails, you should still finalize the output issue comment with an explanation of what was attempted and why it failed.
- Write the Job Summary for GitHub Actions run ${{ github.run_id }} in ${{ github.repository }} to report progess. Do this by writing to the special file `$GITHUB_STEP_SUMMARY` where GITHUB_STEP_SUMMARY is an environment variable set by GitHub Actions.

Include this at the end of the added issue comment:

```
> AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
```
