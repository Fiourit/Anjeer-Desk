require('dotenv').config();
const { Pool } = require('pg');
const fs = require('fs');
const path = require('path');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false
});

// Import complete data
const { allQuotes, allMusic } = require('./complete-data.js');

const sampleQuotes = allQuotes;
const sampleMusic = allMusic;

async function seedDatabase() {
  try {
    console.log('Starting database seed...');
    
    // Clear existing data
    await pool.query('DELETE FROM quotes');
    await pool.query('DELETE FROM music');
    
    // Insert quotes
    console.log('Inserting quotes...');
    for (const quote of sampleQuotes) {
      await pool.query(
        'INSERT INTO quotes (day_of_year, quote, author) VALUES ($1, $2, $3)',
        [quote.day, quote.quote, quote.author]
      );
    }
    
    // Insert music
    console.log('Inserting music...');
    for (const music of sampleMusic) {
      await pool.query(
        'INSERT INTO music (day_of_year, title, artist, url) VALUES ($1, $2, $3, $4)',
        [music.day, music.title, music.artist, music.url]
      );
    }
    
    console.log('Database seeded successfully!');
    console.log(`Inserted ${sampleQuotes.length} quotes and ${sampleMusic.length} music entries.`);
    
  } catch (error) {
    console.error('Error seeding database:', error);
  } finally {
    await pool.end();
  }
}

seedDatabase();
