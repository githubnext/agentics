# 🧹 Draft PR Cleanup

**Automated cleanup policy for stale draft pull requests to maintain a clean and manageable PR list.**

## Overview

The Draft PR Cleanup workflow automatically manages inactive draft pull requests to reduce clutter and improve triage efficiency. It implements a two-phase policy: warning after 10 days of inactivity, then auto-closing after 14 days.

## How It Works

### Warning Phase (10-13 Days)
When a draft PR has been inactive for 10-13 days:
- Adds a friendly warning comment
- Applies a `stale-draft` label
- Informs the author how to prevent auto-closure

### Cleanup Phase (14+ Days)
When a draft PR has been inactive for 14+ days:
- Closes the PR with a respectful comment
- Explains why it was closed
- Reassures the author they can reopen it

### Inactivity Definition
A draft PR is considered inactive when it has no:
- New commits to the branch
- Comments on the PR
- Label changes
- Review requests or reviews
- Updates to title or description

## Preventing Auto-Closure

Authors can prevent auto-closure by:
- **Pushing a new commit** - Shows active development
- **Adding a comment** - Indicates work is continuing
- **Adding the `keep-draft` label** - Exempts from cleanup policy
- **Marking as ready for review** - Converts to regular PR

## Exemption Labels

PRs with these labels are never auto-closed:
- `keep-draft` - Explicitly keep this draft open
- `blocked` - Waiting on external dependencies
- `awaiting-review` - Ready for review but still in draft

## Schedule

- **Frequency**: Daily
- **Trigger**: Scheduled run + manual workflow dispatch

## Why This Workflow?

### Benefits
- **Cleaner PR list**: Easier for maintainers to see active work
- **Better triage**: Reduces noise and helps focus on actionable PRs
- **Automatic tracking**: No manual intervention needed
- **Fair warning**: Always notifies before closing
- **Reversible**: Closed PRs can be reopened anytime

### Use Cases
- Large repositories with many contributors
- Projects with frequent draft PR creation
- Teams wanting to maintain a tidy PR list
- Repositories with limited maintainer bandwidth

## Configuration

The workflow is pre-configured with sensible defaults:
- **Warning threshold**: 10 days
- **Closure threshold**: 14 days
- **Max warnings per run**: 20 PRs
- **Max closures per run**: 10 PRs

These limits prevent overwhelming the PR list with automated actions.

## Communication Style

All automated messages are:
- **Friendly and respectful** - Uses welcoming language
- **Clear and actionable** - Explains what to do next
- **Non-judgmental** - Emphasizes organization, not rejection
- **Grateful** - Thanks contributors for their work

## Example Messages

### Warning Comment
```
👋 This draft PR has been inactive for 10 days and will be automatically 
closed in 4 days unless there is new activity.

To prevent auto-closure:
- Push a new commit
- Add a comment to show work is continuing
- Add the `keep-draft` label if this needs to stay open longer
- Mark as ready for review if it's complete

Why this policy?
We're implementing this to keep the PR list manageable and help maintainers 
focus on active work. Closed PRs can always be reopened if work continues.
```

### Closure Comment
```
🧹 Closing this draft PR due to 14+ days of inactivity.

This is not a rejection! Feel free to:
- Reopen this PR if you continue working on it
- Create a new PR with updated changes
- Add the `keep-draft` label before reopening if you need more time

Why was this closed?
We're keeping the PR list manageable by automatically closing inactive drafts. 
This helps maintainers focus on active work and improves triage efficiency.

Thank you for your contribution! 🙏
```

## Success Metrics

The workflow tracks:
- **Total draft PRs** in the repository
- **Exempt PRs** with protection labels
- **Active PRs** (< 10 days inactive)
- **Warned PRs** (10-13 days)
- **Closed PRs** (14+ days)

## Best Practices

### For Maintainers
- Review the daily summary to understand draft PR health
- Use `keep-draft` label for important long-running work
- Monitor reopen rate to ensure thresholds are appropriate

### For Contributors
- Convert drafts to ready when complete
- Add comments periodically on long-running work
- Use `keep-draft` label for extended development

### For Organizations
- Communicate the policy in CONTRIBUTING.md
- Set expectations about draft PR lifecycle
- Adjust thresholds based on project velocity

## Customization

To customize the workflow for your repository:

1. **Adjust thresholds**: Modify warning (10 days) and closure (14 days) periods
2. **Change labels**: Use different exemption labels
3. **Modify messages**: Customize warning and closure comments
4. **Tune limits**: Adjust max warnings/closures per run

## Technical Details

- **Engine**: Copilot
- **Permissions**: Read-all (writes via safe-outputs)
- **Network**: Default GitHub access
- **Timeout**: 20 minutes
- **Safe outputs**: Labels, comments, PR closure

## Adding to Your Repository

```bash
gh aw add draft-pr-cleanup
gh aw compile
```

The workflow will start running daily and processing inactive draft PRs according to the policy.

## Origin

This workflow was created as a result of the Agent Performance Analyzer identifying that draft PRs accounted for 9.6% of open PRs in the gh-aw repository. The resulting automated draft cleanup successfully reduced the draft PR rate and improved triage efficiency.

**Source**: [gh-aw/draft-pr-cleanup.md](https://github.com/github/gh-aw/blob/main/.github/workflows/draft-pr-cleanup.md)

## Related Workflows

- [Issue Triage](issue-triage.md) - Automated issue classification
- [PR Fix](pr-fix.md) - Fix failing CI checks in PRs
- [Daily Repo Status](daily-repo-status.md) - Repository health monitoring
