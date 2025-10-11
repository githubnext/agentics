# 📦 Daily Dependency Updater

> For an overview of all available workflows, see the [main README](../README.md).

The [daily dependency updater workflow](../workflows/daily-dependency-updates.md?plain=1) will check for Dependabot alerts in the repository and update dependencies to the latest versions, creating pull requests as necessary.

## Installation

```bash
# Install the 'gh aw' extension
gh aw extension install githubnext/agentics

# Add the Daily Dependency Updater workflow to your repository
gh aw add githubnext/agentics/daily-dependency-updates --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-dependency-updates
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

This workflow requires no configuration and works out of the box. You can use local configuation to specify dependency management tools (npm, pip, maven, etc.), customize dependency update strategies and version constraints, onfigure which dependencies to include/exclude from automated updates. Local configuration can be done in `.github/workflows/agentics/daily-dependency-updates.config.md`.



After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and dependency files
- Issues and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information
- Security events and Dependabot alerts

## What it creates

- Creates pull requests with dependency updates
- Creates new branches for the dependency changes
- Makes file changes to update dependency versions
- Requires `contents: write` and `pull-requests: write` permissions

## Human in the loop

- Review dependency update pull requests for breaking changes
- Test updated dependencies to ensure compatibility
- Merge approved pull requests after validation
- Monitor for any issues after dependency updates are deployed
- Disable or uninstall the workflow if dependency updates cause more problems than benefits

## Activity duration

- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

