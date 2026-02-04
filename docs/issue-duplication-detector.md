# 🔄 Issue Duplication Detector

> For an overview of all available workflows, see the [main README](../README.md).

The [Issue Duplication Detector workflow](../.github/workflows/issue-duplication-detector.md?plain=1) automatically detects duplicate issues in the repository. It runs every 5 minutes to batch-process recently created or updated issues, analyzing them against existing issues to find potential duplicates.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the Issue Duplication Detector workflow to your repository
gh aw add githubnext/agentics/issue-duplication-detector
```

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Issues in the fork settings

## Configuration

This workflow requires no configuration and works out of the box. The workflow runs on a schedule (every 5 minutes) and via manual dispatch.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Recently created or updated issues (within the last 10 minutes)
- Issue titles, bodies, and metadata
- Existing open and closed issues for comparison
- Repository information for context

## What it creates

- Comments on issues that appear to be duplicates (via safe-outputs)
- Includes links to potential duplicate issues
- Provides suggested next steps for issue authors
- Uses `read-all` permissions with safe-outputs for controlled comment creation

## What web searches it performs

- This workflow does not perform web searches
- All analysis is done using GitHub issue data

## Human in the loop

- Review duplicate detection comments for accuracy
- Validate that flagged issues are truly duplicates
- Close confirmed duplicate issues when appropriate
- Override false positive detections if needed
- Monitor detection accuracy over time
- Disable or uninstall the workflow if duplicate detection is not helpful

## Activity duration

- This workflow runs on a schedule every 5 minutes
- It will continue running until disabled or removed from the repository
