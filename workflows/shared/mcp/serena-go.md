---
# Serena MCP Server - Go Code Analysis
# Language Server Protocol (LSP)-based tool for deep Go code analysis
#
# Documentation: https://github.com/oraios/serena
#
# Capabilities:
#   - Semantic code analysis using LSP (go to definition, find references, etc.)
#   - Symbol lookup and cross-file navigation
#   - Type inference and structural analysis
#   - Deeper insights than text-based grep approaches
#
# Usage:
#   imports:
#     - shared/mcp/serena-go.md

imports:
  - uses: ./serena.md
    with:
      languages: ["go"]
---

## Serena Go Code Analysis

The Serena MCP server is configured for Go code analysis in this workspace:
- **Workspace**: `${{ github.workspace }}`
- **Memory**: `/tmp/gh-aw/cache-memory/serena/`

### Project Activation

Before analyzing code, activate the Serena project:
```
Tool: activate_project
Args: { "path": "${{ github.workspace }}" }
```

### Analysis Guidelines

1. **Only analyze `.go` files** — Ignore unrelated file types
2. **Use Serena for semantic analysis** — Leverage LSP capabilities for deeper insights than text-based search
