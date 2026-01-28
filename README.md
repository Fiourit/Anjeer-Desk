# Anjeer Desk

A digital space for time, reading, and quiet attention.

Anjeer Desk is a minimal digital environment designed to hold a single day of focused presence. It exists as part of FIOURIT Insight and serves as the digital counterpart to Anjeer House—offering a quiet, solitary space for reading, studying, and thinking without demand or distraction.

## Features

- **Continuous Time Display**: Seconds move forward continuously, without alarms or segmentation
- **Day Counter**: Shows your position within the year (Day X of YYYY)
- **24-Hour Border Animation**: A slow-evolving border that completes one cycle every twenty-four hours
- **Daily Quote**: One sentence per day from a collection of 365 voices, repeating annually
- **Music Suggestion**: A single calming musical piece suggested each day
- **Private Notes**: A writing space stored only on your device, with no save confirmation or export
- **Silence Mode**: Hide quote and music, leaving only time and the page itself
- **Daily Acknowledgment**: A brief, human message that appears once per day

## Technology Stack

- **Backend**: Node.js + Express
- **Database**: PostgreSQL
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Deployment**: Render.com

## Local Development

### Prerequisites

- Node.js (v18 or higher)
- PostgreSQL database
- npm or yarn

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd anjeer-desk
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your database connection string:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/anjeer_desk
   PORT=3000
   NODE_ENV=development
   ```

4. **Set up database:**
   ```bash
   # Connect to PostgreSQL and run schema
   psql -U postgres -d anjeer_desk -f database/schema.sql
   ```

5. **Seed the database:**
   - Edit `scripts/seedDatabase.js` to add your 365 quotes and 365 music suggestions
   - Run: `npm run seed`

6. **Add logo files:**
   - Place `Anjeer Desk - Logo.png` in `public/` folder
   - Place `creator.jpg` in `public/` folder

7. **Start the server:**
   ```bash
   npm start
   # or for development with auto-reload:
   npm run dev
   ```

8. **Visit:**
   - Main page: http://localhost:3000
   - About page: http://localhost:3000/about

## Deployment

See [RENDER_DEPLOYMENT_GUIDE.md](./RENDER_DEPLOYMENT_GUIDE.md) for a complete step-by-step guide to deploying on Render.com.

## Project Structure

```
anjeer-desk/
├── public/              # Frontend files
│   ├── index.html      # Main page
│   ├── about.html      # About page
│   ├── styles.css      # Styles
│   ├── script.js       # Frontend logic
│   ├── Anjeer Desk - Logo.png  # Logo (add this)
│   └── creator.jpg     # Creator image (add this)
├── database/
│   └── schema.sql      # Database schema
├── scripts/
│   └── seedDatabase.js # Database seeding script
├── server.js           # Express server
├── package.json        # Dependencies
├── render.yaml         # Render.com configuration
└── README.md           # This file
```

## API Endpoints

- `GET /api/quote` - Get today's quote
- `GET /api/music` - Get today's music suggestion
- `GET /api/day` - Get current day information
- `GET /health` - Health check endpoint

## Data Requirements

### Quotes
- 365 unique quotes (one for each day of the year)
- Each quote should have: `day_of_year` (1-366), `quote` (text), `author` (optional)

### Music
- 365 music suggestions (one for each day)
- Each entry should have: `day_of_year` (1-366), `title`, `artist`, `url` (optional)

## Design Philosophy

Anjeer Desk does not:
- Organize tasks or track progress
- Measure performance or optimize productivity
- Adapt to behavior or respond to attention
- Claim memory or provide archives

Anjeer Desk does:
- Provide a calm structure for time to pass visibly
- Allow attention to remain unextracted
- Support reading and thinking by removing distractions
- Hold time gently, one day at a time

## License

ISC

## Creator

MHJ - Creator of Anjeer Desk

Website: https://fiourit.com/
