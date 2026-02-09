# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://github.github.com/gh-aw/).

## 📂 Available Workflows

### Depth Triage & Analysis Workflows

- [🏷️ Issue Triage](docs/issue-triage.md) - Triage issues and pull requests
- [🏥 CI Doctor](docs/ci-doctor.md) - Monitor CI workflows and investigate failures automatically
- [🔍 Repo Ask](docs/repo-ask.md) - Intelligent research assistant for repository questions and analysis
- [🔍 Daily Accessibility Review](docs/daily-accessibility-review.md) - Review application accessibility by automatically running and using the application
- [🔧 Q - Workflow Optimizer](docs/q.md) - Expert system that analyzes and optimizes agentic workflows

### Research, Status & Planning Workflows

- [📚 Weekly Research](docs/weekly-research.md) - Collect research updates and industry trends
- [👥 Daily Repo Status](docs/daily-repo-status.md) - Assess repository activity and create status reports
- [📋 Daily Plan](docs/daily-plan.md) - Update planning issues for team coordination
- [📋 Plan Command](docs/plan.md) - Break down issues into actionable sub-tasks with /plan command

### Coding & Development Workflows

- [⚡ Daily Progress](docs/daily-progress.md) - Automated daily feature development following a structured roadmap
- [📦 Daily Dependency Updater](docs/daily-dependency-updates.md) - Update dependencies and create pull requests
- [📖 Regular Documentation Update](docs/update-docs.md) - Update documentation automatically
- [🏥 PR Fix](docs/pr-fix.md) - Analyze failing CI checks and implement fixes for pull requests
- [🔎 Daily Adhoc QA](docs/daily-qa.md) - Perform adhoc explorative quality assurance tasks
- [🧪 Daily Test Coverage Improver](docs/daily-test-improver.md) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Performance Improver](docs/daily-perf-improver.md) - Analyze and improve code performance through benchmarking and optimization

## 🔄 Updating Workflows

Keep your agentic workflows up to date with the latest features and improvements:

### Using the CLI

Upgrade the AW engine version and update your workflows:

```bash
gh extensions upgrade github/gh-aw # Update cli extensiô
gh aw upgrade  # Upgrade to latest gh aw engine version
gh aw update   # Update added workflows
```

This automatically updates agent files, applies codemods, updates actions versions, and recompiles all workflows.

### Using the Agentic Workflows Agent

Alternatively, you can prompt the agentic-workflows agent to update your workflows:

```
/agent agentic-workflows upgrade all workflows to the latest version
```

Or update individual workflows:

```
/agent agentic-workflows update the issue-triage workflow
```

📖 [Learn more about GitHub Agentic Workflows](https://github.github.io/gh-aw/)

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
