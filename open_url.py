#!/usr/bin/env python3
"""
Simple program to open URLs in a web browser or download YouTube audio
"""

import webbrowser
import sys
import subprocess
import os


def is_youtube_url(url):
    """Check if URL is a YouTube link"""
    youtube_domains = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
    return any(domain in url for domain in youtube_domains)


def download_youtube_audio(url):
    """Download audio from YouTube as MP3"""
    print(f"Detected YouTube link: {url}")
    print("Downloading audio as MP3...")

    try:
        # Check if yt-dlp is installed
        result = subprocess.run(['which', 'yt-dlp'], capture_output=True, text=True)
        if result.returncode != 0:
            print("\n✗ yt-dlp is not installed!")
            print("\nTo install yt-dlp:")
            print("  brew install yt-dlp")
            print("  or")
            print("  pip3 install yt-dlp")
            return False

        # Check if ffmpeg is installed (required for MP3 conversion)
        result = subprocess.run(['which', 'ffmpeg'], capture_output=True, text=True)
        if result.returncode != 0:
            print("\n✗ ffmpeg is not installed!")
            print("ffmpeg is required to convert audio to MP3 format.")
            print("\nTo install ffmpeg:")
            print("  brew install ffmpeg")
            return False

        # Get Downloads folder path
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Create Downloads folder if it doesn't exist
        os.makedirs(downloads_folder, exist_ok=True)

        # Set output path to Downloads folder
        output_path = os.path.join(downloads_folder, '%(title)s.%(ext)s')

        # Download audio as MP3
        command = [
            'yt-dlp',
            '-x',  # Extract audio
            '--audio-format', 'mp3',  # Convert to MP3
            '--audio-quality', '0',  # Best quality
            '-o', output_path,  # Output to Downloads folder
            url
        ]

        print("Processing...")
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("✓ Download completed successfully!")
            print(f"✓ File saved in: {downloads_folder}")
            print("✓ File format: MP3")
            return True
        else:
            print(f"✗ Download failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def open_url(url):
    """Open a URL in the default web browser"""
    # Add http:// if no protocol specified
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Check if it's a YouTube URL
    if is_youtube_url(url):
        download_youtube_audio(url)
    else:
        print(f"Opening: {url}")
        webbrowser.open(url)
        print("✓ Browser opened!")


def main():
    """Main function"""
    default_url = "apple.com"

    # Check if URL provided as command-line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
        open_url(url)
    else:
        # Interactive mode - ask user for URL
        print("URL Opener")
        print("-" * 40)
        url = input(f"Enter URL to open (default: {default_url}): ").strip()

        if url:
            open_url(url)
        else:
            print(f"No URL entered. Opening default: {default_url}")
            open_url(default_url)


if __name__ == "__main__":
    main()
