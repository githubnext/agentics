# 🧹 Draft PR Cleanup

> For an overview of all available workflows, see the [main README](../README.md).

The [Draft PR Cleanup workflow](../workflows/draft-pr-cleanup.md?plain=1) automatically manages stale draft pull requests by warning about inactivity and closing drafts that remain inactive for 14+ days. This helps maintain a clean, manageable PR list and reduces triage burden for maintainers.

## Installation

````bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Import the workflow to your repository
gh aw import https://github.com/githubnext/agentics/blob/main/workflows/draft-pr-cleanup.md
````

## What it does

The workflow implements a two-phase automated cleanup policy for draft PRs:

1. **Warning Phase (10-13 days)**: Adds a `stale-draft` label and posts a friendly warning comment
2. **Cleanup Phase (14+ days)**: Closes the draft PR with an explanatory comment

This approach is fair and transparent - contributors always get advance warning before any action is taken.

## How it works

### Inactivity Detection

A draft PR is considered inactive when there's been no:
- Commits to the branch
- Comments on the PR
- Label changes
- Review activity
- Updates to title or description

### Smart Exemptions

The workflow automatically skips PRs with these labels:
- `keep-draft` - Explicitly marked to keep open
- `blocked` - Waiting on external factors
- `awaiting-review` - Ready for review but not yet converted

### Process Flow

**Daily Scan:**
1. Queries all open draft PRs
2. Calculates inactivity period for each
3. Classifies into: Exempt, Active, Warning, or Ready to Close
4. Takes appropriate action based on classification

**Warning Phase (10-13 days inactive):**
- Adds `stale-draft` label
- Posts friendly comment explaining the policy
- Provides clear instructions to prevent closure

**Cleanup Phase (14+ days inactive):**
- Closes the PR with explanatory comment
- Emphasizes this is not a rejection
- Explains how to reopen if work continues

## When it runs

- **Daily** with fuzzy scheduling
- **Manually** via workflow_dispatch

## Benefits

1. **Reduces PR clutter** - Makes PR list more manageable for maintainers
2. **Fair warning system** - 4-day notice before any closure
3. **Respectful communication** - Emphasizes drafts can be reopened
4. **Customizable exemptions** - Easy to keep drafts open with labels
5. **Transparent process** - Clear metrics and summaries in each run

## Configuration

The workflow uses these thresholds by default:
- **Warning threshold**: 10 days of inactivity
- **Closure threshold**: 14 days of inactivity
- **Warning period**: 4 days between warning and closure

To customize these thresholds, edit the workflow prompt in your repository.

## Safe Outputs

The workflow uses GitHub's safe-outputs system with these limits per run:
- **add-labels**: Up to 20 stale-draft labels
- **add-comment**: Up to 20 warning/closure comments  
- **close-pull-request**: Up to 10 PR closures

## Preventing Auto-Closure

Contributors can prevent their draft PRs from being closed by:

1. **Adding activity**: Push commits, add comments, or update the PR
2. **Adding `keep-draft` label**: Explicitly marks the draft to stay open
3. **Converting to ready**: Mark the PR as ready for review
4. **Adding `blocked` or `awaiting-review`**: Indicates PR is waiting on something

## Example Output

When the workflow runs, it generates a summary like:

````markdown
## 🧹 Draft PR Cleanup Summary

**Run Date**: 2026-02-17

### Statistics
- **Total Draft PRs**: 25
- **Exempt from Cleanup**: 3 (keep-draft, blocked, or awaiting-review)
- **Active (< 10 days)**: 15
- **Warned (10-13 days)**: 4
- **Closed (14+ days)**: 3

### Actions Taken
- **New Warnings Added**: 4
- **PRs Closed**: 3
- **PRs Skipped (exempt)**: 3

### PRs Warned This Run
- #12345: "Add new feature" (11 days inactive)
- #12346: "Fix bug in parser" (12 days inactive)

### PRs Closed This Run
- #12340: "Old feature draft" (21 days inactive)
- #12341: "Experimental changes" (15 days inactive)
````

## Success Metrics

The workflow tracks effectiveness through:
- **Draft PR rate**: Percentage of draft PRs vs total PRs
- **Triage efficiency**: Time saved for maintainers reviewing PR list
- **Reopen rate**: Indicates accuracy of staleness detection
- **Coverage**: Percentage of eligible drafts processed

## Customization

You can customize the workflow by editing:
- **Inactivity thresholds**: Change 10-day and 14-day periods
- **Exemption labels**: Add or modify labels that prevent closure
- **Comment text**: Customize warning and closure messages
- **Safe-output limits**: Adjust max PRs processed per run

## Best Practices

1. **Create the `stale-draft` label** in your repository before first run
2. **Document the policy** in your CONTRIBUTING.md
3. **Review closed drafts periodically** to ensure policy is working well
4. **Encourage use of `keep-draft`** for intentional long-running drafts
5. **Monitor metrics** to tune thresholds for your repository

## Why This Workflow?

Many active repositories accumulate draft PRs over time, making it harder for maintainers to:
- Triage active work
- Identify important PRs
- Track progress on features
- Maintain a clean PR list

This workflow automates the tedious task of identifying and managing stale drafts while being respectful to contributors and providing clear paths to keep drafts open when needed.

## Related Workflows

- [Issue Triage](issue-triage.md) - Similar automated triage for issues
- [Contribution Guidelines Checker](contribution-guidelines-checker.md) - Ensures PRs follow contribution standards
- [PR Fix](pr-fix.md) - Helps fix failing PR checks
