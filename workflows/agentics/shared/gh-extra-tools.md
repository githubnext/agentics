---
tools:
  claude:
    allowed:
      Bash: 
      - "gh label list:*"
      - "gh label view:*"
      - "git commit:*"
---

## GitHub Tools

You can use the GitHub MCP tools to perform various tasks in the repository. In addition to the tools listed below, you can also use the following `gh` command line invocations:

- List labels: `gh label list ...`
- View label: `gh label view <label-name> ...`

## Git Configuration

When using `git commit`, ensure you set the author name and email appropriately. Do this by using a `--author` flag with `git commit`, for example `git commit --author "${{ github.workflow }} <github-actions[bot]@users.noreply.github.com>" ...`.
