// Template for adding your 365 quotes and 365 music suggestions
// Copy this structure and fill in all 365 entries

// QUOTES TEMPLATE
// Replace these with your 365 unique, motivational quotes
const quotes = [
    {
        day: 1,
        quote: "The quieter you become, the more you can hear.",
        author: "Ram Dass"
    },
    {
        day: 2,
        quote: "In the depth of winter, I finally learned that there was in me an invincible summer.",
        author: "Albert Camus"
    },
    {
        day: 3,
        quote: "The present moment is the only time over which we have dominion.",
        author: "Thich Nhat Hanh"
    },
    // ... Add 362 more quotes (days 4-366)
    // Make sure each day (1-366) has exactly one quote
    // Quotes should be motivational but not cheap - thoughtful and meaningful
];

// MUSIC TEMPLATE
// Replace these with your 365 relaxing music suggestions
const music = [
    {
        day: 1,
        title: "Weightless",
        artist: "Marconi Union",
        url: "https://open.spotify.com/track/..." // Optional: Add streaming URL
    },
    {
        day: 2,
        title: "Clair de Lune",
        artist: "Claude Debussy",
        url: "https://open.spotify.com/track/..." // Optional
    },
    {
        day: 3,
        title: "Gymnopédie No. 1",
        artist: "Erik Satie",
        url: "https://open.spotify.com/track/..." // Optional
    },
    // ... Add 362 more music suggestions (days 4-366)
    // Make sure each day (1-366) has exactly one music entry
    // Focus on calming, relaxing pieces suitable for reading and thinking
];

// USAGE INSTRUCTIONS:
// 1. Fill in all 365 quotes (or 366 for leap years)
// 2. Fill in all 365 music suggestions
// 3. Copy the arrays to scripts/seedDatabase.js
// 4. Replace the sampleQuotes and sampleMusic arrays
// 5. Run: npm run seed

// TIPS FOR QUOTES:
// - Choose quotes that are meaningful and thought-provoking
// - Avoid clichéd or overly motivational quotes
// - Include diverse voices and perspectives
// - Consider quotes from literature, philosophy, science, art, etc.
// - Each quote should stand alone and be complete

// TIPS FOR MUSIC:
// - Focus on instrumental or ambient pieces
// - Avoid lyrics that might distract from reading
// - Consider classical, ambient, jazz, or minimalist compositions
// - Include a mix of genres but maintain a calming theme
// - URLs are optional but helpful for users
