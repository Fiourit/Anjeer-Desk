// Global state
let isSilent = false;
let hasShownAcknowledgment = false;
let currentDay = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initializeDayCounter();
    initializeBorderAnimation();
    loadQuote();
    initializeNotes();
    initializeSilenceMode();
    checkAcknowledgment();
});

// Day counter
async function initializeDayCounter() {
    try {
        const response = await fetch('/api/day');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        currentDay = data.dayOfYear;
        
        const dayCounterElement = document.getElementById('dayCounter');
        if (dayCounterElement && data.dayOfYear && data.year) {
            dayCounterElement.textContent = `Day ${data.dayOfYear} of ${data.year}`;
        }
    } catch (error) {
        console.error('Error fetching day info:', error);
        // Fallback calculation using JavaScript
        const now = new Date();
        const start = new Date(now.getFullYear(), 0, 1); // Jan 1 of current year
        const diff = now - start;
        const oneDay = 1000 * 60 * 60 * 24;
        const day = Math.floor(diff / oneDay) + 1; // +1 because Jan 1 is day 1
        const year = now.getFullYear();
        
        const dayCounterElement = document.getElementById('dayCounter');
        if (dayCounterElement) {
            dayCounterElement.textContent = `Day ${day} of ${year}`;
        }
        currentDay = day;
    }
}

// Border animation - completes one cycle every 24 hours
// The border is a large rectangle with rounded corners that fades as the day progresses
function initializeBorderAnimation() {
    const borderElement = document.getElementById('borderAnimation');
    if (!borderElement) return;
    
    function updateBorder() {
        const now = new Date();
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();
        
        // Calculate progress through the day (0 to 1)
        // 0 = start of day (midnight), 1 = end of day (next midnight)
        const totalSeconds = hours * 3600 + minutes * 60 + seconds;
        const progress = totalSeconds / 86400; // 86400 seconds in a day
        
        // Border starts thick (8px) and fades to very thin (0.5px) as day progresses
        // Also fades opacity from 1.0 to 0.2
        const minWidth = 0.5;
        const maxWidth = 8;
        const currentWidth = maxWidth - (progress * (maxWidth - minWidth));
        
        // Opacity also fades: starts at 1.0, ends at 0.2
        const minOpacity = 0.2;
        const maxOpacity = 1.0;
        const currentOpacity = maxOpacity - (progress * (maxOpacity - minOpacity));
        
        borderElement.style.borderWidth = `${currentWidth}px`;
        borderElement.style.opacity = currentOpacity;
    }
    
    updateBorder();
    setInterval(updateBorder, 1000); // Update every second for smooth animation
}

// Load quote for today
async function loadQuote() {
    try {
        const response = await fetch('/api/quote');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        const quoteElement = document.getElementById('quote');
        const authorElement = document.getElementById('author');
        
        if (quoteElement && data.quote) {
            quoteElement.textContent = `"${data.quote}"`;
        }
        
        if (authorElement) {
            if (data.author) {
                authorElement.textContent = `— ${data.author}`;
            } else {
                authorElement.textContent = '';
            }
        }
    } catch (error) {
        console.error('Error loading quote:', error);
        const quoteElement = document.getElementById('quote');
        const authorElement = document.getElementById('author');
        if (quoteElement) {
            quoteElement.textContent = '"The present moment is the only time over which we have dominion."';
        }
        if (authorElement) {
            authorElement.textContent = '— Thich Nhat Hanh';
        }
    }
}

// Notes - stored in localStorage
function initializeNotes() {
    const notesElement = document.getElementById('notes');
    if (!notesElement) return;
    
    // Load notes for today
    const today = new Date().toDateString();
    const savedNotes = localStorage.getItem(`notes_${today}`);
    
    if (savedNotes) {
        notesElement.value = savedNotes;
    }
    
    // Save notes as user types
    notesElement.addEventListener('input', () => {
        localStorage.setItem(`notes_${today}`, notesElement.value);
    });
    
    // Clear notes at midnight (optional - you can remove this if you want notes to persist)
    // For now, notes persist until browser is cleared (as per requirements)
}

// Silence mode
function initializeSilenceMode() {
    const silenceToggle = document.getElementById('silenceToggle');
    const contentSection = document.getElementById('contentSection');
    const quoteSection = document.getElementById('quoteSection');
    
    if (!silenceToggle) return;
    
    // Load silence state
    const savedSilence = localStorage.getItem('silenceMode');
    if (savedSilence === 'true') {
        isSilent = true;
        applySilenceMode();
    }
    
    silenceToggle.addEventListener('click', () => {
        isSilent = !isSilent;
        localStorage.setItem('silenceMode', isSilent.toString());
        applySilenceMode();
    });
    
    function applySilenceMode() {
        if (isSilent) {
            if (contentSection) contentSection.classList.add('silent');
            if (quoteSection) quoteSection.style.display = 'none';
            if (silenceToggle) silenceToggle.textContent = 'Sound';
        } else {
            if (contentSection) contentSection.classList.remove('silent');
            if (quoteSection) quoteSection.style.display = 'block';
            if (silenceToggle) silenceToggle.textContent = 'Silence';
        }
    }
}

// Daily acknowledgment - shows once per day
function checkAcknowledgment() {
    const acknowledgmentElement = document.getElementById('acknowledgment');
    if (!acknowledgmentElement) return;
    
    const today = new Date().toDateString();
    const lastShown = localStorage.getItem('acknowledgment_shown');
    
    if (lastShown !== today) {
        // Show acknowledgment after a short delay
        setTimeout(() => {
            acknowledgmentElement.classList.add('show');
            localStorage.setItem('acknowledgment_shown', today);
        }, 2000);
    }
}
