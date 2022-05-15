from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller
from selenium import webdriver
import os
import platform


def heroku_driver() -> webdriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


def win_driver() -> webdriver:
    # chromedriver_autoinstaller.install()
    chrome_options = Options()

    # chrome_options.add_argument("-headless")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(options=chrome_options)


def get_webdriver() -> webdriver:
    if "Windows" in platform.platform():
        return win_driver()
    else:
        return webdriver.Chrome('/home/erickson/Alexa_Skills/resources/chromedriver')
