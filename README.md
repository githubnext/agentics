# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://github.github.com/gh-aw/).

## 📂 Available Workflows

### Triage Workflows

- [🏷️ Issue Triage](docs/issue-triage.md) - Triage issues and pull requests

## Fault Analysis Workflows

- [🏥 CI Doctor](docs/ci-doctor.md) - Monitor CI workflows and investigate failures automatically

## Code Review Workflows

- [✅ Contribution Guidelines Checker](docs/contribution-guidelines-checker.md) - Review pull requests for compliance with contribution guidelines

### Research, Status & Planning Workflows

- [📚 Weekly Research](docs/weekly-research.md) - Collect research updates and industry trends
- [👥 Daily Repo Status](docs/daily-repo-status.md) - Assess repository activity and create status reports
- [👥 Daily Team Status](docs/daily-team-status.md) - Create upbeat daily team activity summaries with productivity insights
- [📋 Daily Plan](docs/daily-plan.md) - Update planning issues for team coordination

### Dependency Management Workflows

- [📦 Dependabot PR Bundler](docs/dependabot-pr-bundler.md) - Create pull requests to bundle together as many dependabot updates as possible
- [📦 Dependabot Issue Bundler](docs/dependabot-issue-bundler.md) - Create issues that group together dependabot updates related to the same ecosystem

### Command-Triggered Agentic Workflows

These workflows are triggered by specific "/" commands in issue or pull request comments, allowing for on-demand agentic assistance. Only maintainers or those with write access can trigger these workflows by commenting with the appropriate command.

- [📋 Plan Command](docs/plan.md) - Break down issues into actionable sub-tasks with /plan command
- [🏥 PR Fix](docs/pr-fix.md) - Analyze failing CI checks and implement fixes for pull requests
- [🔍 Repo Ask](docs/repo-ask.md) - Intelligent research assistant for repository questions and analysis

### Code Improvement Workflows (by analysis, producing report)

These workflows analyze the repository, code, and activity to produce reports, insights, and recommendations for improvements. They do not make any changes to the codebase directly but can be used as input for maintainers to take action.

You can use the "/plan" agent to turn the reports into actionable issues which can then be assigned to the appropriate team members or agents.

- [🔍 Daily Accessibility Review](docs/daily-accessibility-review.md) - Review application accessibility by automatically running and using the application
- [🔎 Daily Adhoc QA](docs/daily-qa.md) - Perform adhoc explorative quality assurance tasks

### Code Improvement Workflows (by making changes, producing pull requests)

- [📖 Regular Documentation Update](docs/update-docs.md) - Update documentation automatically
- [📖 Daily Documentation Updater](docs/daily-doc-updater.md) - Automatically update documentation based on recent code changes and merged PRs
- [✨ Code Simplifier](docs/code-simplifier.md) - Automatically simplify recently modified code for improved clarity and maintainability
- [⚡ Daily Progress](docs/daily-progress.md) - Automated daily feature development following a structured roadmap
- [🧪 Daily Test Coverage Improver](docs/daily-test-improver.md) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Performance Improver](docs/daily-perf-improver.md) - Analyze and improve code performance through benchmarking and optimization
- [🔥 Daily Backlog Burner](docs/daily-backlog-burner.md) - Systematically manage and reduce backlog through strategic cleanup

## Meta-Workflows

- [🔧 Q - Workflow Optimizer](docs/q.md) - Expert system that analyzes and optimizes agentic workflows

## 🔄 Updating Workflows

Keep your agentic workflows up to date with the latest features and improvements:

```bash
gh extensions upgrade github/gh-aw # Update cli extension
gh aw upgrade  # Upgrade to latest gh aw engine version
gh aw update   # Update added workflows
```

This automatically updates agent files, applies codemods, updates actions versions, and recompiles all workflows.

📖 [Learn more about GitHub Agentic Workflows](https://github.github.io/gh-aw/)

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
