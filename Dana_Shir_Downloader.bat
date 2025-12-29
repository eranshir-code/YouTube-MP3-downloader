@echo off
REM Dana Shir MP3 Downloader - Double-click to start

cd /d "%~dp0"

echo ================================================
echo Dana Shir MP3 Downloader
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed!
    echo.
    echo Please install Python first:
    echo 1. Go to: python.org/downloads
    echo 2. Download Python 3.11 or newer
    echo 3. IMPORTANT: Check "Add Python to PATH" during installation
    echo 4. Then double-click this file again
    echo.
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing Flask...
    python -m pip install flask
)

REM Check if yt-dlp is installed
python -c "import yt_dlp" >nul 2>&1
if errorlevel 1 (
    echo Installing yt-dlp...
    python -m pip install yt-dlp
)

REM Check if ffmpeg is available
where ffmpeg >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: ffmpeg is not installed!
    echo MP3 conversion may not work without it.
    echo.
    echo To install ffmpeg:
    echo 1. Go to: ffmpeg.org/download.html
    echo 2. Download the Windows build
    echo 3. Follow installation instructions
    echo.
    echo OR use Chocolatey (if installed): choco install ffmpeg
    echo.
    timeout /t 5
)

echo.
echo Starting server...
echo The browser will open automatically.
echo.
echo IMPORTANT: Keep this window open while using the app!
echo            Close this window to stop the server.
echo.

REM Wait a moment for user to read
timeout /t 2 /nobreak >nul

REM Start the browser
start http://localhost:8080

REM Start the server
python app.py

pause
