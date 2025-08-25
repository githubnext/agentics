# 🔍 Daily Accessibility Review

> For an overview of all available workflows, see the [main README](../README.md).

The [daily accessibility review workflow](../workflows/daily-accessibility-review.md?plain=1) will perform accessibility reviews of the application.

## Installation

```bash
gh aw add daily-accessibility-review -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-accessibility-review
```

## Configuration

- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify application startup commands and URLs to test
- Customize accessibility testing tools and WCAG compliance levels
- Add project-specific accessibility scenarios and user journey testing
- After editing run `gh aw compile` to update the workflow.

## What it reads from GitHub

- Repository contents and source code for accessibility analysis

## What it creates

- Creates new issues documenting accessibility problems found
- Requires `issues: write` permission

## What web searches it performs

- Searches for WCAG 2.2 guidelines and accessibility information
- May look up accessibility best practices and compliance requirements

## Human in the loop

- Review accessibility issues created by the workflow for accuracy
- Validate accessibility problems with screen readers or accessibility tools
- Prioritize accessibility fixes based on severity and impact
- Test accessibility improvements before closing issues
- Disable or uninstall the workflow if accessibility reports are not accurate or useful

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## YOLO

- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes on coding tasks in the [main README](../README.md). You will need to edit the workflow file to add the commands to build and run your project. After editing run `gh aw compile` to update the workflow.
