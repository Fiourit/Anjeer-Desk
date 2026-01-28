# Quick Start Guide

Get Anjeer Desk running locally in 5 minutes.

## Prerequisites Check

- [ ] Node.js installed (v18+)
- [ ] PostgreSQL installed and running
- [ ] Logo files ready (`Anjeer Desk - Logo.png` and `creator.jpg`)

## Steps

### 1. Install Dependencies
```bash
npm install
```

### 2. Set Up Database

Create a PostgreSQL database:
```bash
createdb anjeer_desk
```

Or using psql:
```sql
CREATE DATABASE anjeer_desk;
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:
```
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/anjeer_desk
PORT=3000
NODE_ENV=development
```

### 4. Create Database Tables

```bash
psql -U your_username -d anjeer_desk -f database/schema.sql
```

### 5. Add Logo Files

Copy your logo files to `public/`:
- `Anjeer Desk - Logo.png`
- `creator.jpg`

### 6. Seed Database (Optional for Testing)

Edit `scripts/seedDatabase.js` with at least a few sample quotes and music, then:
```bash
npm run seed
```

**Note:** You'll need to add all 365 quotes and 365 music suggestions before deploying to production.

### 7. Start Server

```bash
npm start
```

Or for development with auto-reload:
```bash
npm run dev
```

### 8. Visit

- Main page: http://localhost:3000
- About page: http://localhost:3000/about

## Next Steps

1. Add all 365 quotes to `scripts/seedDatabase.js`
2. Add all 365 music suggestions to `scripts/seedDatabase.js`
3. Re-seed database: `npm run seed`
4. Deploy to Render.com (see `RENDER_DEPLOYMENT_GUIDE.md`)

## Troubleshooting

**Database connection error?**
- Check PostgreSQL is running
- Verify DATABASE_URL in `.env` is correct
- Test connection: `psql "YOUR_DATABASE_URL"`

**Port already in use?**
- Change PORT in `.env` to a different number (e.g., 3001)
- Or stop the process using port 3000

**Logo not showing?**
- Check file names match exactly (case-sensitive)
- Verify files are in `public/` folder
- Check browser console for 404 errors
