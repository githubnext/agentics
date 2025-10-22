# 🔧 Maintainer Workflow

> For an overview of all available workflows, see the [main README](../README.md).

The [maintainer workflow](../workflows/maintainer.md?plain=1) helps keep your agentic workflows up to date by automatically upgrading them to the latest version of gh-aw. It fetches the latest changes from the gh-aw repository, attempts to recompile all workflows, and either creates a pull request with the updates or an issue if compilation errors occur.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install githubnext/gh-aw

# Add the Maintainer workflow to your repository
gh aw add githubnext/agentics/maintainer --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run maintainer
```

**Mandatory Checklist**

* [ ] I am a repository admin or have sufficient permissions, and am happy for the safe-outputs portion of this workflow to create pull requests or issues in the repository.

* [ ] I have enabled "Allow GitHub Actions to create and approve pull requests" in the repository settings under "Actions > General"

* [ ] If in a fork, I have enabled "GitHub Actions" and "GitHub Issues" in the fork repository settings

* [ ] I will review all pull requests very carefully and monitor the repository.

## What it does

1. **Fetches latest gh-aw changes**: Retrieves the CHANGELOG.md or release notes from the `githubnext/gh-aw` repository to understand new features, breaking changes, and migration instructions.

2. **Installs latest gh-aw**: Upgrades the gh-aw CLI extension to the latest version using the GitHub token.

3. **Attempts recompilation**: Tries to recompile all workflows in the `workflows/` directory with the new gh-aw version.

4. **Fixes compilation errors**: If errors occur, analyzes them using the changelog and documentation, then attempts to fix the workflow files.

5. **Creates outputs**:
   - **Success**: Creates a pull request with upgraded workflows and any necessary fixes
   - **Failure**: Creates an issue documenting the compilation errors and attempted fixes

## Configuration

This workflow requires no configuration and works out of the box. It will process all workflow markdown files in the `workflows/` directory.

## What it reads from GitHub

- Repository contents and workflow files
- CHANGELOG.md from the `githubnext/gh-aw` repository
- Release information and documentation from gh-aw

## What it creates

- Creates pull requests with upgraded workflows (if successful)
- Creates issues documenting upgrade failures (if compilation errors persist)
- Makes file changes to workflow files to fix compatibility issues
- May generate `.lock.yml` files during compilation
- Requires `contents: write`, `pull-requests: write`, and `issues: write` permissions

## Human in the loop

- Review pull requests created by this workflow to understand what changed
- Test the upgraded workflows before merging
- Investigate issues created by the workflow if compilation fails
- Manually fix complex migration issues that the workflow couldn't handle
- Disable or uninstall the workflow if not needed regularly

## When to run

- Run this workflow when you know a new version of gh-aw has been released
- Run it periodically (e.g., monthly) to stay up to date
- Run it before making other workflow changes to ensure compatibility
- Trigger manually via workflow_dispatch when needed

## Troubleshooting

If the workflow creates an issue instead of a PR:
1. Review the issue to understand what compilation errors occurred
2. Check the gh-aw changelog for migration instructions
3. Manually update the affected workflows based on the guidance
4. Re-run the maintainer workflow to verify the fixes work
