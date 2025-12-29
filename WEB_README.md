# URL Opener & YouTube Downloader - Web Application

A web-based tool that opens URLs in your browser or downloads YouTube audio as MP3 files. Access it from any device on your network!

## Features

- 🌐 **Web Interface** - Easy-to-use interface accessible from any browser
- 🎵 **YouTube to MP3** - Automatically downloads YouTube videos as MP3 files
- 🔗 **URL Opener** - Regular URLs open in your browser
- 📥 **Direct Download** - Download MP3 files directly from the web interface
- 🏠 **Default URL** - Press enter without typing to go to apple.com
- 📱 **Mobile Friendly** - Works on phones, tablets, and computers

## Requirements

- Python 3
- Flask (web framework)
- yt-dlp (for YouTube downloads)
- ffmpeg (for MP3 conversion)

## Installation

### 1. Install System Dependencies

```bash
# Install yt-dlp and ffmpeg
brew install yt-dlp ffmpeg
```

### 2. Install Python Packages

```bash
# Option A: Using virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install flask

# Option B: Using system pip
pip3 install flask --user
```

## Running the Web App

### Start the Server

```bash
# If using virtual environment:
source venv/bin/activate
python3 app.py

# Or directly:
python3 app.py
```

You'll see:
```
============================================================
URL Opener & YouTube Downloader - Web Interface
============================================================

Starting server...
Access the app at: http://localhost:5000
Press Ctrl+C to stop the server
============================================================
```

### Access from Your Computer

Open your browser and go to:
```
http://localhost:5000
```

### Access from Other Devices (Phone, Tablet, Another Computer)

1. Find your computer's IP address:
   ```bash
   # On macOS:
   ifconfig | grep "inet " | grep -v 127.0.0.1

   # Example output: inet 192.168.1.100
   ```

2. On any device on the same network, open:
   ```
   http://YOUR_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

## How to Use

1. **Open the web interface** in your browser
2. **Enter a URL** in the text box:
   - Regular URL (e.g., `google.com`) → Opens in browser
   - YouTube URL → Downloads as MP3
   - Leave empty and press Enter → Goes to apple.com
3. **For YouTube downloads**:
   - Wait for the download to complete
   - Click the "Download MP3" button
   - File saves to your Downloads folder

## Web Interface

### Main Page
- Clean, modern interface with gradient background
- URL input field with "Go" button
- Status indicators showing if yt-dlp and ffmpeg are installed
- Feature list
- Installation instructions if tools are missing

### Download Result Page
- Success message with file name
- Download button to get your MP3
- Back button to return to main page
- Error messages with helpful instructions if something goes wrong

## File Structure

```
web_project/
├── app.py                  # Flask web server
├── templates/
│   ├── index.html         # Main page
│   └── result.html        # Download/result page
├── open_url.py            # Command-line version (still works)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Examples

### From Your Computer
```
1. Open http://localhost:5000
2. Type: youtube.com/watch?v=dQw4w9WgXcQ
3. Click "Go"
4. Wait for download
5. Click "Download MP3"
```

### From Your Phone
```
1. Connect to same WiFi as your computer
2. Open http://192.168.1.100:5000 (use your computer's IP)
3. Enter YouTube URL
4. Download MP3 directly to your phone
```

## Troubleshooting

### "yt-dlp not installed" error
```bash
brew install yt-dlp
```

### "ffmpeg not installed" error
```bash
brew install ffmpeg
```

### Can't access from other devices
- Make sure all devices are on the same WiFi network
- Check firewall settings
- Verify the IP address is correct

### Port 5000 already in use
Edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

## Security Notes

- The server is accessible to anyone on your network
- Don't expose it to the internet without proper security
- For personal/local network use only
- Downloaded files are stored in your Downloads folder

## Making It Permanent

To make this accessible anytime:

### Option 1: Keep Terminal Open
Just keep the terminal window with `python3 app.py` running

### Option 2: Run in Background
```bash
nohup python3 app.py &
```

### Option 3: System Service (Advanced)
Create a system service that starts automatically - see online guides for your OS

## Command-Line Version

The original command-line tool (`open_url.py`) still works:
```bash
python3 open_url.py youtube.com/watch?v=VIDEO_ID
```

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3
- **Downloads**: yt-dlp + ffmpeg
- **Styling**: Modern gradient design with responsive layout

## Tips

- Bookmark `http://localhost:5000` for quick access
- Add to your phone's home screen for app-like experience
- Use it to quickly download music from YouTube videos
- Share your computer's URL with family members for easy access

## Development

To modify the design, edit:
- `templates/index.html` - Main page
- `templates/result.html` - Result page
- `app.py` - Server logic

Changes take effect after restarting the server.

---

**Enjoy your web-based URL opener and YouTube downloader!** 🎉
