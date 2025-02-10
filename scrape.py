from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    print("Launching Chrome Browser")

    chrome_driver_path = "./chromedriver.exe"
    options = Options()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        html = driver.page_source
        return html
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        driver.quit()

def extract_body_text(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.find("body")
    if body_content:
        return body_content.get_text(separator="\n", strip=True)
    return "No body content found"

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()
    
    cleaned_content = soup.get_text(separator="\n", strip=True)
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    if not dom_content:
        return ["No content available"]
    
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]

