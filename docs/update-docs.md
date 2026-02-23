# 📖 Regular Documentation Update

> For an overview of all available workflows, see the [main README](../README.md).

The [update documentation workflow](../workflows/update-docs.md?plain=1) will run on each push to main to try to update documentation in the repository. It defaults to using [Astro Starlight](https://starlight.astro.build) for documentation generation, but you can edit it to use other frameworks if necessary.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/update-docs
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run update-docs
```

## How It Works

````mermaid
graph LR
    A[Push to Main] --> B[Analyze Changes]
    B --> C[Generate Docs]
    C --> D{Updates Needed?}
    D -->|Yes| E[Create Doc Branch]
    E --> F[Create PR]
    D -->|No| G[Report: Docs Current]
````

## Configuration

This workflow requires no configuration and works out of the box. You can configure documentation frameworks, documentation structure, themes, files, directories by editing the workflow file.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and source code
- Issues and their metadata
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates pull requests with documentation updates
- Creates new branches for the documentation changes
- Makes file changes to update or add documentation

## Triggering CI on Pull Requests

By default, pull requests created by this workflow do not trigger CI workflow runs. This is a GitHub Actions feature to prevent event cascades.

To trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

## What web searches it performs

- Searches for information to help improve documentation
- May look up best practices, examples, or technical references

## Human in the loop

- Review documentation update pull requests for accuracy and clarity
- Validate that documentation changes reflect actual code behavior
- Edit and improve AI-generated documentation before merging
- Test documentation examples and instructions for correctness
- Disable or uninstall the workflow if documentation updates are not improving quality

