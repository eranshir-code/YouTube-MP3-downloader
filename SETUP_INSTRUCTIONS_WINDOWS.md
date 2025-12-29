# Dana Shir MP3 Downloader - Windows Setup Instructions

## One-time Setup (only needed once)

### Step 1: Install Python
1. Go to: **python.org/downloads**
2. Click "Download Python" (get version 3.11 or newer)
3. Run the installer
4. **IMPORTANT:** Check the box "Add Python to PATH" at the bottom
5. Click "Install Now"
6. Wait for installation to complete

### Step 2: Install ffmpeg
**Option A - Using Chocolatey (easier if you have it):**
1. Open Command Prompt as Administrator
2. Run: `choco install ffmpeg`

**Option B - Manual installation:**
1. Go to: **ffmpeg.org/download.html**
2. Click "Windows builds from gyan.dev"
3. Download "ffmpeg-release-essentials.zip"
4. Extract the zip file to `C:\ffmpeg`
5. Add to PATH:
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\ffmpeg\bin`
   - Click OK on all windows
6. Restart your computer

### Step 3: Get the app files
1. Download the folder from GitHub or copy it from USB drive
2. Put the folder anywhere you like (Desktop or Documents works well)

## How to Use

### Every time you want to download music:

1. **Double-click** the file called: `Dana_Shir_Downloader.bat`
2. A command window will open and your browser will automatically open to the app
3. Paste a YouTube URL and click Download
4. Your MP3 files will be saved to your **Downloads** folder
   (Usually: `C:\Users\YourName\Downloads`)

### To stop the app:
- Just close the Command Prompt window that opened

## Troubleshooting

**Q: It says "Python is not installed"**
- Complete Step 1 above
- Make sure you checked "Add Python to PATH" during installation
- If you forgot, uninstall Python and reinstall with the PATH option checked

**Q: It says "ffmpeg is not installed"**
- Complete Step 2 above
- The .bat file will still work but MP3 conversion won't happen
- You'll get the audio file but not as MP3

**Q: The browser doesn't open automatically**
- Manually open any browser and go to: http://localhost:8080

**Q: Where are my downloaded files?**
- In your Downloads folder: `C:\Users\YourName\Downloads`

**Q: I get a security warning when double-clicking the .bat file**
- Click "More info" → "Run anyway"
- This is normal for batch files

## Notes
- Downloaded files are named with the YouTube video title
- If lyrics are available, they're saved as .srt files
- You need internet connection to download
- Keep the Command Prompt window open while using the app
