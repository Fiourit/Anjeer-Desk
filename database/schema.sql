-- Create quotes table
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    day_of_year INTEGER NOT NULL UNIQUE CHECK (day_of_year >= 1 AND day_of_year <= 366),
    quote TEXT NOT NULL,
    author VARCHAR(255)
);

-- Create music table
CREATE TABLE IF NOT EXISTS music (
    id SERIAL PRIMARY KEY,
    day_of_year INTEGER NOT NULL UNIQUE CHECK (day_of_year >= 1 AND day_of_year <= 366),
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    url TEXT
);

-- Create indexes for faster lookups
CREATE INDEX IF NOT EXISTS idx_quotes_day ON quotes(day_of_year);
CREATE INDEX IF NOT EXISTS idx_music_day ON music(day_of_year);
