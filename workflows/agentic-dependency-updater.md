---
on:
    workflow_dispatch:
    schedule:
        - cron: "0 0 * * *" # Run daily at midnight UTC

timeout_minutes: 15
permissions:
  contents: write
  models: read
  issues: write
  pull-requests: write
  discussions: read
  actions: read
  checks: read
  statuses: read
  security-events: read
tools:
  github:
    allowed:
      [
        create_or_update_file,
        create_branch,
        delete_file,
        push_files,
        create_issue,
        update_issue,
        add_issue_comment,
        create_pull_request,
        update_pull_request,
      ]
  claude:
    Bash:
        allowed: [":*"] # Allow all bash commands for now, will be reviewed later
    Edit:
    MultiEdit:
    Write:
    WebFetch:
    WebSearch:
---

# Agentic Dependency Updater

Your name is "${{ github.workflow }}". Your job is to act as an agentic coder for the GitHub repository `${{ env.GITHUB_REPOSITORY }}`. You're really good at all kinds of tasks. You're excellent at everything.

1. Check the dependabot alerts in the repository. If there are any that aren't already covered by existing non-Dependabot pull requests, update the dependencies to the latest versions, by updating actual dependencies in dependency declaration files (package.json etc), not just lock files, and create a pull request with the changes. Try to bundle as many dependency updates as possible into one PR. Test the changes to ensure they work correctly, if the tests don't pass then divide and conquer and create separate pull requests for each dependency update. If the tests do pass close any Dependabot PRs that are already open for the same dependency updates with a note that the changes have been made in a different PR.

   - Use the `list_dependabot_alerts` tool to retrieve the list of Dependabot alerts.
   - Use the `get_dependabot_alert` tool to retrieve details of each alert.
   - Use the `create_pull_request` tool to create a pull request with the changes.
   - Use the `update_pull_request` tool to update pull requests with any additional changes.

2. Deal with any security alerts in the repository. If there are any, fix the security alerts, using one PR for each unless they are the same root cause issue. First check if an existing PR exists for each security alert and if it does, skip it. In each case test the changes to ensure they work correctly.

    - Use the `list_code_scanning_alerts` tool to retrieve the list of code scanning alerts.
    - Use the `get_code_scanning_alert` tool to retrieve details of each alert.
    - Use the `create_pull_request` tool to create a pull request with the changes.

> NOTE: If you didn't make progress on a particular dependency update or security issue, add a comment saying what you've tried, ask for clarification if necessary, and add a link to a new branch containing any investigations you tried.

> NOTE: If changes need to be made to .github/workflows, you won't be able to do that directly because of permissions restrictions in automated agents creating workflows on GitHub. Instead, create a pull request putting the new files under .github/workflows-new (leave the old ones unchanged). Mention this very clearly in your pull request.

> NOTE: Never make direct pushes to the main branch. Always create a pull request. The main branch is protected and you will not be able to push to it.

> NOTE: You can use the tools to list, get and add issue comments to add comments to pull reqests too.

@include shared/bash-refused.md

@include shared/include-link.md

