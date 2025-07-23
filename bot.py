import os
import requests
from pathlib import Path
from duckduckgo_search import DDGS
from PIL import Image
from io import BytesIO

def download_images(folder, urls):
    """Downloads images from a list of URLs into a specified folder."""
    folder.mkdir(exist_ok=True)
    for i, url in enumerate(urls):
        try:
            # Send a request to get the image
            response = requests.get(url, timeout=1000)
            response.raise_for_status() # Raise an exception for bad status codes

            # Check if the content is a valid image
            img = Image.open(BytesIO(response.content))

            # Create a filename (e.g., 00001.jpg)
            # Use the image format detected by Pillow (e.g., JPEG, PNG)
            filename = f"{i+1:05d}.{img.format.lower()}"

            # Save the image
            with open(folder / filename, "wb") as f:
                f.write(response.content)

            print(f"✅ Downloaded {filename}")

        except Exception as e:
            print(f"❌ Failed to download {url}. Reason: {e}")


# --- Define your objects and search queries here ---
# Use descriptive queries to find multiple objects at once
search_queries = [
    "smartphone on wooden desk with charging cable"
    "wireless headphones over laptop keyboard"
    "smartwatch displaying heart rate on wrist"
    "drone flying over scenic landscape with camera"
    "gaming console with controllers and TV screen"
    "VR headset on futuristic stand"
]
dataset_folder = Path("image_dataset")
max_images_per_query = 300 # Adjust as needed


# --- The script will do the rest ---
all_urls = []
with DDGS() as ddgs:
    for query in search_queries:
        print(f"\nSearching for: '{query}'...")
        # Collect URLs from the search results
        urls = [r['image'] for r in ddgs.images(query, max_results=max_images_per_query)]
        all_urls.extend(urls)
        print(f"Found {len(urls)} images.")

print(f"\nStarting download of {len(all_urls)} total images...")
download_images(dataset_folder, all_urls)

print(f"\n🎉 Task complete! Images are in the '{dataset_folder}' folder.")