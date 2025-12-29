#!/bin/bash
# Setup script for new machine

echo "================================================"
echo "Dana Shir MP3 Downloader - Setup"
echo "================================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✓ Homebrew installed"
fi

# Install yt-dlp
if ! command -v yt-dlp &> /dev/null; then
    echo "Installing yt-dlp..."
    brew install yt-dlp
else
    echo "✓ yt-dlp installed"
fi

# Install ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Installing ffmpeg..."
    brew install ffmpeg
else
    echo "✓ ffmpeg installed"
fi

# Install Flask
echo "Installing Flask..."
pip3 install flask --user

echo ""
echo "================================================"
echo "✓ Setup Complete!"
echo "================================================"
echo ""
echo "To start the server, run:"
echo "  ./start_server.sh"
echo ""
