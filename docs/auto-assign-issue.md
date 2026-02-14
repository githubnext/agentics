# 🎯 Auto-Assign Issue

> For an overview of all available workflows, see the [main README](../README.md).

The [auto-assign issue workflow](../workflows/auto-assign-issue.md?plain=1) automatically assigns unassigned issues to relevant contributors based on their recent merged pull requests. This helps distribute work and ensures issues don't go unnoticed.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/auto-assign-issue
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run auto-assign-issue
```

## Configuration

This workflow requires no configuration and works out of the box. It will automatically:
- Find the oldest unassigned issue
- Identify the 5 most recent contributors from merged PRs
- Match a contributor to the issue based on relevance
- Assign the issue and add a friendly explanatory comment

You can edit it to customize assignment criteria, contributor matching logic, or exclusion labels.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Open issues and their assignees
- Recent merged pull requests and their authors
- Issue labels and metadata
- Repository contributor activity

## What it writes to GitHub

- Issue assignments to contributors
- Brief comments explaining the assignment rationale

## How it works

1. **Find Candidate Issue**: Searches for the oldest open issue that:
   - Has no assignees
   - Doesn't have `ai-generated` or `no-bot` labels
   - Wasn't opened by a bot account

2. **Identify Contributors**: Lists the 5 most recent contributors from merged pull requests

3. **Match and Assign**: Selects a contributor whose recent work seems relevant to the issue type

4. **Notify**: Adds a friendly comment explaining why this contributor was chosen

The workflow assigns only one issue per run to avoid overwhelming contributors. It runs daily by default but can be triggered manually.

## When to use this workflow

This workflow is valuable when:
- You have many unassigned issues accumulating
- You want to distribute work fairly among contributors
- You need help matching issues to the right contributors
- You want to ensure issues get attention from relevant team members

## Customization options

You can customize the workflow to:
- Add more exclusion labels (e.g., `awaiting-triage`, `blocked`)
- Adjust the number of recent contributors to consider
- Change the matching logic for contributor selection
- Modify the assignment frequency (daily, weekly, etc.)
- Add specific criteria for different issue types

## Tips

- Consider adding exclusion labels for issues that need maintainer attention first
- Monitor the assignments to ensure good matches are being made
- Adjust the matching logic based on your repository's contribution patterns
- Use this in combination with issue triage workflows for best results
