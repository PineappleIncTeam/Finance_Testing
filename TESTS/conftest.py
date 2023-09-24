import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PAGES.StartPage import StartPage
from PAGES.RecoveryPage import RecoveryPage
from PAGES.RegisterPage import RegisterPage
# from PAGES.IncomePage import IncomePage


@pytest.fixture(scope="function")
def browser():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-data-dir=tmp/chrome_profile')
    driver = webdriver.Chrome(service=service, options=options)
    driver.delete_all_cookies()
    driver.set_window_size(1366, 768)

    yield driver

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    browser_logs = driver.get_log("browser")
    allure.attach(str(browser_logs), name="Browser Logs", attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture(scope="function")
def startpage(browser):
    start_page = StartPage(browser)
    return start_page


# @pytest.fixture(scope="function")
# def incomepage(browser):
#     income_page = IncomePage(browser)
#     return income_page
#

@pytest.fixture(scope="function")
def recoverypage(browser):
    recovery_page = RecoveryPage(browser)
    return recovery_page


@pytest.fixture(scope="function")
def registerpage(browser):
    register_page = RegisterPage(browser)
    return register_page
