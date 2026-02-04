# 🔍 Issue Duplication Detector

> For an overview of all available workflows, see the [main README](../README.md).

The [issue duplication detector workflow](../workflows/issue-duplication-detector.md?plain=1) runs every 6 hours to detect duplicate issues in the repository and suggest next steps.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Issue Duplication Detector workflow to your repository
gh aw add githubnext/agentics/issue-duplication-detector
```

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can manually trigger this workflow using `gh aw run issue-duplication-detector` or wait for it to run automatically on its 6-hour schedule.

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. The workflow uses intelligent semantic analysis to detect duplicate issues by comparing titles, descriptions, and content.

### How It Works

The workflow operates on a 6-hour batch schedule:

1. **Searches for recent issues**: Queries for issues created or updated in the last 6 hours
2. **Analyzes each issue**: Extracts key information from the issue title and body
3. **Searches for duplicates**: Uses GitHub search with keywords to find similar existing issues
4. **Compares semantically**: Analyzes whether issues describe the same underlying problem or request
5. **Posts helpful comments**: If duplicates are found, adds a polite comment with:
   - Links to potential duplicate issues
   - Explanation of why they appear to be duplicates
   - Suggested next steps for the issue author

### Batch Processing & Cost Control

- Runs every 6 hours to batch-process multiple issues in a single workflow run
- Only comments when high-confidence duplicates are found
- Maximum 10 comments per run to prevent excessive API usage
- 15-minute timeout ensures predictable runtime costs

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Recently created or updated issues (last 6 hours)
- Full issue details including title, body, and metadata
- Repository issue history for duplicate detection
- Both open and closed issues for comprehensive analysis

## What it creates

- Adds comments to issues that appear to be duplicates
- Comments include links to potential duplicates and suggested next steps
- Requires `issues: write` permission

## What web searches it performs

- Does not perform web searches; operates entirely within GitHub data

## Human in the loop

- Review duplicate detection comments for accuracy
- Verify that flagged issues are truly duplicates
- Close duplicate issues or provide clarification if the detection was incorrect
- Add any missing context to the original issue if the duplicate has valuable additional information
- Monitor false positives and disable the workflow if accuracy is not acceptable

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering.
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## Example Output

When a duplicate is detected, the workflow posts a comment like:

```markdown
👋 Hi! It looks like this issue might be a duplicate of existing issue(s):

- #123 - Add support for custom templates

Both issues describe the need for customizable templates in the project configuration.

**Suggested next steps:**
- Review issue #123 to see if it addresses your concern
- If this issue has additional context not covered in #123, consider adding it there
- If they are indeed the same, this issue can be closed as a duplicate

Let us know if you think this assessment is incorrect!
```
