# Ultimate Guide: Deploying Anjeer Desk to Render.com (Python with DANA AI)

This guide will walk you through deploying the Anjeer Desk website to Render.com step by step. **No database required** - DANA AI generates quotes algorithmically!

## Prerequisites

1. A GitHub account
2. A Render.com account (free tier works)
3. Your project code pushed to a GitHub repository
4. Python 3.8+ (for local testing)

## Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Anjeer Desk with DANA AI"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/anjeer-desk.git
   git push -u origin main
   ```

2. **Add your logo files:**
   - Place `Anjeer Desk - Logo.png` in the `public/` folder
   - Place `creator.jpg` in the `public/` folder
   - Make sure these files are committed to git

3. **Verify your files:**
   - ✅ `app.py` - Flask server with DANA AI
   - ✅ `requirements.txt` - Python dependencies
   - ✅ `public/` folder with all HTML, CSS, JS files
   - ✅ `render.yaml` - Render configuration (optional)

## Step 2: Deploy Web Service on Render

### Option A: Using Render Dashboard (Recommended)

1. **Log in to Render.com:**
   - Go to https://render.com
   - Sign up or log in with your GitHub account

2. **Create a new Web Service:**
   - Click the **"New +"** button (top right)
   - Select **"Web Service"**
   - Connect your GitHub account if not already connected
   - Select your `anjeer-desk` repository

3. **Configure the service - IMPORTANT SETTINGS:**

   **Basic Settings:**
   - **Name:** `anjeer-desk` (or any name you prefer)
   - **Region:** Choose the closest region to you (e.g., "Oregon (US West)")
   - **Branch:** `main` (or your default branch name)
   - **Root Directory:** Leave **EMPTY** (or put `./` if needed)

   **Environment Settings:**
   - **Environment:** Select **"Python 3"** (NOT Node.js!)
   - **Python Version:** Leave as default (usually 3.11 or 3.12)

   **Build & Deploy Settings:**
   - **Build Command:** 
     ```
     pip install -r requirements.txt
     ```
     *(Copy this exactly - installs Python dependencies)*
   
   - **Start Command:**
     ```
     gunicorn app:app
     ```
     *(Copy this exactly - starts the Flask server)*

   **Plan:**
   - **Plan:** Select **"Free"** (or paid if you prefer)

4. **Environment Variables (Optional):**
   - Click **"Advanced"** → **"Add Environment Variable"**
   - **Note:** For the Python version, you typically don't need any environment variables
   - Render automatically sets `PORT` for you
   - If you want to explicitly set it:
     - **Key:** `PORT`
     - **Value:** `10000`

5. **Deploy:**
   - Click **"Create Web Service"**
   - Render will automatically:
     - Clone your repository
     - Run the build command (`pip install -r requirements.txt`)
     - Start your service with the start command (`gunicorn app:app`)
   - Wait for deployment to complete (usually 2-5 minutes)
   - You'll see build logs in real-time

### Option B: Using render.yaml (Advanced)

If you've included `render.yaml` in your repository:

1. **Create a new Blueprint:**
   - In Render dashboard, click **"New +"**
   - Select **"Blueprint"**
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and configure everything

2. **Review and Deploy:**
   - Review the configuration (it should show Python environment)
   - Click **"Apply"**
   - Render will create the web service automatically

**Your render.yaml should contain:**
```yaml
services:
  - type: web
    name: anjeer-desk
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PORT
        value: 10000
```

## Step 3: Verify Deployment

1. **Check the deployment logs:**
   - In Render dashboard, go to your web service
   - Click **"Logs"** tab
   - Look for successful messages like:
     - `Installing dependencies...`
     - `Successfully installed Flask gunicorn flask-cors...`
     - `[INFO] Starting gunicorn...`
     - `Listening at: http://0.0.0.0:10000`

2. **Test your website:**
   - Click on your service URL (e.g., `https://anjeer-desk.onrender.com`)
   - Verify:
     - ✅ Page loads correctly
     - ✅ Day counter shows correctly (e.g., "Day 27 of 2026")
     - ✅ Quote appears with author
     - ✅ Border animation is visible (rectangular border with rounded corners)
     - ✅ Notes section works
     - ✅ Silence mode works
     - ✅ About page loads (`/about`)

3. **Test API endpoints:**
   - Visit: `https://your-app.onrender.com/api/quote`
     - Should return: `{"quote": "...", "author": "..."}`
   - Visit: `https://your-app.onrender.com/api/day`
     - Should return: `{"dayOfYear": 27, "year": 2026, "timestamp": ...}`
   - Visit: `https://your-app.onrender.com/health`
     - Should return: `{"status": "ok"}`

## Step 4: Custom Domain (Optional)

1. **Add custom domain:**
   - In your web service settings, go to **"Custom Domains"**
   - Click **"Add Custom Domain"**
   - Enter your domain (e.g., `desk.anjeer.com`)
   - Follow Render's DNS configuration instructions
   - Wait for DNS propagation (can take up to 48 hours)

## Troubleshooting

