import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image

# Set search queries for formal & casual outfits
search_queries = {
    "formal_outfits_men": "Men interview formal wear",
    "formal_outfits_women": "Women interview formal wear",
    "casual_outfits_men": "Men casual wear",
    "casual_outfits_women": "Women casual wear"
}

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in the background (no browser UI)
driver = webdriver.Chrome(options=options)

def download_images(query, folder, num_images=500):
    """Scrape images from Google based on the query and save them."""
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    driver.get(url)
    time.sleep(2)

    os.makedirs(folder, exist_ok=True)

    # Scroll to load images
    for _ in range(3):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

    images = driver.find_elements(By.CSS_SELECTOR, "img")
    count = 0

    for img in images:
        src = img.get_attribute("src")
        if src and "http" in src:
            try:
                response = requests.get(src, stream=True, timeout=5)
                img_path = os.path.join(folder, f"{count}.jpg")

                with open(img_path, "wb") as file:
                    file.write(response.content)

                # Resize and save
                image = Image.open(img_path)
                image = image.convert("RGB")
                image = image.resize((224, 224))  # Standardize image size
                image.save(img_path, "JPEG")

                count += 1
                if count >= num_images:
                    break

            except Exception as e:
                print(f"Error downloading {src}: {e}")

    print(f"Downloaded {count} images for {query}")

# Run for each category
for category, query in search_queries.items():
    download_images(query, f"outfits/{category}")

driver.quit()