from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def watch_stream():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")  # Mutes the stream to avoid noise during automation

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.twitch.tv/angelito20163")
    # Keep the browser open for a certain period
    driver.implicitly_wait(320) 
    driver.quit()

if __name__ == "__main__":
    watch_stream()
