# VSCode Extension Metadata Collector (macOS)

This script retrieves basic metadata for a Visual Studio Code extension from the VSCode Marketplace. It uses `curl` to fetch the extension page and parses the response to extract commonly referenced details.

The tool is designed for macOS and includes basic error handling to ensure reliable execution even when data is missing or unavailable.

---

## Features

- Accepts user input for publisher name and extension name
- Builds a unique VSCode extension identifier
- Fetches extension data using `curl`
- Extracts:
  - Verification status
  - Release date
  - Last updated date
  - Install count
- Gracefully handles missing data (`N/A`)
- Displays clear error messages on request failure

---

## Requirements

- macOS
- Python 3.8 or newer
- `curl` (included by default)

### Python Dependency

```bash
pip install beautifulsoup4
