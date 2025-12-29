# Dana Shir MP3 Downloader - Windows Guide (No Technical Knowledge Needed)

## Complete Step-by-Step Instructions

---

## PART 1: One-Time Setup (Do this once, takes 15-20 minutes)

### Step 1: Get the Files on the Computer

**Option A: USB Drive (Easiest)**
1. Copy the entire `web_project` folder to a USB drive
2. Plug the USB into the Windows computer
3. Open "File Explorer" (the folder icon on taskbar)
4. Click on the USB drive (usually shows up on the left side)
5. Right-click the `web_project` folder
6. Click "Copy"
7. Go to Desktop (click "Desktop" on the left side)
8. Right-click on empty space
9. Click "Paste"
10. Done! The folder is now on the Desktop

**Option B: Email**
1. Zip the `web_project` folder (right-click → Send to → Compressed folder)
2. Email the zip file to yourself
3. Open email on the Windows computer
4. Download the attachment
5. Double-click the downloaded zip file
6. Click "Extract all" button at the top
7. Choose Desktop as location
8. Click "Extract"

### Step 2: Install Python (Required)

1. Open any web browser (Edge, Chrome, Firefox)
2. Go to: **python.org/downloads**
3. You'll see a big yellow button that says "Download Python 3.x.x"
4. Click that button
5. Wait for the download to finish (shows at bottom of browser)
6. Click on the downloaded file to run it
7. **VERY IMPORTANT:** Check the box at the bottom that says "Add Python to PATH"
   - This is critical! Don't skip this!
8. Click "Install Now"
9. Wait for installation (takes 2-3 minutes)
10. When it says "Setup was successful", click "Close"

### Step 3: Install ffmpeg (Required)

**Method A: Using Chocolatey (Easier if you already have it)**

1. Right-click the Windows Start button (bottom left)
2. Click "Windows PowerShell (Admin)" or "Terminal (Admin)"
3. If asked "Do you want to allow this app to make changes?", click "Yes"
4. Type: `choco install ffmpeg`
5. Press Enter
6. Wait for installation
7. Close the window

**If you don't have Chocolatey, skip to Method B**

**Method B: Manual Installation (Works for everyone)**

1. Open web browser
2. Go to: **ffmpeg.org/download.html**
3. Look for "Windows" section
4. Click on "Windows builds from gyan.dev"
5. Click "ffmpeg-release-essentials.zip" to download
6. Wait for download to finish
7. Click on the downloaded zip file
8. Click "Extract all" at the top
9. Change the location to: `C:\ffmpeg`
10. Click "Extract"

**Now add ffmpeg to PATH:**

11. Right-click "This PC" or "My Computer" on Desktop (or in File Explorer)
    - If not on Desktop: Press Windows key + E, then look on left side
12. Click "Properties"
13. Click "Advanced system settings" (on the left or right side)
14. Click "Environment Variables" button (near bottom)
15. In the bottom section "System variables", scroll and find "Path"
16. Click on "Path" to highlight it
17. Click "Edit" button
18. Click "New" button
19. Type: `C:\ffmpeg\bin`
20. Click "OK"
21. Click "OK" again
22. Click "OK" one more time
23. **Restart the computer** (important for changes to take effect)

---

## PART 2: Using the Downloader (Every time you want to download)

### Step 1: Start the Application

1. Open "File Explorer" (folder icon on taskbar)
2. Go to Desktop
3. Double-click the `web_project` folder to open it
4. Look for a file called `Dana_Shir_Downloader.bat`
   - It will have a gear/window icon
   - If you see two files with similar names, choose the one ending in `.bat`
5. Double-click `Dana_Shir_Downloader.bat`

**What happens:**
- A black window (Command Prompt) will open with text
- Your web browser will automatically open to the app
- The black window will say "Server is running"

**If you see a security warning:**
- Click "More info"
- Click "Run anyway"

### Step 2: Download a YouTube Video as MP3

1. Go to YouTube in another browser tab/window
2. Find the video you want
3. Click on the address bar at the top (where the URL is)
4. Right-click and select "Copy" (or press Ctrl+C)
5. Go back to the Dana Shir Downloader tab/window
6. Click in the white text box
7. Right-click and select "Paste" (or press Ctrl+V)
8. Click the purple "Download" button
9. Wait (this takes 30 seconds to 2 minutes depending on video length)

