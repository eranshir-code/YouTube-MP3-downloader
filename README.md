# URL Opener with YouTube MP3 Downloader

A simple Python program that:
- Opens URLs in your default web browser
- Automatically downloads MP3 audio from YouTube links

## Features

- Opens any URL in your default web browser
- **Detects YouTube links and downloads audio as MP3**
- Automatically adds `https://` if you don't include it
- Default URL is **apple.com** if no URL is entered
- Best quality audio extraction
- Simple command-line interface
- Interactive mode for easy use

## Usage

### Method 1: Command-line argument
```bash
# Open regular URL
python3 open_url.py ynet.com

# Download YouTube audio as MP3
python3 open_url.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Method 2: Interactive mode
```bash
python3 open_url.py
```
Then enter the URL when prompted (or press Enter for apple.com).

## Examples

```bash
# Open a regular website
python3 open_url.py ynet.com

# Download YouTube video as MP3
python3 open_url.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Short YouTube URL also works
python3 open_url.py "https://youtu.be/dQw4w9WgXcQ"

# Interactive mode - enter a URL
python3 open_url.py
# Then type: google.com

# Interactive mode - press Enter for default (apple.com)
python3 open_url.py
# Then just press Enter (opens apple.com)
```

## Requirements

- Python 3
- `yt-dlp` (for YouTube downloads)
- `ffmpeg` (for MP3 conversion)

### Installing Required Tools

```bash
# Using Homebrew (macOS) - RECOMMENDED
brew install yt-dlp ffmpeg

# Or install separately:
brew install yt-dlp
brew install ffmpeg

# Alternative using pip for yt-dlp only:
pip3 install yt-dlp
brew install ffmpeg  # Still need ffmpeg for MP3 conversion
```

**Important:** Both `yt-dlp` AND `ffmpeg` are required for MP3 downloads to work properly.

## How It Works

1. **Regular URLs**: Opens in your default web browser (Chrome, Safari, Firefox, etc.)
2. **YouTube URLs**: Automatically detected and audio is downloaded as MP3
   - Detects: youtube.com, youtu.be, m.youtube.com
   - Extracts audio in best quality
   - Converts to MP3 format
   - **Saves in your Downloads folder** (`~/Downloads/`)
   - Filename is the video's title

## YouTube Download Output

When you provide a YouTube URL:
```
Detected YouTube link: https://www.youtube.com/watch?v=...
Downloading audio as MP3...
✓ Download completed successfully!
✓ File saved in: /Users/yourname/Downloads
```

The MP3 file will be saved in your **Downloads folder** with the video's title as the filename.
