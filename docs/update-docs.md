# 📖 Regular Documentation Update

> For an overview of all available workflows, see the [main README](../README.md).

The [update documentation workflow](../workflows/update-docs.md?plain=1) will run on each push to main to try to update documentation in the repository. It defaults to using [Astro Starlight] (https://starlight.astro.build) for documentation generation, but you can edit it to use other frameworks if necessary.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install githubnext/gh-aw

# Add the Update Docs workflow to your repository
gh aw add githubnext/agentics/update-docs --pr
```

This creates a pull request to add the workflow to your repository.

You must also add [choose a coding agent](https://githubnext.github.io/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run update-docs
```

❗IMPORTANT: GitHub Actions runs will **not** trigger on commits pushed by this workflow and will **not** tell you that CI has not been run unless you have enabled a specific custom check for this condition. **You must open/close the PR or hit "Update branch" if offered to trigger CI.Yes it's painful and yes it's just something you need to be aware of.

**Mandatory Checklist**

* [ ] I have read the notes on coding tasks in the [main README](../README.md) and understand the implications.

* [ ] I am a repository admin or have sufficient permissions, and am happy for the safe-outputs portion of this workflow to push new branches to the repository.

* [ ] I have enabled "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] I have considered enabling "Always suggest updating pull request branches" in the repository settings

* [ ] If in a fork, I have enabled "GitHub Actions" and "GitHub Issues" in the fork repository settings

* [ ] I will review all pull requests very carefully, and carefully monitor the repository. 

* [ ] I will operate this demonstrator for a time-limited period only (the default is 48h). 

* [ ] I understand that GitHub Actions runs will **not** trigger on pull requests created by this workflow, see above.

## Configuration

This workflow requires no configuration and works out of the box. You can use local configuration to configure documentation frameworks, documentation structure, themes, files, directories. Local configuration can be done in `.github/workflows/agentics/update-docs.config.md`.



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

