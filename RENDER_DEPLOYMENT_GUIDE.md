# Ultimate Guide: Deploying Anjeer Desk to Render.com

This guide will walk you through deploying the Anjeer Desk website to Render.com step by step.

## Prerequisites

1. A GitHub account
2. A Render.com account (free tier works)
3. Your project code pushed to a GitHub repository

## Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Anjeer Desk"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/anjeer-desk.git
   git push -u origin main
   ```

2. **Add your logo files:**
   - Place `Anjeer Desk - Logo.png` in the `public/` folder
   - Place `creator.jpg` in the `public/` folder

## Step 2: Create PostgreSQL Database on Render

1. **Log in to Render.com:**
   - Go to https://render.com
   - Sign up or log in

2. **Create a PostgreSQL Database:**
   - Click "New +" button
   - Select "PostgreSQL"
   - Configure:
     - **Name:** `anjeer-desk-db`
     - **Database:** `anjeer_desk`
     - **User:** `anjeer_desk_user`
     - **Region:** Choose closest to you
     - **Plan:** Free (or paid if preferred)
   - Click "Create Database"
   - **IMPORTANT:** Copy the "Internal Database URL" - you'll need this later

## Step 3: Set Up Database Schema

1. **Get the connection string:**
   - In Render dashboard, go to your database
   - Copy the "Internal Database URL" (format: `postgresql://user:password@host:port/database`)

2. **Connect to your database locally (optional but recommended):**
   ```bash
   # Install PostgreSQL client tools if needed
   # On Windows: Download from postgresql.org
   # On Mac: brew install postgresql
   # On Linux: sudo apt-get install postgresql-client
   
   # Connect using psql
   psql "YOUR_DATABASE_URL"
   ```

3. **Run the schema:**
   ```bash
   # Option 1: Using psql
   psql "YOUR_DATABASE_URL" -f database/schema.sql
   
   # Option 2: Copy and paste the contents of database/schema.sql into psql
   ```

   Or use the Render database dashboard's "Connect" feature and run:
   ```sql
   -- Copy contents from database/schema.sql
   CREATE TABLE IF NOT EXISTS quotes (
       id SERIAL PRIMARY KEY,
       day_of_year INTEGER NOT NULL UNIQUE CHECK (day_of_year >= 1 AND day_of_year <= 366),
       quote TEXT NOT NULL,
       author VARCHAR(255)
   );
   
   CREATE TABLE IF NOT EXISTS music (
       id SERIAL PRIMARY KEY,
       day_of_year INTEGER NOT NULL UNIQUE CHECK (day_of_year >= 1 AND day_of_year <= 366),
       title VARCHAR(255) NOT NULL,
       artist VARCHAR(255) NOT NULL,
       url TEXT
   );
   
   CREATE INDEX IF NOT EXISTS idx_quotes_day ON quotes(day_of_year);
   CREATE INDEX IF NOT EXISTS idx_music_day ON music(day_of_year);
   ```

## Step 4: Seed the Database

1. **Set up environment variable locally:**
   ```bash
   # Create .env file
   cp .env.example .env
   ```

2. **Edit .env file:**
   ```
   DATABASE_URL=YOUR_DATABASE_URL_FROM_RENDER
   PORT=3000
   NODE_ENV=development
   ```

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Prepare your data:**
   - Edit `scripts/seedDatabase.js`
   - Add all 365 quotes (replace the sample quotes)
   - Add all 365 music suggestions (replace the sample music)

5. **Run the seed script:**
   ```bash
   npm run seed
   ```

   **Important:** Make sure you have all 365 quotes and 365 music entries before deploying!

## Step 5: Deploy Web Service on Render

### Option A: Using Render Dashboard (Recommended for first-time users)

1. **Create a new Web Service:**
   - In Render dashboard, click "New +"
   - Select "Web Service"
   - Connect your GitHub repository
   - Select the `anjeer-desk` repository

