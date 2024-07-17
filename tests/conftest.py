import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import datetime

from pages.start_page import StartPage


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    incognito = False  # Default value for incognito mode
    if hasattr(request, 'param'):
        incognito = request.param

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    options = Options()

    if incognito:
        options.add_argument("--incognito")

    options.add_argument("--headless")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-cache")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    # driver.set_window_size(1440, 960)

    yield driver

    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.datetime}", attachment_type=allure.attachment_type.PNG)
    browser_logs = driver.get_log("browser")
    allure.attach(str(browser_logs), name="Browser Logs", attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture(scope="function")
def start_p(browser, width, height):
    s_p = StartPage(browser)
    s_p.driver.set_window_size(width, height)
    s_p.go_to_site()
    s_p.is_opened()
    return s_p
