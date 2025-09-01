---
tools:
  claude:
    allowed:
      Bash: 
      - "gh label list:*"
      - "gh label view:*"
      - "gh repo view:*"
      - "gh issue list:*"
      - "gh issue view:*"
      - "gh pr list:*"
      - "gh pr view:*"
---

## GitHub Tools

You can use the GitHub MCP tools to perform various tasks in the repository. You can also use the following `gh` command line invocations:

- List labels: `gh label list ...`
- View label: `gh label view <label-name> ...`
- View repository: `gh repo view ${{ github.repository }} ...`
- List issues: `gh issue list --label <label-name> ...`
- View issue: `gh issue view <issue-number> ...`
- List pull requests: `gh pr list --label <label-name> ...`
- View pull request: `gh pr view <pr-number> ...`

