# Dana Shir MP3 Downloader

A simple web-based tool to download YouTube videos as MP3 files with lyrics.

## Quick Start Guide

### For Windows Users
1. Read: `SETUP_INSTRUCTIONS_WINDOWS.md`
2. Double-click: `Dana_Shir_Downloader.bat`

### For Mac/Linux Users
1. Read: `SETUP_INSTRUCTIONS.md`
2. Double-click: `Dana_Shir_Downloader.command`

## What This Does
- Download YouTube videos as MP3 files
- Automatically download lyrics when available (as .srt files)
- Simple web interface - no technical knowledge needed
- Files saved to your Downloads folder

## Features
- Web-based interface (runs in your browser)
- Double-click launcher - no command line needed
- Auto-installs dependencies
- Best quality audio extraction
- Automatic lyrics download (when available)
- Works with any YouTube URL

## System Requirements
- **Windows:** Python 3.11+, ffmpeg
- **Mac:** Python 3 (included), yt-dlp, ffmpeg (auto-installed via Homebrew)
- Internet connection

## First-Time Setup
See the setup instructions file for your operating system:
- Windows: `SETUP_INSTRUCTIONS_WINDOWS.md`
- Mac: `SETUP_INSTRUCTIONS.md`

## Daily Use
1. Double-click the launcher file (`.bat` for Windows or `.command` for Mac)
2. Browser opens automatically to the app at http://localhost:8080
3. Paste any YouTube URL
4. Click Download
5. Find your MP3 in the Downloads folder

## File Locations
- **Windows:** `C:\Users\YourName\Downloads`
- **Mac:** `~/Downloads/`

## Advanced Usage - Command Line (Optional)

The original command-line version is still available:

```bash
# Run the web server manually
python3 app.py

# Or use the original CLI version
python3 open_url.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

See the original README sections below for more CLI options.

## Troubleshooting
See the setup instructions file for common issues and solutions.

## Cloud Version
There's also a cloud version deployed at Render.com, but YouTube often blocks cloud downloads.
For reliable downloads, use the local version (this one).

## Credits
Created with Flask, yt-dlp, and ffmpeg.
