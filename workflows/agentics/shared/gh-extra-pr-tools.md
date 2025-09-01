---
tools:
  claude:
    allowed:
      Bash: 
      - "git checkout:*"
      - "git branch:*"
      - "git add:*"
      - "git commit:*"
      - "git push:*"
      - "gh pr create:*"
---

## Creating and Updating Pull Requests

To create a branch, add changes to your branch and push code to GitHub, use Bash `git branch...` `git add ...`, `git commit ...`, `git push ...` etc.

When using `git commit`, ensure you set the author name and email appropriately. Do this by using a `--author` flag with `git commit`, for example `git commit --author "${{ github.workflow }} <github-actions[bot]@users.noreply.github.com>" ...`.

To create a pull request with the changes, use Bash `gh pr create --repo ${{ github.repository }} ...` 