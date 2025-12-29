# 🚀 Quick Railway Deployment - Manual Steps

**⚠️ IMPORTANT: Do this in a REGULAR TERMINAL, not in Claude Code**

The Claude Code environment blocks network access, so open Terminal.app and follow these steps:

---

## Step-by-Step Instructions

### 1️⃣ Open Regular Terminal
- Press `Cmd + Space`
- Type "Terminal"
- Press Enter

### 2️⃣ Navigate to Project
```bash
cd ~/Downloads/ai-bootcamp-main/HDC-bootcamp/SESSION7-Agentic-coding/web_project
```

### 3️⃣ Install Railway CLI
```bash
npm i -g @railway/cli
```

**Alternative if that fails:**
```bash
brew install railway
```

### 4️⃣ Login to Railway
```bash
railway login
```
- A browser window will open
- Sign up/login (free account)
- Authorize the CLI
- Return to terminal

### 5️⃣ Initialize Project
```bash
railway init
```
- Choose: "Create new project"
- Give it a name (e.g., "url-opener")
- Press Enter

### 6️⃣ Deploy
```bash
railway up
```
- Wait 2-3 minutes
- Watch the build process
- ✓ Deployment complete!

### 7️⃣ Generate Public URL
```bash
railway domain
```
- Generates a public URL
- Example: `https://url-opener-production.up.railway.app`

### 8️⃣ DONE! 🎉

Copy the URL and share it with anyone!

---

## OR Use the Automated Script

```bash
cd ~/Downloads/ai-bootcamp-main/HDC-bootcamp/SESSION7-Agentic-coding/web_project
./deploy_railway.sh
```

This script does all the steps automatically!

---

## After Deployment

### Check if it's working:
Open the URL in your browser!

### View logs:
```bash
railway logs
```

### Open Railway dashboard:
```bash
railway open
```

### Update your app later:
```bash
# Make changes to your code
railway up
```

---

## What You'll See

**During deployment:**
```
Building...
Deploying...
✓ Deployment successful
```

**Your URL will look like:**
```
https://url-opener-production-abcd.up.railway.app
```

**That's your permanent URL to share!**

---

## Troubleshooting

### "npm command not found"
Install Node.js first:
```bash
brew install node
```

### "railway: command not found" after npm install
Try:
```bash
brew install railway
```

### Deployment fails
- Check you have credits in Railway account
- Check the logs: `railway logs`
- Try again: `railway up`

---

## Cost Reminder

- **$5 free credit** when you sign up
- Enough for ~500 hours (~1 month of continuous use)
- After that: ~$5/month

---

## Next Steps

1. ✅ Open regular terminal
2. ✅ Run the commands above
3. ✅ Get your URL
4. ✅ Share with everyone!

**It takes about 5 minutes total.** 🚀
