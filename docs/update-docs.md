# 📖 Regular Documentation Update

> For an overview of all available workflows, see the [main README](../README.md).

The [update documentation workflow](../workflows/update-docs.md?plain=1) will run on each push to main to try to update documentation in the repository. It defaults to using [Astro Starlight] (https://starlight.astro.build) for documentation generation, but you can edit it to use other frameworks if necessary.

## Installation

```bash
gh aw add update-docs -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run update-docs
```

**Checklist**

* [ ] See notes on coding tasks in the [main README](../README.md). 

* [ ] Enable "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] Recommend enabling  "Always suggest updating pull request branches" in the repository settings

* [ ] If in a fork, enable "GitHub Actions" and "GitHub Issues" in the fork project settings

* [ ] When a pull request is created, you must review the changes carefully. 

* [ ] Understand that your GitHub Actions runs will **not** trigger on pull requests created by this workflow, or indeed any Actions-created PRs. You must open/close the PR or push a new commit to trigger CI checks. This is not indicated in the GitHub UI. It's just something you need to be aware of.


## Configuration

- Benefits from configuring build steps for documentation generation
- Edit the workflow to specify your documentation framework (Astro Starlight, MkDocs, etc.)
- Customize documentation structure, themes, and generation commands
- Add project-specific documentation validation and deployment steps
- Configure which files and directories to include in documentation updates
- After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and source code
- Issues and their metadata
- Actions workflow runs and results
- Checks and status information

## What it creates

- Creates pull requests with documentation updates
- Creates new branches for the documentation changes
- Makes file changes to update or add documentation
- Requires `contents: write` and `pull-requests: write` permissions

## What web searches it performs

- Searches for information to help improve documentation
- May look up best practices, examples, or technical references

## Human in the loop

- Review documentation update pull requests for accuracy and clarity
- Validate that documentation changes reflect actual code behavior
- Edit and improve AI-generated documentation before merging
- Test documentation examples and instructions for correctness
- Disable or uninstall the workflow if documentation updates are not improving quality

## Activity duration

- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

