import os
import time
import schedule
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CAPTURE_FOLDER = "screenshots"

if not os.path.exists(CAPTURE_FOLDER):
    os.makedirs(CAPTURE_FOLDER)

def screenshot():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(30)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")

    try:
        driver.get("https://wplace.live/?lat=24.492667725032447&lng=118.17518521552732&zoom=14.282844653325695")
        time.sleep(8)
        filename = os.path.join(CAPTURE_FOLDER, f"{timestamp}.png")
        driver.save_screenshot(filename)
        print(f"[{timestamp}]Captured: {filename}")
    except Exception as e:
        print(f"[{timestamp}]Capture failed {e}")
    finally:
        driver.quit()

schedule.every().hour.do(screenshot)

print("Screenshot every hour...")
screenshot()

while True:
    schedule.run_pending()
    time.sleep(1)
