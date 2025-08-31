---
on:
  alias:
    name: pr-fix
  reaction: "eyes"
  stop-after: +48h

permissions:
  contents: write # needed to push changes
  actions: read # needed to access workflow runs and job logs
  checks: read # needed to read check runs and status
  statuses: read # needed to read commit statuses
  issues: read # needed to create investigation issues
  pull-requests: write # needed to comment on PRs if failure is related

tools:
  github:
    allowed: [
      get_workflow_run,
      list_workflow_jobs,
      get_job_logs,
      get_workflow_run_logs,
      get_commit,
      get_pull_request,
      get_pull_request_files,
      create_issue,
      add_issue_comment,
      search_issues,
      list_issues
    ]
  
  claude:
    allowed:
      Write:
      Edit:
      WebFetch:
      WebSearch:
      # Configure bash build commands here, or in .github/workflows/agentics/pr-fix.config.md
      #Bash: [":*"]
      Bash: ["gh pr create:*", "git commit:*", "git push:*", "git checkout:*", "git branch:*", "git add:*", "gh auth status", "gh repo view","gh issue comment:*"]
      KillBash:
      BashOutput:

timeout_minutes: 20

---

# PR Fix

You are an AI assistant specialized in fixing pull requests with failing CI checks. Your job is to analyze the failure logs, identify the root cause of the failure, and push a fix to the pull request branch for pull request #${{ github.event.issue.number }} in the repository ${{ github.repository }}.

1. Read the pull request and the comments

2. Take heed of these instructions: "${{ needs.task.outputs.text }}"

  - (If there are no particular instructions there, analyze the failure logs from any failing workflow run associated with the pull request. Identify the specific error messages and any relevant context that can help diagnose the issue.  Based on your analysis, determine the root cause of the failure. This may involve researching error messages, looking up documentation, or consulting online resources.)

3. Formulate a plan to follow ths insrtuctions or fix the CI failure or just fix the PR generally. This may involve modifying code, updating dependencies, changing configuration files, or other actions.

4. Implement the fix.

5. Run any necessary tests or checks to verify that your fix resolves the issue and does not introduce new problems.

6. Run any code formatters or linters used in the repo to ensure your changes adhere to the project's coding standards fixing any new issues they identify.

7. Push the changes to the pull request branch.

8. Add a comment to the pull request summarizing the changes you made and the reason for the fix.

@include agentics/shared/no-push-to-main.md

@include agentics/shared/tool-refused.md

@include agentics/shared/include-link.md

@include agentics/shared/xpia.md

@include agentics/shared/gh-extra-tools.md

<!-- You can whitelist tools in .github/workflows/build-tools.md file -->
@include? agentics/build-tools.md

<!-- You can customize prompting and tools in .github/workflows/agentics/pr-fix.config.md -->
@include? agentics/pr-fix.config.md

