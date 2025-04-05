Got it! Here's the cleaned-up, human-friendly README without the code box so you can directly copy-paste it into your README.md file:

---

# Outfit Image Scraper (Google Images)

This is a simple Python script that helps you download outfit images (like formal and casual clothes) from Google Images using Selenium.

## ✨ What It Does

- Searches Google Images for specific outfit types  
- Downloads the images automatically  
- Resizes them to 224x224 pixels  
- Saves them in organized folders  

## 📂 Categories Included

The script downloads images for these 4 categories:

- Formal outfits for men  
- Formal outfits for women  
- Casual outfits for men  
- Casual outfits for women  

Each category is saved in its own folder inside the `outfits/` directory.

## 🔧 Requirements

- Python 3.8 to 3.11  
- Google Chrome browser  
- ChromeDriver (version should match your Chrome)  

To install required libraries, run:

`pip install selenium pillow requests`

## 🚀 How to Use

Just run the script:

`python image_scraper.py`

It will open a browser in the background, search for each outfit type, and save the images automatically.

## 🔢 Want More or Fewer Images?

By default, it saves 50 images per category. You can change that in the script by editing this line:

`download_images(query, f"outfits/{category}", num_images=50)`

Change `50` to any number you prefer.

## 🗂️ Folder Structure

After the script runs, you’ll have a folder like this:

```
outfits/
├── casual_outfits_men/
├── casual_outfits_women/
├── formal_outfits_men/
└── formal_outfits_women/
```

Each folder will contain `.jpg` images you scraped.

---

**Note:** This script is for learning or personal use only. Google might limit scraping if overused, so use it reasonably.

---

Let me know if you want a similar style README for your other projects too!