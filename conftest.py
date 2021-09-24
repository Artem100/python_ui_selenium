import pytest
import os
from dotenv import load_dotenv
from os.path import dirname, abspath

from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


ROOT_DIR = dirname(abspath(__file__))
DOWNLOAD_DIR = ROOT_DIR + "//download_files"
load_dotenv()

@pytest.fixture()
def browser(request):
    browser_list = request.config.getoption("--browser")
    browser_remote = request.config.getoption("--browser")

    if 'chrome' in browser_list:
        options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": DOWNLOAD_DIR}
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", preferences)
        capabilities = options.to_capabilities()
        # if jenkins:
        # options.add_argument('--headless')
        #     options.add_argument("--window-size=1920,1080")
        # driver = webdriver.Chrome(executable_path=ROOT_DIR + chrome_driver_path, desired_capabilities=capabilities)
        driver = webdriver.Chrome(desired_capabilities=capabilities)
    elif 'firefox' in browser_list:
        fp = webdriver.FirefoxProfile()
        options = Options()
        # options.headless = True
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference('browser.download.dir', DOWNLOAD_DIR)
        fp.set_preference("browser.helperApps.alwaysAsk.force", False)
        fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/pdf,application/x-pdf')
        fp.set_preference("pdfjs.disabled", True)
        driver = webdriver.Firefox(firefox_profile=fp, options=options)
    elif "remote" in browser_list:
        if "REMOTE_BROWSER_URL" in os.environ:
            REMOTE_BROWSER_URL = os.environ["REMOTE_BROWSER_URL"]
        else:
            REMOTE_BROWSER_URL = str(os.getenv("REMOTE_BROWSER_URL"))

        if "REMOTE_BROWSER_NAME" in os.environ:
            REMOTE_BROWSER_NAME = os.environ["REMOTE_BROWSER_NAME"]
        else:
            REMOTE_BROWSER_NAME = str(os.getenv("REMOTE_BROWSER_NAME"))

        if "REMOTE_BROWSER_VERSION" in os.environ:
            REMOTE_BROWSER_VERSION = os.environ["REMOTE_BROWSER_VERSION"]
        else:
            REMOTE_BROWSER_VERSION = str(os.getenv("REMOTE_BROWSER_VERSION"))

        capabilities = {'browserName': REMOTE_BROWSER_NAME,
                        "version": "",
                        "enableVnc": True,
                        "enableVideo": True,
                        "enableLog": True
                        }

        driver = webdriver.Remote(REMOTE_BROWSER_URL, desired_capabilities=capabilities)
        # logging.info(f"Browser {}")
    driver.maximize_window()
    driver.set_page_load_timeout(20)
    yield driver
    driver.quit()

# @pytest.fixture(scope='session')
# def user_cookies():
#     cookies = authUser("test@ayay.coo", "12345")
#     yield cookies

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type of browser: edge, chrome, firefox, remote")


