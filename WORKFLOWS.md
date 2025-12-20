# Workflow Versioning and References

This document explains how to properly reference workflows from this repository.

## Referencing Workflows

When using workflows from this repository with `gh aw add`, always reference them by branch name or tag, not by specific commit SHA.

### ✅ Correct (Recommended)

```bash
# Reference by branch - gets latest version from main
gh aw add githubnext/agentics/ci-doctor@main

# Reference by tag (when available) - gets specific stable version
gh aw add githubnext/agentics/ci-doctor@v1.0.0
```

### ❌ Incorrect (Not Recommended)

```bash
# Don't reference by SHA - prevents proper version tracking
gh aw add githubnext/agentics/ci-doctor@ea350161ad5dcc9624cf510f134c6a9e39a6f94d
```

## Why Branch/Tag References Are Better

When you reference a workflow by branch or tag:
- ✅ The `gh aw update` command can check for and install newer versions
- ✅ You can easily see what version you're using
- ✅ Updates are straightforward and tracked

When you reference by SHA:
- ❌ The `gh aw update` command cannot determine if there are newer versions
- ❌ The reference is opaque - you can't easily tell what version it is
- ❌ Updates require manual SHA lookup and replacement

## Updating Workflows

To update workflows to their latest versions:

```bash
# Update a specific workflow
gh aw update ci-doctor

# Update all workflows
gh aw update --all
```

## Current Stable Branch

The `main` branch contains the current stable versions of all workflows. When in doubt, reference `@main`.

## Version Tags

Version tags will be created for major stable releases:
- `v1.0.0` - Initial stable release
- `v1.1.0` - Minor updates with new features
- `v1.0.1` - Patch updates with bug fixes

Check the [releases page](https://github.com/githubnext/agentics/releases) for available versions.

## Troubleshooting

### Error: "failed to resolve latest ref"

If you see an error like:
```
failed to resolve latest ref: failed to get latest commit for branch <sha>
```

This means your workflow has a SHA-based source reference. To fix:

1. Check your workflow's source field in the frontmatter
2. Update it to use `@main` or a version tag instead of the SHA
3. Recompile the workflow with `gh aw compile`

Example fix in your workflow:
```yaml
# Change this:
source: githubnext/agentics/workflows/ci-doctor.md@ea350161ad5dcc9624cf510f134c6a9e39a6f94d

# To this:
source: githubnext/agentics/workflows/ci-doctor.md@main
```
