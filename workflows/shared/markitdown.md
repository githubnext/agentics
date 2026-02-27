---
mcp-servers:
  markitdown:
    container: "mcp/markitdown"
    allowed: ["*"]
---

<!--
# MarkItDown MCP Server
# Converts documents and web resources to Markdown
#
# Wraps Microsoft's MarkItDown tool as an MCP server, enabling agents to
# convert PDFs, Word documents, PowerPoints, HTML pages, and other file
# formats into Markdown text for further processing.
#
# Documentation: https://hub.docker.com/r/mcp/markitdown
# Source:        https://github.com/microsoft/markitdown
#
# Available tools:
#   - convert_to_markdown: Convert a resource described by an http:, https:,
#                          file: or data: URI to Markdown
#
# Usage:
#   imports:
#     - shared/markitdown.md
-->
