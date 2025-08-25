# 🔍 Daily Adhoc QA

> For an overview of all available workflows, see the [main README](../README.md).

The [daily Adhoc QA workflow](../workflows/daily-qa.md?plain=1) will perform adhoc quality assurance tasks in the repository, such as following the instructions in the README.md, tutorials and walkthroughs to check that the code builds and runs, and that the getting started process is simple and works well. You can edit and configure the workflow to describe more tasks. 

## Installation

```bash
gh aw add daily-qa -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-qa
```

## Configuration

- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify build tools, test frameworks, and QA scenarios
- Customize quality checks, performance benchmarks, and validation steps
- Add project-specific getting-started instructions and tutorial validation
- After editing run `gh aw compile` to update the workflow.

## What it reads from GitHub

- Repository contents and source code
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates new issues for problems found during QA
- Updates existing issues with QA findings
- Adds comments to issues with QA results
- Requires `issues: write` permission

## Human in the loop

- Review QA issues to validate reported problems
- Reproduce and confirm issues identified by the workflow
- Prioritize QA findings and assign them for resolution
- Close issues once problems have been addressed
- Disable or uninstall the workflow if QA findings are not actionable or valuable

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## YOLO

- If you're sufficiently isolated (e.g. operating in a fresh fork of an open source project, with Actions and Issues enabled ), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes on coding tasks in the [main README](../README.md).
