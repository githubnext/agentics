# 🔍 Daily Accessibility Review

> For an overview of all available workflows, see the [main README](../README.md).

The [daily accessibility review workflow](../workflows/daily-accessibility-review.md?plain=1) will perform accessibility reviews of the application.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Daily Accessibility Review workflow to your repository
gh aw add-wizard githubnext/agentics/daily-accessibility-review
```

This walks you through adding the workflow to your repository.

## Configuration

This workflow requires no configuration and works out of the box.

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

