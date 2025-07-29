---
tools:
  github:
    allowed: [search_issues, get_issue, get_issue_comments, add_issue_comment]
---

### Output Report implemented via GitHub Issue

You will share one "output issue" with all other developers entitled "Team Status DATE" where DATE is the date, UTC time, UK date format DD/MM/YYYY. If an open issue with this title doesn't exist, create it with content describing what it's for. Ignore closed issues with this title. You and other team members will add comments to this issue as you progress. The comments will be used as the "output report" for the workflow.

When you start your work, add an issue comment to the output issue saying you are starting work and briefly saying who you are and what you are doing.

Before each tool use, add another issue comment saying you are starting work and briefly saying who you are, what you've done and what you are about to do.

At the end of the workflow:

- add an issue comment saying you have finished your work and briefly saying who you are and what you did.

- if you encounter a failure or don't have access to a tool, add a comment to the issue noting the problem, explaining what you would have done if you had access, and give your analysis of what needs to be fixed.

- write the Job Summary for GitHub Actions run ${{ github.run_id }} in ${{ github.repository }} to report progess. Do this by writing to the special file `$GITHUB_STEP_SUMMARY` where GITHUB_STEP_SUMMARY is an environment variable set by GitHub Actions.

Include this at the end of each added issue comment:

```
> AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
```
