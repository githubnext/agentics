# Release and Maintenance Workflows

This document describes the new release automation workflows added to the repository.

## Overview

Two new GitHub Actions workflows have been added to automate the release process and trigger post-release maintenance tasks:

1. **release.yml** - Creates GitHub releases
2. **maintenance.yml** - Runs maintenance tasks after releases

## Release Workflow

### Trigger Methods

#### Automatic (Recommended)
The release workflow automatically triggers when you push a version tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Tag format: `v*.*.*` (e.g., `v1.0.0`, `v2.1.3`, `v1.0.0-beta.1`)

#### Manual
You can also manually trigger the workflow from the GitHub Actions UI:
1. Go to Actions → Release
2. Click "Run workflow"
3. Enter the tag name (e.g., `v1.0.0`)

### What It Does

1. **Creates a GitHub Release**
   - Uses the GitHub CLI (`gh release create`)
   - Generates release notes automatically
   - Links to commit history

2. **Triggers Maintenance Workflow**
   - After successful release creation
   - Passes the release tag to the maintenance workflow
   - Runs on the repository's default branch

### Permissions

- `contents: write` - Required to create releases
- `actions: write` - Required to trigger the maintenance workflow

## Maintenance Workflow

### Purpose

The maintenance workflow runs automatically after each release to perform post-release tasks.

### Current Tasks

Currently, the workflow contains placeholders for common maintenance tasks:
- Update documentation
- Clean up old artifacts
- Update dependencies
- Send notifications

### Customization

To add actual maintenance tasks, edit `.github/workflows/maintenance.yml` and replace the placeholder comments with your specific tasks.

Example:
```yaml
- name: Run maintenance tasks
  run: |
    echo "Running maintenance tasks after release"
    if [ -n "${{ inputs.release_tag }}" ]; then
      echo "Triggered by release: ${{ inputs.release_tag }}"
    fi
    
    # Your custom tasks here
    npm run update-docs
    npm run clean-artifacts
```

### Manual Triggering

You can also manually trigger the maintenance workflow:
1. Go to Actions → Maintenance
2. Click "Run workflow"
3. Optionally specify a release tag

### Permissions

- `contents: read` - Minimal read-only access following security best practices

## Security

Both workflows follow GitHub Actions security best practices:
- Explicit GITHUB_TOKEN permissions (principle of least privilege)
- No secrets exposed
- CodeQL security scanning passed
- No deprecated actions used

## Testing

To test the workflows without creating an actual release:
1. Use the manual trigger option in the GitHub Actions UI
2. Specify a test tag (e.g., `v0.0.1-test`)
3. Review the workflow logs
4. Delete the test release if needed

## Troubleshooting

### Release workflow fails at "Create Release"
- Check that the tag doesn't already exist
- Verify the tag format matches `v*.*.*`
- Ensure you have `contents: write` permissions

### Maintenance workflow not triggered
- Check the release workflow logs for the "Trigger maintenance workflow" step
- Verify the maintenance.yml file exists in `.github/workflows/`
- Ensure the workflow has `actions: write` permissions

### Wrong branch used for maintenance
- The workflow uses the repository's default branch
- If you need a different branch, modify the `ref` parameter in release.yml

## Example Usage

```bash
# 1. Create and push a tag
git tag v1.0.0
git push origin v1.0.0

# 2. The release workflow automatically:
#    - Creates a GitHub release
#    - Triggers the maintenance workflow

# 3. Check the Actions tab to see both workflows running

# 4. The maintenance workflow receives the tag 'v1.0.0' as input
```

## Files Modified

- `.github/workflows/release.yml` - Release creation workflow
- `.github/workflows/maintenance.yml` - Post-release maintenance workflow
