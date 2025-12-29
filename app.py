from flask import Flask, render_template, request, redirect, send_file, jsonify
import subprocess
import os
import re
from datetime import datetime

app = Flask(__name__)

# Configuration
DOWNLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def is_youtube_url(url):
    """Check if URL is a YouTube link"""
    youtube_domains = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
    return any(domain in url for domain in youtube_domains)


def check_dependencies():
    """Check if required tools are installed"""
    yt_dlp_installed = subprocess.run(['which', 'yt-dlp'], capture_output=True).returncode == 0
    ffmpeg_installed = subprocess.run(['which', 'ffmpeg'], capture_output=True).returncode == 0
    return yt_dlp_installed, ffmpeg_installed


def download_youtube_audio(url):
    """Download audio from YouTube as MP3"""
    try:
        # Set output path
        output_template = os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')

        # Download audio as MP3
        command = [
            'yt-dlp',
            '-x',  # Extract audio
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            '--no-check-certificates',
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            '--extractor-args', 'youtube:player_client=android',
            '-o', output_template,
            '--print', 'after_move:filepath',  # Print the output file path
            url
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # Extract filename from output
            output_lines = result.stdout.strip().split('\n')
            filepath = output_lines[-1] if output_lines else None

            if filepath and os.path.exists(filepath):
                filename = os.path.basename(filepath)
                return True, filename
            else:
                return False, "Download completed but file not found"
        else:
            return False, result.stderr

    except Exception as e:
        return False, str(e)


@app.route('/')
def index():
    """Main page"""
    yt_dlp_ok, ffmpeg_ok = check_dependencies()
    return render_template('index.html',
                         yt_dlp_installed=yt_dlp_ok,
                         ffmpeg_installed=ffmpeg_ok)


@app.route('/process', methods=['POST'])
def process_url():
    """Process submitted URL"""
    url = request.form.get('url', '').strip()

    # Use default if empty
    if not url:
        url = 'apple.com'

    # Add https if no protocol
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Check if it's YouTube
    if is_youtube_url(url):
        # Check dependencies
        yt_dlp_ok, ffmpeg_ok = check_dependencies()

        if not yt_dlp_ok or not ffmpeg_ok:
            missing = []
            if not yt_dlp_ok:
                missing.append('yt-dlp')
            if not ffmpeg_ok:
                missing.append('ffmpeg')

            return render_template('result.html',
                                 error=True,
                                 message=f"Missing required tools: {', '.join(missing)}",
                                 install_needed=True)

        # Download the audio
        success, result = download_youtube_audio(url)

        if success:
            return render_template('result.html',
                                 success=True,
                                 filename=result,
                                 download_url=f"/download/{result}")
        else:
            return render_template('result.html',
                                 error=True,
                                 message=f"Download failed: {result}")
    else:
        # Regular URL - redirect to it
        return redirect(url)


@app.route('/download/<filename>')
def download_file(filename):
    """Serve downloaded MP3 file"""
    filepath = os.path.join(DOWNLOAD_FOLDER, filename)

    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found", 404


if __name__ == '__main__':
    print("=" * 60)
    print("URL Opener & YouTube Downloader - Web Interface")
    print("=" * 60)
    print("\nStarting server...")

    # Get port from environment variable (for cloud deployment) or use 8080
    port = int(os.environ.get('PORT', 8080))

    print(f"Access the app at: http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)

    # Disable debug mode in production
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
