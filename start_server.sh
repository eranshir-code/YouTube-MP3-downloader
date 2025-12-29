#!/bin/bash

echo "============================================="
echo "Starting URL Opener Web App"
echo "============================================="
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask is not installed!"
    echo ""
    echo "Please install Flask first:"
    echo "  pip3 install flask --user"
    echo "  or"
    echo "  python3 -m venv venv && source venv/bin/activate && pip install flask"
    echo ""
    exit 1
fi

# Check if yt-dlp is installed
if ! command -v yt-dlp &> /dev/null; then
    echo "⚠️  Warning: yt-dlp is not installed"
    echo "   YouTube downloads will not work"
    echo "   Install with: brew install yt-dlp"
    echo ""
fi

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  Warning: ffmpeg is not installed"
    echo "   MP3 conversion will not work"
    echo "   Install with: brew install ffmpeg"
    echo ""
fi

# Get local IP address
LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

echo "✓ Starting server..."
echo ""
echo "Access from this computer:"
echo "  http://localhost:8080"
echo ""
if [ ! -z "$LOCAL_IP" ]; then
    echo "Access from other devices (phone, tablet):"
    echo "  http://$LOCAL_IP:8080"
    echo ""
fi
echo "Press Ctrl+C to stop the server"
echo "============================================="
echo ""

# Run the Flask app
python3 app.py
