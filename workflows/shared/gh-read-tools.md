---
tools:
  claude:
    Bash: 
      allowed:
      - "gh label list:*"
      - "gh label view:*"
      - "gh issue list:*"
      - "gh issue view:*"
      - "gh pr list:*"
      - "gh pr view:*"
      - "gh repo view:*"
      - "git log:*"
      - "git diff:*"
      - "git status:*"
      - "git branch:*"
      - "git checkout:*"
---

## GitHub Tools

You can use the GitHub MCP tools to perform various tasks in the repository. In addition to the tools listed below, you can also use the `gh` command line tool to perform various tasks in the repository:

- List labels: `gh label list ...`
- View label: `gh label view <label-name> ...`
- List issues: `gh issue list ...`
- View issue: `gh issue view <issue-number> ...`
- List pull requests: `gh pr list ...`
- View pull request: `gh pr view <pull-request-number> ...`
- View repository: `gh repo view <repository-name> ...`
- View git log: `git log ...`
- View git diff: `git diff ...`
- View git status: `git status ...`
- View git branch: `git branch ...`
- Checkout git branch: `git checkout <branch-name> ...`