2. **Configure the service:**
   - **Name:** `anjeer-desk`
   - **Environment:** `Node`
   - **Region:** Same as your database
   - **Branch:** `main` (or your default branch)
   - **Root Directory:** Leave empty (or `./` if needed)
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`

3. **Add Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Add:
     - **Key:** `NODE_ENV`
     - **Value:** `production`
   - Add:
     - **Key:** `DATABASE_URL`
     - **Value:** Your database's "Internal Database URL" from Step 2
   - Add:
     - **Key:** `PORT`
     - **Value:** `10000` (Render uses port 10000 by default)

4. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Wait for deployment to complete (usually 2-5 minutes)

### Option B: Using render.yaml (Advanced)

If you've included `render.yaml` in your repository:

1. **Create a new Blueprint:**
   - In Render dashboard, click "New +"
   - Select "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and configure everything

2. **Review and Deploy:**
   - Review the configuration
   - Click "Apply"
   - Render will create both the database and web service

## Step 6: Verify Deployment

1. **Check the deployment logs:**
   - In Render dashboard, go to your web service
   - Click "Logs" tab
   - Look for "Anjeer Desk server running on port 10000"

2. **Test your website:**
   - Click on your service URL (e.g., `https://anjeer-desk.onrender.com`)
   - Verify:
     - Clock is running
     - Day counter shows correctly
     - Quote appears
     - Music suggestion appears
     - Border animation is visible
     - Notes section works
     - Silence mode works
     - About page loads

3. **Test API endpoints:**
   - Visit: `https://your-app.onrender.com/api/quote`
   - Visit: `https://your-app.onrender.com/api/music`
   - Visit: `https://your-app.onrender.com/api/day`

## Step 7: Custom Domain (Optional)

1. **Add custom domain:**
   - In your web service settings, go to "Custom Domains"
   - Add your domain (e.g., `desk.anjeer.com`)
   - Follow Render's DNS configuration instructions

## Troubleshooting

### Database Connection Issues

**Error:** "Connection refused" or "Database not found"

**Solution:**
- Verify `DATABASE_URL` environment variable is set correctly
- Use "Internal Database URL" (not external) for Render services
- Check database is running in Render dashboard

### Build Failures

**Error:** "npm install failed"

**Solution:**
- Check `package.json` is valid
- Ensure Node.js version is compatible (Render uses Node 18+ by default)
- Check build logs for specific errors

### Missing Quotes/Music

**Error:** "Quote not found for today"

**Solution:**
- Verify database is seeded with all 365 entries
- Check day_of_year values are 1-366
- Re-run seed script if needed

### Static Files Not Loading

**Error:** Logo or images not showing

**Solution:**
- Verify files are in `public/` folder
- Check file names match exactly (case-sensitive)
- Ensure files are committed to git

### Port Issues

**Error:** "Port already in use"

**Solution:**
- Render uses port 10000 by default
- Ensure `PORT` environment variable is set to `10000`
- Or use `process.env.PORT` in server.js (already configured)

## Render.com Commands Reference

### Via Render Dashboard:

1. **View Logs:**
   - Service → Logs tab
   - Real-time logs available

2. **Manual Deploy:**
   - Service → Manual Deploy → Deploy latest commit

3. **Environment Variables:**
   - Service → Environment → Add/Edit variables

4. **Database Access:**
   - Database → Connect → Use provided connection string

### Via Render CLI (Optional):

```bash
# Install Render CLI
npm install -g render-cli

# Login
render login

# Deploy
render deploy

# View logs
render logs

# List services
render services list
```

## Important Notes

1. **Free Tier Limitations:**
   - Services spin down after 15 minutes of inactivity
   - First request after spin-down may take 30-60 seconds
   - Consider upgrading to paid plan for always-on service

2. **Database Backups:**
   - Free tier databases are backed up daily
   - Paid plans offer more frequent backups
   - Export your data regularly as backup

3. **Environment Variables:**
   - Never commit `.env` file to git
   - Always set sensitive variables in Render dashboard
   - Use "Internal Database URL" for services on same account

4. **Auto-Deploy:**
   - Render auto-deploys on git push by default
   - Disable in service settings if needed
   - Use manual deploy for production releases

## Maintenance

### Updating Quotes/Music:

1. **Edit seed script:**
   - Update `scripts/seedDatabase.js`
   - Commit and push changes

2. **Re-seed database:**
   ```bash
   # Connect to database
   psql "YOUR_DATABASE_URL"
   
   # Clear existing data
   DELETE FROM quotes;
   DELETE FROM music;
   
   # Run seed script locally
   npm run seed
   ```

### Monitoring:

- Check Render dashboard regularly
- Monitor logs for errors
- Set up alerts for service downtime (paid plans)

## Support

- Render Documentation: https://render.com/docs
- Render Support: support@render.com
- Community: https://community.render.com

---

**Congratulations!** Your Anjeer Desk is now live on Render.com. The website will automatically update quotes and music suggestions each day, providing a quiet digital space for focused presence.
