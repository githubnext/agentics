# 🔍 Daily Accessibility Review

> For an overview of all available workflows, see the [main README](../README.md).

The [daily accessibility review workflow](../workflows/daily-accessibility-review.md?plain=1) will perform accessibility reviews of the application.

## Installation

```bash
gh aw add daily-accessibility-review -r githubnext/agentics --pr
```

This creates an issue in your repository recording accessibility problems found.

```bash
gh aw run daily-accessibility-review
```

**Mandatory Checklist**

* [ ] I understand that, by default, the agentic portion of this workflow will generate and run bash commands in the confine of the GitHub Actions VM, with network access.

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. You can use local configuation to specify which accessibility standards to check (e.g., WCAG 2.1, WCAG 2.2), types of accessibility issues to prioritize, and reporting format. Local configuration can be done in `.github/workflows/agentics/daily-accessibility-review.config.md`.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

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

