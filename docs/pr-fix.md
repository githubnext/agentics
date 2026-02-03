# 🔧 PR Fix

> For an overview of all available workflows, see the [main README](../README.md).

The ["@pr-fix" workflow](../workflows/pr-fix.md?plain=1) is an alias workflow "@pr-fix" that will help you fix and complete pull requests. By default it will analyze failing CI checks in pull requests, identify root causes, and implement fixes to resolve issues and get PRs back to a passing state. 

You can trigger the workflow in default mode by adding a comment to a pull request with the command:

```
/pr-fix
```

or by writing a comment:

```
/pr-fix Please add more tests.
```

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the PR Fix workflow to your repository
gh aw add githubnext/agentics/pr-fix --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can't start a run of this workflow directly as it is triggered in the context of a pull request with failing checks.

To trigger the workflow on a specific pull request, add a comment with the command:

```
/pr-fix
```

IMPORTANT: GitHub Actions runs will **not** trigger on commits pushed by this workflow and will **not** tell you that CI has not been run unless you have enabled a specific custom check for this condition. **You must open/close the PR or hit "Update branch" if offered to trigger CI.Yes it's painful and yes it's just something you need to be aware of.

**Mandatory Checklist**

* [ ] I have read the notes on coding tasks in the [main README](../README.md) and understand the implications.

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] I am a repository admin or have sufficient permissions, and am happy for the safe-outputs portion of this workflow to push new branches to the repository.

* [ ] I have enabled "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] I have considered enabling "Always suggest updating pull request branches" in the repository settings

* [ ] If in a fork, I have enabled "GitHub Actions" and "GitHub Issues" in the fork repository settings

* [ ] I will review all pull requests very carefully, and carefully monitor the repository. 

* [ ] I will operate this demonstrator for a time-limited period only (the default is 48h). 

* [ ] I understand that GitHub Actions runs will **not** trigger on pull requests created by this workflow, see above.

## Configuration

This workflow requires no configuration and works out of the box. You can use local configuration to specify custom build commands, testing procedures, linting rules, and code formatting standards. Local configuration can be done in `.github/workflows/agentics/pr-fix.config.md`.

 

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
- Requires `contents: write` and `pull-requests: write` permissions

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
