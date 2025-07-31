# GitHub Agentic Workflows (Samples)

More information about the format at https://github.com/githubnext/gh-aw

To install, first install the `gh-aw` extension:

```bash 
gh extension install githubnext/gh-aw
```

Then install one or more workflows from this repository as described below.

## Weekly Researcher

The [weekly researcher workflow](workflows/weekly-research.md?plain=1) will run each Monday morning to collect research updates from the team and post them to a new issue in the repository.

```bash
gh aw add weekly-research -r githubnext/agentics
git commit -m "Add weekly-research workflow"
git push
```

> NOTE: When run, this workflow will create an issue with the research report.

## Daily Team Status

The [daily team status workflow](workflows/daily-team-status.md?plain=1) will run daily to collect status updates from the team and post them to a designated channel.

```bash
gh aw add daily-team-status -r githubnext/agentics
git commit -m "Add daily-team-status workflow"
git push
```

> NOTE: When run, this workflow will create an issue with the status report.

## Daily Plan

The [daily plan workflow](workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team.

```bash
gh aw add project-plan -r githubnext/agentics
git commit -m "Add project-plan workflow"
git push # or create a pull request
```

> NOTE: When run, this workflow will create an issue with the project plan. It will also search the web for information to help with the planning.

## Issue Triage

The [issue triage workflow](workflows/issue-triage.md?plain=1) will run daily to triage issues and pull requests in the repository.

```bash
gh aw add issue-triage -r githubnext/agentics
git commit -m "Add issue-triage workflow"
git push # or create a pull request
```

> NOTE: When run, this workflow will add an issue comment to your issue. It may also search the web for information.

## Coding Tasks

The samples in this repo include workflows that can help with coding tasks, such as solving issues, updating documentation, and performing QA tasks.

⚠️⚠️ Coding tasks should be installed with caution. While the tasks are executed within GitHub Actions, and are relatively sandboxed, they still operate in an environment where outward network requests are allowed. Also, you will require you to configure additional `Bash` commands to build and test your project. You will need to edit the workflow file to add those commands and then run `gh aw compile` to update the workflow. The worfklows below will attempt to "self-report" the commands they need to run, so you can look at the initial reports to see what commands are needed.

### Daily Dependency Updater

The [daily dependency updater workflow](workflows/daily-dependency-updates.md?plain=1) will run daily to check for Dependabot alerts in the repository and update dependencies to the latest versions, creating pull requests as necessary.

```bash
gh aw add daily-dependency-updates -r githubnext/agentics
git commit -m "Add dependency-updater workflow"
git push # or create a pull request
```

See notes above on coding tasks.  **You will need to configure additional Bash commands to build and test your project.** 

### Daily QA 

The [daily QA workflow](workflows/daily-qa.md?plain=1) will run daily to perform quality assurance tasks in the repository, such as following the instructions in the README.md to check that the code builds and runs, and that the tests pass.

```bash
gh aw add daily-qa -r githubnext/agentics
git commit -m "Add daily-qa workflow"
git push # or create a pull request
```

See notes above on coding tasks.  **You will need to configure additional Bash commands to build and test your project.** 

### Solve Issues

The [solve issues workflow](workflows/solve-issues.md?plain=1) will run every 3 hours to solve issues in the repository. It will look for issues labelled with the workflow name and attempt to solve them by creating pull requests with the changes.

```bash
gh aw add solve-issues -r githubnext/agentics
git commit -m "Add solve-issues workflow"
git push # or create a pull request
```

See notes above on coding tasks.  **You will need to configure additional Bash commands to build and test your project.** 

### Solving Security Alerts

The [daily security issues workflow](workflows/daily-security-issues.md?plain=1) will run daily to check for existing security alerts from code scanning in the repository and attempt to create pull requests for them.

```bash
Add the workflow:
gh aw add daily-security-issues -r githubnext/agentics
git commit -m "Add security-issues workflow"
git push # or create a pull request
```

See notes above on coding tasks.  **You will need to configure additional Bash commands to build and test your project.** 

## Documentation Update

The [update documentation workflow](workflows/update-docs.md?plain=1) will run on each push to main to try to update documentation in the repository.

```bash
gh aw add update-docs -r githubnext/agentics
git commit -m "Add update-docs workflow"
```

See notes above on coding tasks.  **You will need to configure additional Bash commands to build and test your project.** 
