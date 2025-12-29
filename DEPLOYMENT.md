# Deployment Guide - Share Your Tool With Others

## Quick Comparison

| Method | Ease | Cost | Access | Setup Time |
|--------|------|------|--------|------------|
| Local Network | ★★★★★ | Free | Same WiFi only | 0 min (already works!) |
| Ngrok | ★★★★☆ | Free tier | Internet | 5 min |
| Cloud (Render/Railway) | ★★★☆☆ | Free tier | Internet | 15 min |
| Cloud (Heroku) | ★★★☆☆ | $5/month | Internet | 20 min |
| VPS (DigitalOcean) | ★★☆☆☆ | $5/month | Internet | 30 min |

---

## Option 1: Local Network (Already Works!)

**Your URL:** `http://10.100.102.29:8080`

### Steps:
1. Keep server running: `./start_server.sh`
2. Share URL with anyone on same WiFi
3. They open in browser

### Best for:
- Family/friends at home
- Office coworkers
- Quick local sharing

---

## Option 2: Ngrok (Internet Access in 5 Minutes)

### Setup:
```bash
# Install ngrok
brew install ngrok

# Sign up (free) at ngrok.com and get auth token
ngrok config add-authtoken YOUR_TOKEN

# Start your server
./start_server.sh

# In another terminal, create tunnel
ngrok http 8080
```

### Share:
Copy the `https://` URL shown (e.g., `https://abc123.ngrok.io`)

### Pros:
- ✅ Works in 5 minutes
- ✅ Free tier available
- ✅ HTTPS included
- ✅ No server management

### Cons:
- ❌ URL changes each restart (unless paid plan)
- ❌ Your computer must stay on
- ❌ Bandwidth limits on free tier

---

## Option 3: Cloud Platform (Permanent URL)

### A. Render.com (Easiest, Free Tier)

1. **Sign up** at render.com (free)

2. **Create new Web Service**
   - Connect your GitHub repo OR upload files
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

3. **Add Buildpack** for yt-dlp and ffmpeg:
   - Add to render.yaml or install in Dockerfile

4. **Get URL**: `https://your-app.onrender.com`

### B. Railway.app (Simple, Free $5 Credit)

1. **Sign up** at railway.app

2. **Deploy from GitHub** or upload

3. **Environment Variables**: None needed

4. **Auto-detects** Python and installs requirements

5. **Get URL**: `https://your-app.up.railway.app`

### C. Heroku (Popular, $5/month)

```bash
# Install Heroku CLI
brew install heroku

# Login
heroku login

# Create app
heroku create your-app-name

# Add buildpacks for ffmpeg
heroku buildpacks:add --index 1 https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
heroku buildpacks:add --index 2 heroku/python

# Deploy
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

**Your URL**: `https://your-app-name.herokuapp.com`

---

## Option 4: Share the Code (Let Others Run It)

### Create a GitHub Repository:

1. **Create repo** on github.com

2. **Push code**:
```bash
cd web_project
git init
git add .
git commit -m "URL Opener & YouTube Downloader"
git remote add origin https://github.com/YOUR_USERNAME/url-opener.git
git push -u origin main
```

3. **Share repo URL**: `https://github.com/YOUR_USERNAME/url-opener`

### Others can run it:
```bash
git clone https://github.com/YOUR_USERNAME/url-opener.git
cd url-opener
pip install -r requirements.txt
brew install yt-dlp ffmpeg
./start_server.sh
```

---

## Recommended Approach by Use Case

### Family/Friends at Home
→ **Use Local Network** (already works!)
- Share: `http://10.100.102.29:8080`

### Quick Demo to Remote Friend
→ **Use Ngrok**
- 5-minute setup
- Works anywhere
- Free

### Permanent Public Tool
→ **Use Render or Railway**
- Free tier
- Always online
- Own domain possible

### Developer Friends
→ **Share on GitHub**
- They run their own instance
- Most control
- Free

---

## Important Notes

### For Cloud Deployment:
- **yt-dlp/ffmpeg**: Some platforms require special buildpacks
- **Downloads**: Cloud servers have limited storage
- **Terms of Service**: Check if YouTube downloading is allowed
- **Rate Limits**: Free tiers have usage limits

### For Internet Exposure:
- No authentication currently (anyone can use it)
- Could add password protection if needed
- Be aware of bandwidth/storage costs

### Security Considerations:
- Current app has no auth/rate limiting
- Fine for personal/local use
- Add authentication for public deployment

---

## Quick Start Commands

### Local (Already Works)
```bash
./start_server.sh
# Share: http://10.100.102.29:8080
```

### Ngrok (5 minutes)
```bash
brew install ngrok
ngrok http 8080
# Share the https URL shown
```

### GitHub (Share Code)
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
# Share: Your GitHub repo URL
```

---

## Need Help?

- Local network issues → Check firewall settings
- Ngrok issues → Verify auth token
- Cloud deployment → Check platform documentation
- GitHub → See WEB_README.md for full instructions

Choose the option that fits your needs best!
