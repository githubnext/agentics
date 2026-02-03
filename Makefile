.PHONY: install compile setup clean help

# Default target
all: setup compile

# Install the github/gh-aw extension
install:
	@echo "Installing github/gh-aw extension..."
	gh extension install github/gh-aw
	gh extension upgrade github/gh-aw

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
	@echo "Uninstalling github/gh-aw extension..."
	gh extension remove github/gh-aw || true

# Show help
help:
	@echo "Available targets:"
	@echo "  install  - Install the github/gh-aw extension"
	@echo "  compile  - Run gh aw compile"
	@echo "  setup    - Install extension and compile (default)"
	@echo "  clean    - Uninstall the extension"
	@echo "  help     - Show this help message"