# 🔍 Duplicate Code Detector

> For an overview of all available workflows, see the [main README](../README.md).

The [Duplicate Code Detector workflow](../workflows/duplicate-code-detector.md?plain=1) automatically identifies duplicate code patterns across your codebase and suggests refactoring opportunities to improve maintainability.

## What It Does

This workflow runs daily to analyze recent code changes and detect duplicate patterns:

- **Analyzes Recent Changes**: Focuses on files modified in recent commits to catch new duplication early
- **Semantic Analysis**: Uses intelligent pattern matching to find duplicates beyond simple text matching
- **Creates Actionable Issues**: Generates focused issues (max 3 per run) for significant duplication patterns
- **Assigns to Copilot**: Issues are automatically assigned to @copilot for potential automated remediation

## Why It's Valuable

Code duplication is a common source of technical debt that:

- Makes maintenance harder (fixes must be applied in multiple places)
- Increases bug risk (inconsistent fixes across duplicated code)
- Bloats the codebase unnecessarily
- Reduces code clarity and understandability

The Duplicate Code Detector helps by:

- **Catching duplication early** before it spreads
- **Providing specific recommendations** for refactoring
- **Enabling automated remediation** through Copilot assignment
- **Improving code quality** continuously over time

## How It Works

## How It Works

````mermaid
graph LR
    A[Analyze Recent Changes] --> B[Detect Patterns]
    B --> C[Find Duplicates]
    C --> D{Significant?}
    D -->|Yes| E[Create Refactoring Issue]
    D -->|No| F[Report: Code is DRY]
````

1. **Daily Schedule**: Runs automatically every day
2. **Change Analysis**: Examines files modified in recent commits
3. **Pattern Detection**: Searches for:
   - Identical or nearly identical functions
   - Repeated logic blocks
   - Similar implementations of the same functionality
   - Copy-pasted code with minor variations
4. **Reporting**: Creates separate issues for each significant pattern found (threshold: >10 lines or 3+ instances)
5. **Assignment**: Issues are assigned to @copilot for automated or manual remediation

## What Gets Detected

### Reported Patterns

- Identical or nearly identical functions in different files
- Repeated code blocks that could be extracted to utilities
- Similar classes or modules with overlapping functionality
- Copy-pasted code with minor modifications
- Duplicated business logic across components

### Excluded Patterns

- Standard boilerplate code (imports, package declarations)
- Test setup/teardown code (acceptable duplication in tests)
- Configuration files with similar structure
- Language-specific patterns (constructors, getters/setters)
- Small code snippets (<5 lines) unless highly repetitive

## Example Output

When duplication is detected, the workflow creates issues like:

````markdown
# 🔍 Duplicate Code Detected: Error Handling Pattern in Parser Module

**Severity**: High  
**Occurrences**: 4 instances  
**Locations**:
- `src/parser/json.ts` (lines 45-58)
- `src/parser/xml.ts` (lines 67-80)
- `src/parser/yaml.ts` (lines 34-47)
- `src/parser/csv.ts` (lines 89-102)

## Refactoring Recommendations

1. **Extract Common Error Handler**
   - Create utility: `src/parser/error-handler.ts`
   - Estimated effort: 2-3 hours
   - Benefits: Single source of truth, easier to maintain
````

## Merge Rate

Based on usage in the gh-aw repository, this workflow has demonstrated **79% merge rate** (76 merged PRs out of 96 proposed), indicating high practical value and acceptance by maintainers.

## Configuration

The workflow is configured to:

- Run daily on a schedule
- Create max 3 issues per run to avoid overwhelm
- Auto-expire issues after 2 days if not addressed
- Skip test files, generated code, and workflow files
- Focus on source code files only

## Getting Started

This workflow requires no additional setup - it works out of the box with any repository. Simply enable it and it will start analyzing your codebase for duplication patterns.

The workflow uses standard code exploration tools and git commands, making it applicable to any programming language and project structure.

## Learn More

- [GitHub Agentic Workflows Documentation](https://github.github.io/gh-aw/)
- [Blog: Continuous Simplicity Workflows](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-simplicity/)
