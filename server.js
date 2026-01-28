require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000; // Render.com uses PORT env variable automatically

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Database connection
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false
});

// Helper function to get day of year (1-365/366)
function getDayOfYear() {
  const now = new Date();
  const start = new Date(now.getFullYear(), 0, 0);
  const diff = now - start;
  const oneDay = 1000 * 60 * 60 * 24;
  const day = Math.floor(diff / oneDay);
  return day;
}

// API: Get quote for today
app.get('/api/quote', async (req, res) => {
  try {
    const dayOfYear = getDayOfYear();
    const result = await pool.query(
      'SELECT quote, author FROM quotes WHERE day_of_year = $1',
      [dayOfYear]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Quote not found for today' });
    }
    
    res.json(result.rows[0]);
  } catch (error) {
    console.error('Error fetching quote:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API: Get music suggestion for today
app.get('/api/music', async (req, res) => {
  try {
    const dayOfYear = getDayOfYear();
    const result = await pool.query(
      'SELECT title, artist, url FROM music WHERE day_of_year = $1',
      [dayOfYear]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Music not found for today' });
    }
    
    res.json(result.rows[0]);
  } catch (error) {
    console.error('Error fetching music:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API: Get current day info
app.get('/api/day', (req, res) => {
  const dayOfYear = getDayOfYear();
  const now = new Date();
  const year = now.getFullYear();
  
  res.json({
    dayOfYear,
    year,
    timestamp: now.getTime()
  });
});

// Serve main page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Serve about page
app.get('/about', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'about.html'));
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(PORT, () => {
  console.log(`Anjeer Desk server running on port ${PORT}`);
});
