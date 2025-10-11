# 🏥 CI Doctor

> For an overview of all available workflows, see the [main README](../README.md).

The [CI Doctor workflow](../workflows/ci-doctor.md?plain=1) monitors your GitHub Actions workflows and automatically investigates CI failures. When a monitored workflow fails, the CI Doctor conducts a deep analysis to identify root causes, patterns, and provides actionable recommendations for fixing the issues.

## Installation

```bash
# Install the 'gh aw' extension
gh aw extension install githubnext/agentics

# Add the CI Doctor workflow to your repository
gh aw add githubnext/agentics/ci-doctor --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://githubnext.github.io/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

After merging the PR, the workflow will automatically trigger when monitored CI workflows fail. You cannot start this workflow manually as it responds to workflow failure events.

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

You can specify which workflows to monitor (currently monitors "Daily Perf Improver" and "Daily Test Improver") by editing the workflow directly.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Failed workflow runs and job details
- Workflow and job logs from failed executions
- Repository contents and configuration files
- Commit details that triggered the failure
- Pull request information (if failure is PR-related)
- Historical issues for pattern matching
- Actions workflow runs and status information

## What it creates

- Creates detailed investigation issues with root cause analysis
- Adds comments to related pull requests with failure analysis
- Updates existing issues if similar failures have occurred
- Stores investigation data in cache for pattern recognition
- Requires `issues: write`, `actions: read`, and `pull-requests: write` permissions

## What web searches it performs

- Searches for error message explanations and solutions
- Looks up documentation for failing dependencies or tools
- May search for known issues and workarounds for identified problems

## Human in the loop

- Review CI failure investigation reports for accuracy and completeness
- Validate root cause analysis and recommended fixes
- Implement suggested solutions and test fixes
- Close investigation issues once problems are resolved
- Monitor for recurring failure patterns and adjust workflows accordingly
- Disable or uninstall the workflow if failure investigations are not providing value

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering.
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.
