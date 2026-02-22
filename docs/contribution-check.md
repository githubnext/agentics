# 🔍 Contribution Check

> For an overview of all available workflows, see the [main README](../README.md).

The [contribution check workflow](../workflows/contribution-check.md?plain=1) runs on a regular schedule (every 4 hours) to review a batch of open pull requests against the repository's contribution guidelines. It helps maintainers efficiently prioritize community contributions by evaluating PRs for compliance with CONTRIBUTING.md and categorizing them as ready to review, needing work, or falling outside contribution guidelines.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/contribution-check
```

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can trigger this workflow manually via workflow_dispatch or let it run on its configured schedule.

## How It Works

````mermaid
graph LR
    A[Fetch Open PRs] --> B[Pre-filter Candidates]
    B --> C[Check CONTRIBUTING.md]
    C --> D{Compliant?}
    D -->|Ready| E[Label: lgtm]
    D -->|Needs Work| F[Add Feedback Comment]
    D -->|Off Guidelines| G[Label: spam]
    E --> H[Create Report Issue]
    F --> H
    G --> H
````

## Configuration

The workflow uses a pre-filtering step to intelligently select PRs for evaluation. You can customize:

- **Target repository**: Set a `TARGET_REPOSITORY` repository variable to check PRs in a different repository than where the workflow runs. By default, it checks the repository where the workflow is installed.
- **Schedule frequency**: Change `every 4 hours` to your preferred interval
- **Report format**: Customize the report layout rules in the main workflow prompt

The workflow requires a `CONTRIBUTING.md` file (or `.github/CONTRIBUTING.md` or `docs/CONTRIBUTING.md`) to evaluate PRs against. If no contribution guidelines exist, PRs will be marked with `no-guidelines` quality.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Open pull requests and their metadata (title, description, author, labels, association)
- PR diffs and changed files list
- Repository contribution guidelines (`CONTRIBUTING.md`)
- Repository structure, README, and architecture documentation
- Related issues referenced in PR descriptions
- Test files and patterns adjacent to changed code
- Other open PRs touching the same files

## What it creates

- **Report issues** with title prefix "[Contribution Check Report]" containing structured evaluations of PRs grouped by:
  - Ready to review 🟢 (lgtm)
  - Needs a closer look 🟡 (needs-work)
  - Off-guidelines 🔴 (spam)
- **Comments on PRs** with constructive feedback and agentic prompts when quality is not `lgtm`
- **Labels on PRs** based on quality signals: `spam`, `needs-work`, `lgtm`, `outdated`
- **Labels on report issues**: `contribution-report` plus quality signals found in the batch

Requires `issues: read`, `pull-requests: write`, and `contents: read` permissions.

Previous report issues are automatically closed when new reports are created.

## What web searches it performs

This workflow does not perform web searches.

## Human in the loop

- Review the report issues to understand which PRs need attention and prioritize maintainer review time
- Validate that PRs marked as `lgtm` are actually ready for in-depth code review
- Check PRs marked `needs-work` to ensure the automated feedback is constructive and accurate
- Review PRs flagged as `spam` or `off-guidelines` before taking any action (closing, labeling, etc.)
- Adjust the workflow's filter logic if too many false positives or false negatives occur
- Monitor the agentic prompts posted to PRs — disable the workflow if the prompts are not helpful or are confusing contributors
- Engage with contributors who receive feedback to clarify expectations and welcome improvements
- Disable or uninstall the workflow if contribution checking automation is not accurate or helpful for your repository's needs
