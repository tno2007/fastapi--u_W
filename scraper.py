
import os
import cloudscraper
from datetime import datetime

def scrape_and_save(url: str, filename: str = "") -> str:
    """
    Scrape the given URL using cloudscraper and save the HTML response to the specified file in the 'download' folder.
    If filename is not provided or empty, generate a filename using the current date and time.
    Returns the filename the response was saved to.
    """
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)
    scraper = cloudscraper.create_scraper(
        delay=5,   
    )
    response = scraper.get(url)
    if not filename:
        now = datetime.now()
        urlname = url.split("/")[-2] if len(url.split("/")) > 2 else "output"
        filename = f"{urlname}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"
    filepath = os.path.join(download_dir, filename)
    print(f"Saving response to {filepath}")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(response.text)
    return filepath

def read_file_contents(filename: str) -> str:
    """
    Reads the contents of the specified file and returns it as a string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()