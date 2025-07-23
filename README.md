# Image Scraper for Model Training

This Python script provides a simple yet effective way to scrape images from DuckDuckGo based on specific search queries. It's designed to help researchers and developers quickly gather image datasets for machine learning model training, computer vision tasks, or other data-driven projects.

## 🚀 Features

* **Customizable Search Queries:** Easily define multiple search terms to gather diverse image sets.
* **Batch Downloading:** Efficiently downloads a specified number of images per query.
* **Error Handling:** Basic error handling for failed downloads, ensuring the script continues even if some images can't be fetched.
* **Image Validation:** Uses Pillow to verify downloaded content is a valid image before saving.
* **Organized Output:** Saves all downloaded images into a specified local folder.

## ✨ Why is this useful for Model Training?

Collecting a relevant and sufficiently large dataset is often the first and most critical step in training robust machine learning models, especially in computer vision. This script automates a significant part of that data collection process, allowing you to:
* Quickly build initial datasets for proof-of-concept models.
* Expand existing datasets with more examples.
* Gather images for specific object detection, image classification, or segmentation tasks.
* Obtain diverse variations of objects or scenes required for model generalization.

## 📦 Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone [https://github.com/YourGitHubUsername/your-repo-name.git](https://github.com/YourGitHubUsername/your-repo-name.git)
    cd your-repo-name
    ```
    (Replace `YourGitHubUsername` and `your-repo-name` with your actual GitHub details)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

1.  **Open the `image_scraper.py` (or whatever you name your script) file.**

2.  **Modify the `search_queries` list:**
    ```python
    search_queries = [
        "person working on laptop with mug",
        "office desk with books and computer",
        "student studying with laptop and books"
    ]
    ```
    Add or remove queries to suit your image collection needs. Use descriptive queries for better results.

3.  **Adjust `max_images_per_query`:**
    ```python
    max_images_per_query = 75 # Adjust as needed
    ```
    This controls how many images the script attempts to download for each query.

4.  **Run the script:**
    ```bash
    python image_scraper.py
    ```

    The script will create a folder named `image_dataset` (or whatever you set `dataset_folder` to) in the same directory and download the images there.

## ⚠️ Important Considerations & Disclaimer

* **Copyright and Licensing:** Be mindful of image copyrights and licenses. Images found online may be subject to various usage restrictions. Ensure you have the necessary rights or permissions for your intended use, especially for commercial projects. This script is provided for educational and research purposes.
* **Rate Limiting:** Making too many requests in a short period might lead to temporary IP blocking by search engines. This script does not currently implement advanced rate limiting.
* **Search Engine Changes:** Web scraping relies on the structure of websites. Changes in the search engine's HTML/API might break the `duckduckgo-search` library's functionality in the future.

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or bug fixes.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
