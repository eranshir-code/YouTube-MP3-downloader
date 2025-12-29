# Enhanced Web Scraping Tool - Features

## New Capabilities Added

### 1. **Extended Parsing Functions**
- `extract_h1_tags()` - Extract all H1 headings
- `extract_h2_tags()` - Extract all H2 subheadings
- `extract_links()` - Extract URLs and link text
- `extract_images()` - Extract all image sources
- `extract_paragraphs()` - Extract paragraph content
- `extract_meta_tags()` - Extract metadata from HTML head

### 2. **Data Saving**
- `save_to_file()` - Save scraped data to JSON format
- Automatic timestamped filenames
- UTF-8 encoding support for Hebrew and other languages
- Pretty-printed JSON output

### 3. **Command-Line Interface**
Both `main.py` and `demo_offline.py` now support command-line arguments:

```bash
# Basic usage - scrape with default settings
python3 main.py https://example.com

# Full analysis - extract everything
python3 main.py https://example.com --full

# Save results to JSON file
python3 main.py https://example.com --full --save

# Analyze local HTML files
python3 demo_offline.py sample_ynet.html --full --save
```

### 4. **Full Analysis Mode**
When enabled with `--full` flag, extracts:
- Title
- H1 tags
- H2 tags
- Links (first 50)
- Images (first 20)
- Paragraphs (first 10)
- Meta tags
- Content length
- Timestamp

### 5. **Dual Mode Operation**
- **main.py**: Fetches live data from the web (requires internet)
- **demo_offline.py**: Works with local HTML files (no internet needed)

## Usage Examples

### Online Mode (main.py)
```bash
# Demo mode - shows examples
python3 main.py

# Scrape a specific URL
python3 main.py http://www.ynet.co.il --full --save

# Quick scrape without full analysis
python3 main.py https://example.com
```

### Offline Mode (demo_offline.py)
```bash
# Demo mode with sample file
python3 demo_offline.py

# Analyze your own HTML file
python3 demo_offline.py mypage.html --full --save

# Quick analysis
python3 demo_offline.py mypage.html
```

## Output Formats

### Basic Scrape
```json
{
  "url": "https://example.com",
  "status_code": 200,
  "title": "Example Domain",
  "h1_tags": ["Example Heading"],
  "fetched_at": "2025-12-29T10:00:00"
}
```

### Full Analysis
```json
{
  "url": "https://example.com",
  "status_code": 200,
  "title": "Example Domain",
  "h1_tags": ["Example Heading"],
  "h2_tags": ["Subheading 1", "Subheading 2"],
  "links": [
    {"url": "/about", "text": "About Us"},
    {"url": "/contact", "text": "Contact"}
  ],
  "images": ["/logo.png", "/banner.jpg"],
  "paragraphs": ["First paragraph text...", "Second paragraph..."],
  "meta_tags": {
    "description": "Page description",
    "keywords": "example, demo"
  },
  "content_length": 12345,
  "fetched_at": "2025-12-29T10:00:00"
}
```

## Features Summary

✓ Extract titles, headings (H1/H2)
✓ Parse links with anchor text
✓ Extract image sources
✓ Get paragraph content
✓ Parse meta tags
✓ Save results to JSON
✓ Command-line arguments
✓ Full/basic analysis modes
✓ Unicode/Hebrew support
✓ Timestamped outputs
✓ Error handling
✓ Works offline with local files

## Files in Project

- `main.py` - Main scraper for live web access
- `demo_offline.py` - Offline demo with local files
- `sample_ynet.html` - Sample Hebrew HTML for testing
- `requirements.txt` - Python dependencies (if needed)
- `README.md` - Setup instructions
- `FEATURES.md` - This file

## Next Steps

When internet access is available:
1. Run `main.py` to fetch live data from ynet.com
2. Try with different URLs
3. Use `--full --save` to create complete analyses
4. Build custom scrapers based on these functions

## Notes

- The proxy blocking issue prevents live web access in Claude Code
- Use `demo_offline.py` to test functionality
- Run `main.py` in a regular terminal for live web scraping
- All parsing functions work with both online and offline modes