### Build Failures

**Error:** "pip install failed" or "No module named 'flask'"

**Solution:**
- Check `requirements.txt` exists and contains:
  ```
  Flask==3.0.0
  flask-cors==4.0.0
  gunicorn==21.2.0
  ```
- Verify you selected **"Python 3"** as the environment (NOT Node.js)
- Check build logs for specific error messages
- Make sure `app.py` is in the root directory

**Error:** "ModuleNotFoundError" or import errors

**Solution:**
- Verify all dependencies are in `requirements.txt`
- Check that `app.py` imports are correct
- Look at build logs to see which module is missing

### Start Command Issues

**Error:** "gunicorn: command not found"

**Solution:**
- Verify `gunicorn==21.2.0` is in `requirements.txt`
- Check that build command completed successfully
- Try start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

**Error:** "Address already in use" or port errors

**Solution:**
- Render automatically sets PORT - don't hardcode it
- Use: `gunicorn app:app` (gunicorn uses PORT automatically)
- Or: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Static Files Not Loading

**Error:** Logo or images not showing

**Solution:**
- Verify files are in `public/` folder
- Check file names match exactly (case-sensitive):
  - `Anjeer Desk - Logo.png` (with spaces and capital letters)
  - `creator.jpg`
- Ensure files are committed to git
- Check that `app.py` has: `static_folder='public'`

### Quote Not Appearing

**Error:** Quote shows "Loading..." or doesn't appear

**Solution:**
- Check browser console for errors (F12)
- Verify `/api/quote` endpoint works (visit it directly)
- Check Render logs for Python errors
- Verify DANA AI initialized correctly (check logs)

### Service Won't Start

**Error:** Service crashes or won't start

**Solution:**
- Check Render logs for Python traceback errors
- Verify `app.py` has correct Flask app initialization
- Make sure `if __name__ == '__main__':` block exists
- Test locally first: `python app.py`

## Render.com Commands Reference

### Via Render Dashboard:

1. **View Logs:**
   - Service → **"Logs"** tab
   - Real-time logs available
   - Shows both build and runtime logs

2. **Manual Deploy:**
   - Service → **"Manual Deploy"** → **"Deploy latest commit"**
   - Useful for testing changes

3. **Environment Variables:**
   - Service → **"Environment"** → **"Add Environment Variable"**
   - For Python version, usually not needed

4. **Restart Service:**
   - Service → **"Manual Deploy"** → **"Clear build cache & deploy"**
   - Useful if something goes wrong

### Configuration Summary

**What to put in Render Dashboard:**

| Field | Value |
|-------|-------|
| **Name** | `anjeer-desk` |
| **Environment** | `Python 3` |
| **Region** | Your choice (e.g., "Oregon (US West)") |
| **Branch** | `main` |
| **Root Directory** | *(leave empty)* |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | `Free` |

**Environment Variables (usually not needed):**
- `PORT` - Automatically set by Render (optional to set to `10000`)

## Important Notes

1. **Free Tier Limitations:**
   - Services spin down after 15 minutes of inactivity
   - First request after spin-down may take 30-60 seconds (cold start)
   - Consider upgrading to paid plan for always-on service

2. **No Database Needed:**
   - DANA AI generates quotes algorithmically
   - No database setup required
   - No database connection strings needed
   - Saves on free tier limitations!

3. **Environment Variables:**
   - Never commit `.env` file to git
   - For Python version, you typically don't need any env vars
   - Render automatically provides `PORT`

4. **Auto-Deploy:**
   - Render auto-deploys on git push by default
   - Disable in service settings if needed
   - Use manual deploy for testing

5. **DANA AI:**
   - Quotes are generated deterministically
   - Same day always shows same quote
   - Quotes repeat annually
   - No database queries needed

## Maintenance

### Updating Quotes:

1. **Edit app.py:**
   - Find the `quote_pool` list in the `DANA_AI` class
   - Add or modify quotes
   - Commit and push changes
   - Render will auto-deploy

2. **No Database to Update:**
   - All quotes are in `app.py`
   - Just edit and push - that's it!

### Monitoring:

- Check Render dashboard regularly
- Monitor logs for errors
- Set up alerts for service downtime (paid plans)
- Check `/health` endpoint for service status

## Local Testing Before Deployment

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python app.py

# Or with gunicorn (production-like)
gunicorn app:app

# Test endpoints
curl http://localhost:5000/api/quote
curl http://localhost:5000/api/day
curl http://localhost:5000/health
```

## Support

- Render Documentation: https://render.com/docs
- Render Support: support@render.com
- Community: https://community.render.com
- Flask Documentation: https://flask.palletsprojects.com/
- Gunicorn Documentation: https://gunicorn.org/

---

## Quick Reference Card

**For Render Dashboard:**

```
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Plan: Free
```

**No database needed!** DANA AI handles everything.

---

**Congratulations!** Your Anjeer Desk is now live on Render.com. The website will automatically show a thoughtful quote each day, powered by DANA AI, providing a quiet digital space for focused presence.
