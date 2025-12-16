# VSCode Extension Metadata Collector (macOS)

This script retrieves basic metadata for a Visual Studio Code extension from the VSCode Marketplace. It uses `curl` to fetch the extension page and parses the response to extract commonly referenced details. The tool is designed for macOS and includes basic error handling to ensure reliable execution even when data is missing or unavailable.

## Features

- Accepts user input for publisher name and extension name
- Builds a unique VSCode extension identifier
- Fetches extension data using `curl`
- Extracts verification status, release date, last updated date, and install count
- Gracefully handles missing data (displays `N/A`)
- Displays clear error messages on request failure

## Requirements

- macOS
- Python 3.8 or newer
- `curl` (included by default)

### Python Dependency

```bash
pip install beautifulsoup4
```

## Usage

Run the script and follow the prompts:

```bash
python3 VSCodeExtScript.py
```

### Example

```text
Enter publisher name (e.g. ms-python): ms-python
Enter VSCode extension name (e.g. debugpy): debugpy

verified: 'Y'
ReleaseDate: '6/14/2023 18:20:56'
LastUpdatedDate: '12/15/2025 23:00:32'
InstallCount: '196,234,513'
```

## Output Fields

| Field | Description |
|-------|-------------|
| `verified` | Indicates whether the publisher is verified (Y, N, or N/A) |
| `ReleaseDate` | Date the extension was first published |
| `LastUpdatedDate` | Date the extension was last updated |
| `InstallCount` | Number of unique installs |

## Notes

- Some fields may return `N/A` if the information cannot be found
- The VSCode Marketplace page structure may change over time
- Excessive automated requests may result in rate limiting

## Disclaimer

This tool is intended for educational, research, and auditing purposes only. Ensure usage complies with applicable terms of service.