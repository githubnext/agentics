# GitHub Agentic Workflows (Samples)

More information about the format at https://github.com/githubnext/gh-aw

To install, first install the `gh-aw` extension:

```bash 
gh extension install githubnext/gh-aw
```

Then install the pack of agentic workflows:
```bash
gh aw install githubnext/agentics
```

## Weekly Researcher

This workflow will run weekly to collect research updates from the team and post them to a new issue in the repository.

```bash
gh aw add weekly-research-report
git commit -a -m "Add weekly-research-report workflow"
```

## Dependency Updater

This workflow will run daily to check for dependency updates and try to create one combined pull request for all updates.

```bash
Add the workflow:

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
git commit -a -m "Add dependency-updater workflow"
```

## Daily QA 

This workflow will run daily to perform adhoc QA tasks, e.g. check that the code builds and runs, and that the tests pass.

```bash
gh aw add daily-qa -r githubnext/agentics
```

Now follow the same steps as for the dependency updater to edit the workflow to add the Bash commands needed to build and test the project.

## Issue Triage

This workflow will run daily to triage issues and pull requests, and assign them to the appropriate team members.

```bash
gh aw add issue-triage -r githubnext/agentics
```

Now follow the same steps as for the dependency updater to edit the workflow to add the Bash commands needed to build and test the project.

## Daily Plan

This workflow will run daily to update a planning issue for the team.

```bash
gh aw add daily-plan -r githubnext/agentics
git commit -a -m "Add daily-plan workflow"
```

## Daily Team Status

This workflow will run daily to collect team status updates and post them to a designated channel.

```bash
gh aw add daily-team-status -r githubnext/agentics
git commit -a -m "Add daily-team-status workflow"
```

## Issue Solver

This workflow will run every 3 hours to solve issues in the repository.

```bash
gh aw add regular-solve-issue -r githubnext/agentics
git commit -a -m "Add issue-solver workflow"
```

## Security Alerts

This workflow will run daily to check for security alerts and try to create pull request for them.

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
git commit -a -m "Add security-issues workflow"
```

