# GitHub Agentic Workflows (Samples)

More information about the format at https://github.com/githubnext/gh-aw

To install, first install the `gh-aw` extension:

```bash 
gh extension install githubnext/gh-aw
```

Then install one or more workflows from this repository as described below.

## Weekly Researcher

This workflow will run weekly to collect research updates from the team and post them to a new issue in the repository.

```bash
gh aw add weekly-research -r githubnext/agentics
git commit -m "Add weekly-research workflow"
git push
```

## Daily Team Status

This workflow will run daily to collect team status updates and post them to a designated channel.

```bash
gh aw add daily-team-status -r githubnext/agentics
git commit -m "Add daily-team-status workflow"
git push
```

> NOTE: When run, this workflow will create an issue with the status report.

## Daily Dependency Updater

This workflow will run daily to check for dependency updates and try to create one combined pull request for all updates.

```bash
gh aw add daily-dependency-updates -r githubnext/agentics
```

Now edit the workflow to add the typical Bash commands needed to build and test the project.

```bash
code .github/workflows/daily-dependency-updates.md
```

Now update:

```bash
gh aw compile
```

Now commit the changes:

```bash
git commit -m "Add dependency-updater workflow"
git push
```

> NOTE: When run, this workflow will edit files in the checked-out repository (e.g. in a GitHub Actions workflow run), and create a pull request with the changes. It may also search the web for information.

## Daily QA 

This workflow will run daily to perform adhoc QA tasks, e.g. check that the code builds and runs, and that the tests pass.

```bash
gh aw add daily-qa -r githubnext/agentics
```

Now follow the same steps as for the dependency updater to edit the workflow to add the Bash commands needed to build and test the project.

> NOTE: When run, this workflow will edit files in the checked-out repository (e.g. in a GitHub Actions workflow run), and create a pull request with the changes. It may also search the web for information.

## Issue Triage

This workflow will run daily to triage issues and pull requests, and assign them to the appropriate team members.

```bash
gh aw add issue-triage -r githubnext/agentics
```

Now follow the same steps as for the dependency updater to edit the workflow to add the Bash commands needed to build and test the project.

> NOTE: When run, this workflow will edit files in the checked-out repository (e.g. in a GitHub Actions workflow run), and create a pull request with the changes. It may also search the web for information.

## Daily Plan

This workflow will run daily to update a planning issue for the team.

```bash
gh aw add project-plan -r githubnext/agentics
git commit -m "Add project-plan workflow"
git push
```

> NOTE: When run, this workflow will create issues and add comments to existing issues. It may also search the web for information.

## Solve Issues

This workflow will run every 3 hours to solve issues in the repository.

```bash
gh aw add solve-issues -r githubnext/agentics
```

Now edit the workflow to add the typical Bash commands needed to build and test the project.

```bash
code .github/workflows/solve-issues.md
```

Now update:

```bash
gh aw compile
```
Now commit the changes:

```bash
git commit -m "Add solve-issues workflow"
```

## Solving Security Alerts

This workflow will run daily to check for security alerts and try to create pull requests for them.

```bash
Add the workflow:

```bash
gh aw add daily-security-issues -r githubnext/agentics
```

Now edit the workflow to add the typical Bash commands needed to build and test the project.

```bash
code .github/workflows/daily-security-issues.md
```

Now update:

```bash
gh aw compile
```

Now commit the changes:

```bash
git commit -m "Add security-issues workflow"
```

## Documentation Update

This workflow will run on each push to main to try to update documentation in the repository.

```bash
gh aw add update-docs -r githubnext/agentics
git commit -m "Add update-docs workflow"
```
