from selenium import webdriver  # Import Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Handles ChromeDriver service
from selenium.webdriver.chrome.options import Options  # Configures Chrome options
from selenium.webdriver.common.by import By  # Helps locate HTML elements
from selenium.webdriver.support.ui import WebDriverWait  # Implements explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Defines wait conditions
from bs4 import BeautifulSoup  # Parses HTML for text extraction
import time  # Adds delays if necessary

def scrape_website(website):
    """
    Launches a Chrome browser instance, navigates to the specified website, and retrieves its HTML content.

    Parameters:
        website (str): The URL of the website to scrape.

    Returns:
        str: The HTML content of the page or None if an error occurs.
    """
    print("Launching Chrome Browser")

    # Path to the ChromeDriver executable (ensure it's correctly placed)
    chrome_driver_path = "./chromedriver.exe"

    # Set up Chrome options (e.g., run in headless mode if needed)
    options = Options()
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Open the website
        driver.get(website)
        print("Page loaded...")

        # Wait until the <body> tag is present (ensures page is loaded)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Get the page source (HTML content)
        html = driver.page_source
        return html

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Always close the browser after scraping
        driver.quit()

def extract_body_text(html):
    """
    Extracts and returns the main text content from the <body> tag of the given HTML.

    Parameters:
        html (str): The HTML content of a webpage.

    Returns:
        str: Extracted body text or an error message if no body is found.
    """
    soup = BeautifulSoup(html, "html.parser")  # Parse HTML content
    body_content = soup.find("body")  # Locate the <body> tag

    if body_content:
        return body_content.get_text(separator="\n", strip=True)  # Extract and clean text

    return "No body content found"  # Return message if <body> is missing

def clean_body_content(body_content):
    """
    Cleans extracted text by removing unnecessary scripts and styles, then formats it properly.

    Parameters:
        body_content (str): The raw text extracted from the website's body.

    Returns:
        str: Cleaned and formatted text.
    """
    soup = BeautifulSoup(body_content, "html.parser")  # Parse the extracted text

    # Remove unwanted elements like <script> and <style> tags
    for script in soup(["script", "style"]):
        script.extract()
    
    # Get cleaned text with line breaks
    cleaned_content = soup.get_text(separator="\n", strip=True)

    # Remove extra blank lines and spaces
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content  # Return formatted text

def split_dom_content(dom_content, max_length=6000):
    """
    Splits large content into smaller chunks to avoid exceeding model processing limits.

    Parameters:
        dom_content (str): The cleaned extracted content.
        max_length (int): The maximum length of each chunk (default: 6000 characters).

    Returns:
        list: A list of text chunks.
    """
    if not dom_content:
        return ["No content available"]  # Handle empty content case

    # Split content into multiple chunks based on the specified max length
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
