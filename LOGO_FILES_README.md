# Logo Files Required

This project requires two image files to be placed in the `public/` folder:

## Required Files

1. **`Anjeer Desk - Logo.png`**
   - Location: `public/Anjeer Desk - Logo.png`
   - Used in: Main page header and About page header
   - Format: PNG (recommended) or any web-compatible image format

2. **`creator.jpg`**
   - Location: `public/creator.jpg`
   - Used in: About page (creator section)
   - Format: JPG, PNG, or any web-compatible image format
   - Recommended size: Square format (e.g., 300x300px or 500x500px) for best display

## How to Add

1. Place both files in the `public/` directory
2. Ensure file names match exactly (case-sensitive):
   - `Anjeer Desk - Logo.png` (note the spaces and capitalization)
   - `creator.jpg`
3. Commit the files to your git repository:
   ```bash
   git add "public/Anjeer Desk - Logo.png"
   git add public/creator.jpg
   git commit -m "Add logo files"
   ```

## Notes

- The logo will be displayed at 60px height (45px on mobile)
- The creator image will be displayed as a circular 120px image
- Both images should be optimized for web (compressed but high quality)
- If you don't have the files yet, the website will still work but images won't display

## Alternative

If you need to use different file names or formats, update the references in:
- `public/index.html` (line with `<img src="Anjeer Desk - Logo.png"`)
- `public/about.html` (lines with logo and creator image)
