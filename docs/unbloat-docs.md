# 🗜️ Documentation Unbloat

> For an overview of all available workflows, see the [main README](../README.md).

The [Documentation Unbloat workflow](../workflows/unbloat-docs.md?plain=1) automatically reviews and simplifies documentation by removing verbosity while maintaining clarity and completeness.

## Installation

````bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/unbloat-docs
````

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

````bash
gh aw run unbloat-docs
````

Or trigger it in a pull request comment with:

````
/unbloat
````

## What It Does

````mermaid
graph LR
    A[Scan Documentation] --> B[Identify Verbosity]
    B --> C{Bloat Found?}
    C -->|Yes| D[Remove Redundancy]
    D --> E[Preserve Accuracy]
    E --> F[Create PR]
    C -->|No| G[Report: Docs are Lean]
````

The Documentation Unbloat workflow runs daily and can be triggered via `/unbloat` command in PR comments. It:

1. **Scans Documentation** - Reviews markdown files in the repository for bloat
2. **Identifies Verbosity** - Finds duplicate content, excessive bullet points, redundant examples, and verbose descriptions
3. **Removes Bloat** - Makes targeted edits to improve clarity and conciseness
4. **Preserves Accuracy** - Maintains all essential information, links, and technical details
5. **Creates Pull Requests** - Proposes documentation improvements one file at a time for easy review

## How It Works

### What Gets Removed

The workflow identifies and removes:

- **Duplicate content**: Same information repeated in different sections
- **Excessive bullet points**: Long lists that could be condensed into prose or tables
- **Redundant examples**: Multiple examples showing the same concept
- **Verbose descriptions**: Overly wordy explanations
- **Repetitive structure**: Overused "What it does" / "Why it's valuable" patterns

### What Gets Preserved

The workflow never removes:

- Technical accuracy or specific details
- Links to external resources
- Code examples (though duplicates may be consolidated)
- Critical warnings or notes
- Frontmatter metadata

### One File at a Time

The workflow improves exactly **one file per run** to keep changes small, focused, and easily reviewable. This incremental approach makes it easier to:

- Review and approve changes quickly
- Understand what was modified
- Revert changes if needed
- Track improvements over time

### Protected Files

Files can be protected from automatic editing by adding `disable-agentic-editing: true` to their frontmatter. The workflow automatically skips:

- Auto-generated documentation
- Changelog or release notes
- License or legal files
- Files marked with `disable-agentic-editing: true`

### Memory and Tracking

The workflow uses cache memory to track previously cleaned files, avoiding duplicate work and ensuring efficient coverage of documentation over time.

## Trigger Options

### Triggering CI on Pull Requests

By default, pull requests created by this workflow do not trigger CI workflow runs. This is a GitHub Actions feature to prevent event cascades.

To trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

### Daily Schedule

Runs automatically once per day at a scattered execution time to continuously improve documentation.

### Slash Command

Trigger on-demand in pull request comments:

````
/unbloat
````

This analyzes documentation files modified in the PR and proposes improvements.

### Manual Trigger

Run manually via GitHub Actions UI or CLI:

````bash
gh aw run unbloat-docs
````

## Success Criteria

A successful run:

- ✅ Improves exactly **one** documentation file
- ✅ Reduces bloat by at least 20% (lines, words, or bullet points)
- ✅ Preserves all essential information
- ✅ Creates a clear, reviewable pull request
- ✅ Explains the improvements made

## Benefits

**Improved Readability**: Concise documentation is easier to scan and understand, helping users find information faster.

**Reduced Maintenance**: Shorter documentation is easier to keep up-to-date as the project evolves.

**Better User Experience**: Clear, focused content reduces cognitive load and improves comprehension.

**Continuous Improvement**: Daily runs ensure documentation stays lean as new content is added.

## Example Improvements

### Before (Bloated)

````markdown
### Tool Name
Description of the tool.

- **What it does**: This tool does X, Y, and Z
- **Why it's valuable**: It's valuable because A, B, and C
- **How to use**: You use it by doing steps 1, 2, 3, 4, 5
- **When to use**: Use it when you need X
- **Benefits**: Gets you benefit A, benefit B, benefit C
- **Learn more**: [Link](url)
````

### After (Concise)

````markdown
### Tool Name
Description of the tool that does X, Y, and Z to achieve A, B, and C.

Use it when you need X by following steps 1-5. [Learn more](url)
````

## Customization

You can customize the workflow by editing the [`unbloat-docs.md`](../workflows/unbloat-docs.md) file:

- Adjust which directories or file patterns to scan
- Modify the success criteria (e.g., minimum bloat reduction percentage)
- Change the PR labeling and auto-merge behavior
- Add project-specific exclusion patterns
- Customize the tone or style guidance

After making changes, recompile the workflow:

````bash
gh aw compile unbloat-docs
````

## Complementary Workflows

This workflow pairs well with:

- [Daily Documentation Updater](daily-doc-updater.md) - Ensures accuracy and completeness
- [Glossary Maintainer](glossary-maintainer.md) - Keeps terminology consistent
- [Link Checker](link-checker.md) - Validates all documentation links

Together, these workflows maintain comprehensive, accurate, and readable documentation.
