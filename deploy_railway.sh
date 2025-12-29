#!/bin/bash
# Quick Railway Deployment Script
# Run this in a REGULAR TERMINAL (not Claude Code)

echo "============================================="
echo "Railway Quick Deployment"
echo "============================================="
echo ""

# Step 1: Install Railway CLI
echo "Step 1: Installing Railway CLI..."
npm i -g @railway/cli

if [ $? -ne 0 ]; then
    echo "❌ Installation failed. Try using brew instead:"
    echo "   brew install railway"
    exit 1
fi

echo "✓ Railway CLI installed"
echo ""

# Step 2: Login
echo "Step 2: Login to Railway..."
echo "This will open a browser window for authentication."
railway login

if [ $? -ne 0 ]; then
    echo "❌ Login failed"
    exit 1
fi

echo "✓ Logged in"
echo ""

# Step 3: Initialize project
echo "Step 3: Initializing Railway project..."
railway init

if [ $? -ne 0 ]; then
    echo "❌ Initialization failed"
    exit 1
fi

echo "✓ Project initialized"
echo ""

# Step 4: Deploy
echo "Step 4: Deploying to Railway..."
echo "This may take 2-3 minutes..."
railway up

if [ $? -ne 0 ]; then
    echo "❌ Deployment failed"
    exit 1
fi

echo "✓ Deployed successfully!"
echo ""

# Step 5: Generate domain
echo "Step 5: Generating public URL..."
railway domain

echo ""
echo "============================================="
echo "✓ DEPLOYMENT COMPLETE!"
echo "============================================="
echo ""
echo "Your app is now live!"
echo "Copy the URL above and share it with anyone."
echo ""
echo "To check status: railway status"
echo "To view logs: railway logs"
echo "To open dashboard: railway open"
echo ""
