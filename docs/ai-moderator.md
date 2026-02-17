# 🛡️ AI Moderator

> For an overview of all available workflows, see the [main README](../README.md).

The [AI Moderator workflow](../workflows/ai-moderator.md?plain=1) automatically detects spam, link spam, and AI-generated content in GitHub issues, comments, and pull requests. This workflow helps maintain quality discussions and protect your repository from malicious or low-quality contributions.

## Installation

````bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/ai-moderator
````

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

You can't start a run of this workflow directly as it is triggered automatically when issues, comments, or pull requests are created.

## Configuration

This workflow works out of the box with sensible defaults. You can customize:

- The labels to apply for different detection types (spam, link-spam, ai-generated, ai-inspected)
- The user roles that are skipped (defaults to admins, maintainers, write access, and triage)
- The bots to skip (defaults to github-actions and copilot)
- Rate limiting settings to control how often the workflow runs
- Detection criteria and thresholds in the workflow prompt

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- New issues and their content
- Comments on issues and pull requests
- Pull request diffs and file changes
- Repository context to evaluate content relevance
- User information and roles

## What it creates

- Adds labels to issues and pull requests (`spam`, `link-spam`, `ai-generated`, or `ai-inspected`)
- Hides comments that are detected as spam
- Requires `issues: write` and `pull-requests: write` permissions (note: the workflow is configured with read-only by default, so you'll need to adjust permissions if you want it to take action)

## What web searches it performs

This workflow does not perform web searches.

## Human in the loop

- Review labels applied to ensure accurate spam detection
- Monitor for false positives and adjust detection criteria if needed
- Override moderation decisions when the AI makes mistakes
- Validate hidden comments and unhide legitimate content if necessary
- Adjust the workflow configuration based on your repository's needs
- Consider exempting trusted contributors from moderation if desired
- Disable or uninstall the workflow if moderation automation is not providing value
