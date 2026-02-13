# 📈 Daily Progress

> For an overview of all available workflows, see the [main README](../README.md).

The [daily progress workflow](../workflows/daily-progress.md?plain=1) is an automated workflow that runs daily (Monday through Friday at 2am UTC) to work systematically on your repository's feature roadmap. This workflow acts as an autonomous developer that researches project goals, creates development plans, and implements features through a structured multi-step process.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-progress
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-progress
```

## Configuration

The workflow will self-configure to create a build configuration file at `.github/actions/daily-progress/build-steps/action.yml` to set up the development environment for feature work.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## How it Works

The Daily Progress workflow follows a systematic 7-step process:

### 1. Roadmap Research
- Searches for an existing roadmap issue titled "Daily Roadmap Progress: Research, Roadmap and Plan"
- If no roadmap exists, conducts comprehensive research into the project's goals, features, and target audience
- Analyzes existing documentation, issues, pull requests, and project files
- Creates a detailed roadmap issue with development priorities

### 2. Build Configuration Setup
- Checks for `.github/actions/daily-progress/build-steps/action.yml`
- If missing, researches typical build/setup steps for the project
- Creates the build configuration file and submits a pull request
- Ensures the repository is properly configured for automated development work

### 3. Goal Selection
- Reads the project roadmap and any maintainer feedback
- Reviews existing pull requests to avoid conflicts
- Selects an appropriate goal from the roadmap to work on
- Updates the roadmap if it needs refreshing

### 4. Feature Development
- Creates a new branch for the selected goal
- Implements code changes to work toward the goal
- Ensures existing tests pass and adds new tests when appropriate
- Applies code formatting and linting standards

### 5. Pull Request Creation
- Creates a draft pull request with the implemented changes
- Provides detailed description of what was done and why
- Ensures no unwanted files are included in the PR
- Links back to the roadmap issue

### 6. Issue Reporting
- If development fails, creates an issue summarizing the problems encountered
- Provides context for future development attempts

### 7. Communication
- Updates the roadmap issue with progress information
- Links to created pull requests or issues
- Seeks clarification if unexpected failures occur

## What it reads from GitHub

- Repository contents and file structure
- Existing issues and pull requests
- Project documentation and configuration files
- Actions workflow runs and CI/CD configurations
- Development container configurations
- Project boards and roadmaps

## What it creates

- **Planning Issues**: Creates roadmap and research issues for project direction
- **Configuration Pull Requests**: Adds build and setup configurations
- **Feature Pull Requests**: Implements new features and improvements as draft PRs
- **Progress Issues**: Reports on development challenges or failures
- **Issue Comments**: Updates roadmap issues with progress information
- Requires `issues: write` and `pull-requests: write` permissions

## What web searches it performs

- Researches project roadmap information and feature development best practices
- Looks up documentation for technologies used in the project
- Searches for implementation patterns and code examples
- May research industry trends relevant to the project goals

## What bash commands it runs

- Repository analysis and exploration commands
- Build and test commands to ensure code quality
- Code formatting and linting tools
- Git operations for branch management and commits
- Package management commands (npm, pip, etc.)
- Any commands needed for feature development and validation

## Use Cases

- **Continuous Feature Development**: Automatically work on project roadmap items daily
- **Technical Debt Reduction**: Systematically improve code quality and documentation
- **Research and Planning**: Maintain up-to-date project roadmaps and development plans
- **Automated Maintenance**: Regular updates, dependency management, and improvements
- **Proof of Concept Development**: Explore new features and implementation approaches

## Monitoring and Control

- **Draft Pull Requests**: All feature changes are created as draft PRs for human review
- **Roadmap Issues**: Central tracking of project goals and progress
- **Scheduled Execution**: Runs only on weekdays to respect team schedules
- **Safe Outputs**: Controlled limits on issues and PRs created

## Human in the loop

- Review and approve all draft pull requests created by the workflow
- Provide feedback on roadmap issues to guide development priorities  
- Monitor progress and adjust goals based on changing project needs
- Validate that automated changes align with project standards and goals
- Merge approved pull requests and close completed roadmap items