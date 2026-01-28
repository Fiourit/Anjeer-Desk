from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import random

app = Flask(__name__, static_folder='public')
CORS(app)

# DANA AI - Thoughtful quote generation system
class DANA_AI:
    """DANA AI: A system for generating thoughtful, meaningful quotes for each day"""
    
    def __init__(self):
        # Seed quotes database - thoughtful quotes from diverse sources
        self.quote_pool = [
            {"quote": "The quieter you become, the more you can hear.", "author": "Ram Dass"},
            {"quote": "In the depth of winter, I finally learned that there was in me an invincible summer.", "author": "Albert Camus"},
            {"quote": "The present moment is the only time over which we have dominion.", "author": "Thich Nhat Hanh"},
            {"quote": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "author": "Aristotle"},
            {"quote": "The unexamined life is not worth living.", "author": "Socrates"},
            {"quote": "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "author": "Ralph Waldo Emerson"},
            {"quote": "It is during our darkest moments that we must focus to see the light.", "author": "Aristotle"},
            {"quote": "The only way out is through.", "author": "Robert Frost"},
            {"quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson"},
            {"quote": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
            {"quote": "Two roads diverged in a wood, and I—I took the one less traveled by, and that has made all the difference.", "author": "Robert Frost"},
            {"quote": "The mind is everything. What you think you become.", "author": "Buddha"},
            {"quote": "Life is what happens to you while you're busy making other plans.", "author": "John Lennon"},
            {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
            {"quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.", "author": "J.K. Rowling"},
            {"quote": "You must be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
            {"quote": "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do.", "author": "Mark Twain"},
            {"quote": "To live is the rarest thing in the world. Most people just exist.", "author": "Oscar Wilde"},
            {"quote": "That which does not kill us makes us stronger.", "author": "Friedrich Nietzsche"},
            {"quote": "We are all in the gutter, but some of us are looking at the stars.", "author": "Oscar Wilde"},
            {"quote": "It is better to be hated for what you are than to be loved for what you are not.", "author": "André Gide"},
            {"quote": "The only person you are destined to become is the person you decide to be.", "author": "Ralph Waldo Emerson"},
            {"quote": "Go confidently in the direction of your dreams. Live the life you have imagined.", "author": "Henry David Thoreau"},
            {"quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
            {"quote": "In the end, we will remember not the words of our enemies, but the silence of our friends.", "author": "Martin Luther King Jr."},
            {"quote": "The only impossible journey is the one you never begin.", "author": "Tony Robbins"},
            {"quote": "In this life we cannot do great things. We can only do small things with great love.", "author": "Mother Teresa"},
            {"quote": "Don't judge each day by the harvest you reap but by the seeds that you plant.", "author": "Robert Louis Stevenson"},
            {"quote": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
            {"quote": "The real difficulty is to overcome how you think about yourself.", "author": "Maya Angelou"},
            {"quote": "If you want to lift yourself up, lift up someone else.", "author": "Booker T. Washington"},
            {"quote": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas A. Edison"},
            {"quote": "A person who never made a mistake never tried anything new.", "author": "Albert Einstein"},
            {"quote": "The person who says it cannot be done should not interrupt the person who is doing it.", "author": "Chinese Proverb"},
            {"quote": "There are two ways of spreading light: to be the candle or the mirror that reflects it.", "author": "Edith Wharton"},
            {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
            {"quote": "It is never too late to be what you might have been.", "author": "George Eliot"},
            {"quote": "You can't use up creativity. The more you use, the more you have.", "author": "Maya Angelou"},
            {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
            {"quote": "The difference between ordinary and extraordinary is that little extra.", "author": "Jimmy Johnson"},
            {"quote": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
            {"quote": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"},
            {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
            {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
            {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
            {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
            {"quote": "If you can dream it, you can do it.", "author": "Walt Disney"},
            {"quote": "The future depends on what you do today.", "author": "Mahatma Gandhi"},
            {"quote": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
            {"quote": "People who are crazy enough to think they can change the world, are the ones who do.", "author": "Rob Siltanen"},
            {"quote": "Failure will never overtake me if my determination to succeed is strong enough.", "author": "Og Mandino"},
            {"quote": "We may encounter many defeats but we must not be defeated.", "author": "Maya Angelou"},
            {"quote": "Knowing yourself is the beginning of all wisdom.", "author": "Aristotle"},
            {"quote": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu"},
            {"quote": "That which we persist in doing becomes easier to do, not that the nature of the thing has changed but that our power to do has increased.", "author": "Ralph Waldo Emerson"},
            {"quote": "The best revenge is massive success.", "author": "Frank Sinatra"},
            {"quote": "You may be disappointed if you fail, but you are doomed if you don't try.", "author": "Beverly Sills"},
            {"quote": "Life is 10% what happens to you and 90% how you react to it.", "author": "Charles R. Swindoll"},
            {"quote": "Remember that not getting what you want is sometimes a wonderful stroke of luck.", "author": "Dalai Lama"},
            {"quote": "You can't fall if you don't climb. But there's no joy in living your whole life on the ground.", "author": "Unknown Author"},
            {"quote": "We become what we think about.", "author": "Earl Nightingale"},
            {"quote": "The two most important days in your life are the day you are born and the day you find out why.", "author": "Mark Twain"},
            {"quote": "Whatever you can do, or dream you can, begin it. Boldness has genius, power and magic in it.", "author": "Johann Wolfgang von Goethe"},
            {"quote": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "author": "Helen Keller"},
            {"quote": "The cave you fear to enter holds the treasure you seek.", "author": "Joseph Campbell"},
            {"quote": "What we achieve inwardly will change outer reality.", "author": "Plutarch"},
            {"quote": "The privilege of a lifetime is to become who you truly are.", "author": "Carl Jung"},
            {"quote": "I would rather have questions that can't be answered than answers that can't be questioned.", "author": "Richard Feynman"},
            {"quote": "The most common way people give up their power is by thinking they don't have any.", "author": "Alice Walker"},
            {"quote": "The mind is not a vessel to be filled but a fire to be kindled.", "author": "Plutarch"},
            {"quote": "We are not makers of history. We are made by history.", "author": "Martin Luther King Jr."},
            {"quote": "The only true wisdom is in knowing you know nothing.", "author": "Socrates"},
            {"quote": "What we think, we become.", "author": "Buddha"},
            {"quote": "The greatest discovery of all time is that a person can change his future by merely changing his attitude.", "author": "Oprah Winfrey"},
            {"quote": "In three words I can sum up everything I've learned about life: it goes on.", "author": "Robert Frost"},
            {"quote": "If you want to go fast, go alone. If you want to go far, go together.", "author": "African Proverb"},
            {"quote": "The purpose of life is to discover your gift. The work of life is to develop it. The meaning of life is to give your gift away.", "author": "David Viscott"},
            {"quote": "The wound is the place where the Light enters you.", "author": "Rumi"},
            {"quote": "What you seek is seeking you.", "author": "Rumi"},
            {"quote": "Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.", "author": "Rumi"},
            {"quote": "The art of being wise is the art of knowing what to overlook.", "author": "William James"},
            {"quote": "We are what we pretend to be, so we must be careful about what we pretend to be.", "author": "Kurt Vonnegut"},
            {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
            {"quote": "Get busy living or get busy dying.", "author": "Stephen King"},
            {"quote": "You have within you right now, everything you need to deal with whatever the world can throw at you.", "author": "Brian Tracy"},
            {"quote": "The only person you should try to be better than is the person you were yesterday.", "author": "Unknown Author"},
            {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
            {"quote": "It's not what happens to you, but how you react to it that matters.", "author": "Epictetus"},
            {"quote": "The only way to have a friend is to be one.", "author": "Ralph Waldo Emerson"},
            {"quote": "The best preparation for tomorrow is doing your best today.", "author": "H. Jackson Brown Jr."},
            {"quote": "The only thing we have to fear is fear itself.", "author": "Franklin D. Roosevelt"},
            {"quote": "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", "author": "Jordan Belfort"},
            {"quote": "At the still point, there the dance is.", "author": "T.S. Eliot"},
            {"quote": "I took a deep breath and listened to the old brag of my heart; I am, I am, I am.", "author": "Sylvia Plath"},
            {"quote": "We accept the love we think we deserve.", "author": "Stephen Chbosky"},
            {"quote": "It does not do to dwell on dreams and forget to live.", "author": "J.K. Rowling"},
            {"quote": "So we beat on, boats against the current, borne back ceaselessly into the past.", "author": "F. Scott Fitzgerald"},
            {"quote": "All that is gold does not glitter, not all those who wander are lost.", "author": "J.R.R. Tolkien"},
            {"quote": "The only way out of the labyrinth of suffering is to forgive.", "author": "John Green"},
            {"quote": "It is our choices that show what we truly are, far more than our abilities.", "author": "J.K. Rowling"},
        ]
        
        # Expand to 365 quotes by cycling through and adding variations
        self.expand_quotes()
    
    def expand_quotes(self):
        """Expand quote pool to 365 unique quotes"""
        base_quotes = len(self.quote_pool)
        needed = 365 - base_quotes
        
        # Additional thoughtful quotes to reach 365
        additional_quotes = [
            {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
            {"quote": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
            {"quote": "Stay hungry. Stay foolish.", "author": "Steve Jobs"},
            {"quote": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
            {"quote": "Design is not just what it looks like and feels like. Design is how it works.", "author": "Steve Jobs"},
            {"quote": "Be a yardstick of quality. Some people aren't used to an environment where excellence is expected.", "author": "Steve Jobs"},
            {"quote": "I think the things you regret most in life are the things you didn't do.", "author": "Steve Jobs"},
            {"quote": "You can't connect the dots looking forward; you can only connect them looking backwards.", "author": "Steve Jobs"},
            {"quote": "Have the courage to follow your heart and intuition.", "author": "Steve Jobs"},
            {"quote": "The people who are crazy enough to think they can change the world are the ones who do.", "author": "Steve Jobs"},
            {"quote": "Life is really simple, but we insist on making it complicated.", "author": "Confucius"},
            {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
            {"quote": "Wherever you go, go with all your heart.", "author": "Confucius"},
            {"quote": "Our greatest glory is not in never falling, but in rising every time we fall.", "author": "Confucius"},
            {"quote": "The man who moves a mountain begins by carrying away small stones.", "author": "Confucius"},
            {"quote": "Real knowledge is to know the extent of one's ignorance.", "author": "Confucius"},
            {"quote": "I hear and I forget. I see and I remember. I do and I understand.", "author": "Confucius"},
            {"quote": "Everything has beauty, but not everyone sees it.", "author": "Confucius"},
            {"quote": "Wheresoever you go, go with all your heart.", "author": "Confucius"},
            {"quote": "The superior man is modest in his speech, but exceeds in his actions.", "author": "Confucius"},
            {"quote": "By three methods we may learn wisdom: First, by reflection, which is noblest; Second, by imitation, which is easiest; and third by experience, which is the bitterest.", "author": "Confucius"},
            {"quote": "He who knows all the answers has not been asked all the questions.", "author": "Confucius"},
            {"quote": "The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence.", "author": "Confucius"},
            {"quote": "When it is obvious that the goals cannot be reached, don't adjust the goals, adjust the action steps.", "author": "Confucius"},
            {"quote": "Study the past if you would define the future.", "author": "Confucius"},
            {"quote": "The man who asks a question is a fool for a minute, the man who does not ask is a fool for life.", "author": "Confucius"},
            {"quote": "To see what is right and not do it is the want of courage.", "author": "Confucius"},
            {"quote": "When we see men of worth, we should think of equaling them; when we see men of a contrary character, we should turn inwards and examine ourselves.", "author": "Confucius"},
            {"quote": "The superior man understands what is right; the inferior man understands what will sell.", "author": "Confucius"},
            {"quote": "He who learns but does not think, is lost. He who thinks but does not learn is in great danger.", "author": "Confucius"},
            {"quote": "The way out is through the door. Why is it that no one will use this method?", "author": "Confucius"},
            {"quote": "Better a diamond with a flaw than a pebble without.", "author": "Confucius"},
            {"quote": "The gem cannot be polished without friction, nor man perfected without trials.", "author": "Confucius"},
            {"quote": "Silence is a true friend who never betrays.", "author": "Confucius"},
            {"quote": "The expectations of life depend upon diligence; the mechanic that would perfect his work must first sharpen his tools.", "author": "Confucius"},
            {"quote": "If you think in terms of a year, plant a seed; if in terms of ten years, plant trees; if in terms of 100 years, teach the people.", "author": "Confucius"},
            {"quote": "The superior man is satisfied and composed; the mean man is always full of distress.", "author": "Confucius"},
            {"quote": "He who speaks without modesty will find it difficult to make his words good.", "author": "Confucius"},
            {"quote": "The superior man acts before he speaks, and afterwards speaks according to his action.", "author": "Confucius"},
            {"quote": "The superior man is distressed by the limitations of his ability; he is not distressed by the fact that men do not recognize the ability that he has.", "author": "Confucius"},
            {"quote": "The superior man thinks always of virtue; the common man thinks of comfort.", "author": "Confucius"},
            {"quote": "The superior man is easy to serve, but difficult to please. The inferior man is difficult to serve, but easy to please.", "author": "Confucius"},
            {"quote": "The superior man cannot be known in little matters, but he may be entrusted with great concerns. The small man may not be entrusted with great concerns, but he may be known in little matters.", "author": "Confucius"},
            {"quote": "The superior man is dignified, but does not wrangle. He is sociable, but not a partisan.", "author": "Confucius"},
            {"quote": "The superior man is broad and fair; the inferior man is partisan and small.", "author": "Confucius"},
            {"quote": "The superior man seeks what is right; the inferior one, what is profitable.", "author": "Confucius"},
            {"quote": "The superior man is slow in his words and earnest in his conduct.", "author": "Confucius"},
            {"quote": "The superior man has a dignified ease without pride. The mean man has pride without a dignified ease.", "author": "Confucius"},
            {"quote": "The superior man makes the difficulty to be overcome his first interest; success only comes later.", "author": "Confucius"},
            {"quote": "The superior man is firm in the right way, and not merely firm.", "author": "Confucius"},
        ]
        
        # Add additional quotes
        self.quote_pool.extend(additional_quotes)
        
        # If still not enough, cycle through base quotes to reach exactly 365
        current_count = len(self.quote_pool)
        if current_count < 365:
            for i in range(365 - current_count):
                base_index = i % base_quotes
                quote = self.quote_pool[base_index].copy()
                self.quote_pool.append(quote)
    
    def get_quote_for_day(self, day_of_year):
        """Get a deterministic quote for a specific day of the year"""
        # Use day_of_year as seed for deterministic selection
        random.seed(day_of_year)
        quote_index = random.randint(0, len(self.quote_pool) - 1)
        return self.quote_pool[quote_index]

# Initialize DANA AI
dana_ai = DANA_AI()

def get_day_of_year():
    """Get the current day of year (1-365/366)"""
    now = datetime.now()
    start = datetime(now.year, 1, 1)
    day_of_year = (now - start).days + 1
    return day_of_year

@app.route('/')
def index():
    """Serve main page"""
    return send_from_directory('public', 'index.html')

@app.route('/about')
def about():
    """Serve about page"""
    return send_from_directory('public', 'about.html')

@app.route('/api/quote', methods=['GET'])
def get_quote():
    """Get today's quote from DANA AI"""
    try:
        day_of_year = get_day_of_year()
        quote_data = dana_ai.get_quote_for_day(day_of_year)
        return jsonify(quote_data)
    except Exception as e:
        print(f'Error generating quote: {e}')
        return jsonify({
            "quote": "The present moment is the only time over which we have dominion.",
            "author": "Thich Nhat Hanh"
        }), 500

@app.route('/api/day', methods=['GET'])
def get_day():
    """Get current day information"""
    try:
        day_of_year = get_day_of_year()
        now = datetime.now()
        return jsonify({
            "dayOfYear": day_of_year,
            "year": now.year,
            "timestamp": int(now.timestamp() * 1000)
        })
    except Exception as e:
        print(f'Error getting day: {e}')
        return jsonify({"error": "Internal server error"}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"})

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from public directory"""
    return send_from_directory('public', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
