# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://github.com/githubnext/gh-aw?tab=readme-ov-file).

> [!WARNING]
> GitHub Agentic Workflows are a research demonstrator, and these workflows are samples only.

## 📂 Available Workflows

### Research & Planning Workflows
- [📚 Weekly Research](docs/weekly-research.md) - Collect research updates and industry trends
- [👥 Daily Team Status](docs/daily-team-status.md) - Assess repository activity and create status reports
- [📋 Daily Plan](docs/daily-plan.md) - Update planning issues for team coordination
- [🏷️ Issue Triage](docs/issue-triage.md) - Triage issues and pull requests

### Coding & Development Workflows
- [🏥 CI Doctor](docs/ci-doctor.md) - Monitor CI workflows and investigate failures automatically
- [📦 Daily Dependency Updater](docs/daily-dependency-updates.md) - Update dependencies and create pull requests
- [📖 Regular Documentation Update](docs/update-docs.md) - Update documentation automatically
- [🔍 Daily Adhoc QA](docs/daily-qa.md) - Perform "soft", explorative quality assurance tasks
- [🧪 Daily Test Coverage Improver](docs/daily-test-improver.md) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Performance Improver](docs/daily-perf-improver.md) - Analyze and improve code performance through benchmarking and optimization
- [🔍 Daily Accessibility Review](docs/daily-accessibility-review.md) - Review application accessibility by automatically running and using the application

## 💻 Coding Tasks Warning

The workflows that help with coding tasks should be installed with caution and used only experimentally, then disabled. While the tasks are executed within GitHub Actions and are relatively sandboxed, they still operate in an environment where outward network requests are allowed and egress is possible. You will need to configure additional `Bash` commands to build and test your project by editing the markdown workflow file to add those commands and then running `gh aw compile` to update the workflow. The workflows will attempt to "self-report" the commands they need to run, so you can look at the initial reports to see what commands are needed.

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
