.PHONY: install compile setup clean help

# Default target
all: setup compile

# Install the githubnext/gh-aw extension
install:
	@echo "Installing githubnext/gh-aw extension..."
	gh extension install githubnext/gh-aw
	gh extension upgrade githubnext/gh-aw

# Run gh aw compile
compile:
	@echo "Running gh aw compile..."
	gh aw compile
	gh aw compile --dir workflows

# Setup: install extension and compile
setup: install compile
	@echo "Setup complete!"

# Clean up (uninstall extension if needed)
clean:
	@echo "Uninstalling githubnext/gh-aw extension..."
	gh extension remove githubnext/gh-aw || true

# Show help
help:
	@echo "Available targets:"
	@echo "  install  - Install the githubnext/gh-aw extension"
	@echo "  compile  - Run gh aw compile"
	@echo "  setup    - Install extension and compile (default)"
	@echo "  clean    - Uninstall the extension"
	@echo "  help     - Show this help message"