**When download is complete:**
- You'll see "Download Ready!" with a music note emoji
- The filename will be shown
- Click the purple "Download MP3" button
- The MP3 file will be saved to your Downloads folder

### Step 3: Find Your Downloaded MP3

1. Open "File Explorer"
2. Click "Downloads" on the left side
3. Your MP3 file will be there, named with the video title
4. If there were lyrics available, you'll also see a `.srt` file

**To listen:**
- Double-click the MP3 file
- It will open in your default music player (Windows Media Player, Groove, etc.)

### Step 4: Download Another Song (Optional)

1. In the browser, click "Back to Home" button
2. Paste another YouTube URL
3. Click Download
4. Repeat!

### Step 5: When Finished

1. Close the browser tab/window
2. Go to the black Command Prompt window
3. Click the X button to close it
   - Or click in the window and press Ctrl+C

**The server stops when you close the black window**

---

## Common Questions

**Q: Where's the Dana_Shir_Downloader.bat file?**
- Desktop → web_project folder → look for file ending in `.bat`

**Q: What if the browser doesn't open automatically?**
- Open any browser manually
- Type in address bar: `localhost:8080`
- Press Enter

**Q: The black window closed by itself**
- Something went wrong with the setup
- Make sure Python and ffmpeg are installed correctly
- Double-click the .bat file again

**Q: It says "Python is not installed"**
- Go back to Part 1, Step 2
- Make sure you checked "Add Python to PATH" during installation
- If you forgot, uninstall Python and reinstall with that box checked

**Q: It says "ffmpeg is not installed"**
- Go back to Part 1, Step 3
- Complete the ffmpeg installation
- Restart your computer after adding to PATH

**Q: The download failed with an error**
- Some YouTube videos are protected and can't be downloaded
- Try a different video
- Make sure you have internet connection

**Q: Can I download multiple videos at once?**
- No, do them one at a time
- Wait for each download to finish before starting the next

**Q: Where exactly are my downloaded files?**
- Press Windows key + R
- Type: `%USERPROFILE%\Downloads`
- Press Enter
- This opens your Downloads folder

**Q: Can I change where files are saved?**
- This requires editing the code (advanced)
- By default, always saves to Downloads folder

**Q: The black window shows lots of text scrolling**
- This is normal! It's showing download progress
- Don't close it until download finishes

**Q: How do I create a shortcut on Desktop?**
1. Go to Desktop → web_project folder
2. Right-click `Dana_Shir_Downloader.bat`
3. Click "Create shortcut"
4. Drag the shortcut to Desktop
5. Rename it to "Download MP3" if you want
6. Now you can double-click the shortcut instead of opening the folder

---

## Quick Reference (After Setup is Complete)

1. **Double-click** `Dana_Shir_Downloader.bat` (or its shortcut)
2. **Browser opens** automatically
3. **Paste** YouTube URL
4. **Click** Download button
5. **Wait** for "Download Ready!"
6. **Click** "Download MP3" button
7. **Find** file in Downloads folder
8. **Close** the black window when done

---

## Visual Checklist

**One-time setup:**
- ☐ Copy web_project folder to Desktop
- ☐ Install Python (with "Add to PATH" checked!)
- ☐ Install ffmpeg
- ☐ Add ffmpeg to PATH
- ☐ Restart computer

**Every use:**
- ☐ Double-click Dana_Shir_Downloader.bat
- ☐ Browser opens showing the app
- ☐ Paste YouTube URL
- ☐ Click Download
- ☐ Download MP3 file when ready
- ☐ Close black window when done

---

## Need Help?

If these instructions don't work:
1. Make sure you completed ALL steps in Part 1
2. Try restarting the computer
3. Check that Python and ffmpeg installed correctly:
   - Open Command Prompt (search for "cmd" in Start menu)
   - Type: `python --version` and press Enter (should show Python 3.x.x)
   - Type: `ffmpeg -version` and press Enter (should show ffmpeg version)
   - If either says "not recognized", the installation didn't work

Created with ❤️ for Dana Shir
