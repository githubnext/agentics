# 🔧 PR Fix

> For an overview of all available workflows, see the [main README](../README.md).

The ["pr-fix" workflow](../workflows/pr-fix.md?plain=1) is an alias workflow "/pr-fix" that will help you fix and complete pull requests. By default it will analyze failing CI checks in pull requests, identify root causes, and implement fixes to resolve issues and get PRs back to a passing state. 

You can trigger the workflow in default mode by adding a comment to a pull request with the command:

```text
/pr-fix
```

or by writing a comment:

```text
/pr-fix Please add more tests.
```

## How It Works

````mermaid
graph LR
    A[/pr-fix Command] --> B[Analyze CI Failures]
    B --> C[Identify Root Cause]
    C --> D[Implement Fix]
    D --> E[Push to Branch]
    E --> F[Comment on PR]
````

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/pr-fix
```

This walks you through adding the workflow to your repository.

You can't start a run of this workflow directly as it is triggered in the context of a pull request with failing checks.

To trigger the workflow on a specific pull request, add a comment with the command:

```text
/pr-fix
```

## Configuration

This workflow requires no configuration and works out of the box. You can edit it to specify custom build commands, testing procedures, linting rules, and code formatting standards, or customize these for all agents in AGENTS.md in your repository.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Pull request details, files, and metadata
- Workflow run logs and job outputs
- Check run results and status information
- Commit information and diff context
- Repository contents and file structure
- Existing issues related to CI failures

## What it creates

- Pushes fixes directly to the pull request branch
- Adds comments to pull requests explaining the changes made
- May create issues for complex problems requiring human intervention

## Triggering CI on Pull Requests

By default, pushes to pull request branches by this workflow do not trigger CI workflow runs. This is a GitHub Actions feature to prevent event cascades.

To trigger CI checks on PRs updated by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

## What web searches it performs

- Searches for error message documentation and solutions
- Looks up best practices for specific technologies and frameworks
- Researches common fixes for build and test failures

## Human in the loop

- Review all changes pushed by the workflow before merging the PR
- Validate that fixes actually resolve the intended issues
- Monitor for any unintended side effects or regressions
- Provide additional context or instructions via PR comments when needed
- Override or revert changes if the automated fix is incorrect

## Activity duration

- By default this workflow will run for up to 48 hours after being triggered
- The workflow stops automatically after this period to prevent indefinite runs
- You can re-trigger the workflow by commenting with the alias again if needed
