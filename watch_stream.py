from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time  # Import the time module for the sleep function

def watch_stream():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")  # Mutes the stream

    service = Service(executable_path=r'chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.twitch.tv/angelito20163")
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
    driver.quit()

if __name__ == "__main__":
    watch_stream()
