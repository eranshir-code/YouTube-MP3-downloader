#!/bin/bash
# Dana Shir MP3 Downloader - Double-click to start

# Get the directory where this script is located
cd "$(dirname "$0")"

echo "================================================"
echo "Dana Shir MP3 Downloader"
echo "================================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "⚠️  First-time setup required!"
    echo ""
    echo "Please install Homebrew first:"
    echo "1. Open Safari and go to: brew.sh"
    echo "2. Copy the install command and run it in Terminal"
    echo "3. Then double-click this file again"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# Check and install yt-dlp
if ! command -v yt-dlp &> /dev/null; then
    echo "Installing yt-dlp..."
    brew install yt-dlp
fi

# Check and install ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Installing ffmpeg..."
    brew install ffmpeg
fi

# Check and install Flask
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing Flask..."
    pip3 install flask --user
fi

echo ""
echo "✓ All dependencies installed!"
echo ""
echo "Starting server..."
echo "The browser will open automatically."
echo ""
echo "⚠️  IMPORTANT: Keep this window open while using the app!"
echo "    Close this window to stop the server."
echo ""

# Wait a moment for user to read
sleep 2

# Start the server in background and capture the PID
python3 app.py &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Open browser
open http://localhost:8080

echo ""
echo "================================================"
echo "✓ Server is running!"
echo "================================================"
echo ""
echo "To stop the server:"
echo "  - Close this window, or"
echo "  - Press Ctrl+C"
echo ""

# Wait for the server process
wait $SERVER_PID
