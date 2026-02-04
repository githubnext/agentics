# ✅ PR Contribution Guidelines Checker

> For an overview of all available workflows, see the [main README](../README.md).

The [PR contribution guidelines checker workflow](../.github/workflows/pr-contribution-checker.md?plain=1) automatically reviews incoming pull requests to ensure they meet the contribution guidelines for your repository.

## What it does

When a pull request is opened, synchronized, or reopened, this workflow:

1. **Checks for contribution guidelines** - Looks for CONTRIBUTING.md or similar files in your repository
2. **Reviews the PR** - Examines the PR title, description, files changed, and code changes
3. **Evaluates compliance** - Checks if the PR meets contribution guidelines such as:
   - Clear PR title and description
   - References to related issues
   - Tests for new features
   - Updated documentation
   - Appropriate file organization
   - Reasonable PR size
4. **Takes action**:
   - **If compliant**: Adds a label like `ready-for-review` or `contribution-guidelines-met`
   - **If non-compliant**: Posts a friendly, constructive comment with specific suggestions

## Installation

```bash
# Install the 'gh aw' extension (if not already installed)
gh extension install github/gh-aw

# Add the PR Contribution Checker workflow to your repository
gh aw add githubnext/agentics/pr-contribution-checker
```

This walks you through adding the workflow to your repository.

You must also [choose a coding agent](https://github.github.com/gh-aw/reference/engines/) and add an API key secret for the agent to your repository.

**Mandatory Checklist**

* [ ] If in a fork, enable GitHub Actions and Pull Requests in the fork settings
* [ ] Ensure the workflow has permission to add labels and comments (via safe-outputs configuration)

## Configuration

This workflow works out of the box with sensible defaults. You can customize the agent's behavior by editing `.github/agentics/pr-contribution-checker.md` without recompilation.

### Customization options:

1. **Add repository-specific guidelines**: Edit the prompt to include your specific contribution requirements
2. **Adjust label names**: Modify which labels are added for compliant PRs
3. **Customize comment format**: Change the structure and tone of feedback comments
4. **Add integration with project tools**: Configure MCP servers for additional checks

After editing the prompt file, changes take effect immediately without running `gh aw compile`.

If you modify the workflow configuration (`.github/workflows/pr-contribution-checker.md`), run `gh aw compile pr-contribution-checker` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Pull request details (title, description, files changed)
- Repository contribution guidelines (CONTRIBUTING.md or similar)
- Related issues and context
- Code changes in the PR

## What it creates

- Adds labels to pull requests that meet guidelines (via safe-outputs)
- Posts comments with suggestions for PRs that need improvements (via safe-outputs)
- Requires only `read-all` permissions - write operations are handled securely through safe-outputs

## What web searches it performs

None - this workflow operates entirely on repository data.

## Human in the loop

- Review labels added to PRs for accuracy
- Validate feedback comments for helpfulness and correctness
- Override workflow decisions when needed
- Adjust the prompt to improve future checks
- Disable or uninstall the workflow if automation is not helpful

## Activity duration

- This workflow triggers on every PR (opened, synchronized, reopened)
- No automatic expiration - remains active as long as the workflow file is present
- Can be disabled at any time by removing or disabling the workflow file

## Security and Privacy

- Uses `roles: all` to allow any authenticated user to open PRs that trigger the workflow
- Operates with `read-all` permissions - all write operations use safe-outputs
- Labels and comments are the only outputs - no code modifications or PR approvals
- Designed to be helpful and constructive, not a gatekeeper
