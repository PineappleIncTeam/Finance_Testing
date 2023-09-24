from selenium.webdriver.support.ui import WebDriverWait as WdW
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common import ElementNotVisibleException, NoSuchElementException, TimeoutException
import allure


class Main:
    def __init__(self, driver, timeout = 10):
        """
       Args:
       driver: The Selenium WebDriver instance.
       timeout (int): The default timeout for implicit waits (default is 10 seconds).
        """
        self.driver = driver
        self.base_url = "https://freenance.online/"
        self.driver.implicitly_wait(timeout)

    def go_to_site(self) -> None:
        """
        Opens the main website at the specified base URL.
        """
        with allure.step(f"Go to site: {self.base_url}"):
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(5)

    def get_element_name(self, by_locator):
        """
        Gets the text of an element identified by the given locator.
        """
        element = WdW(self.driver, 10).until(Ec.visibility_of_element_located(by_locator))
        return element.text

    def do_element_click(self, name_element: str, by_locator) -> None:
        """
        Performs a click action on an element identified by the given locator.
        """
        with allure.step(f"Click '{name_element}'"):
            WdW(self.driver, 20).until(Ec.presence_of_element_located(by_locator)).click()

    def do_element_send_keys(self, locator_name: str, by_locator, text_keys) -> None:
        with allure.step(f"Send {text_keys} to {locator_name} field"):
            """
            Sends the specified text to an element identified by the given locator.
            """
            WdW(self.driver, 10).until(Ec.visibility_of_element_located(by_locator)).send_keys(text_keys)

    def element_displayed(self, by_locator):
        """
        Checks if an element identified by the given locator is displayed.
        """
        element = WdW(self.driver, 10).until(Ec.presence_of_element_located(by_locator))
        return bool(element)

    def get_element(self, by_locator):
        """
        Waits for and returns an element identified by the given locator.
        """
        element = WdW(self.driver, 10).until(Ec.visibility_of_element_located(by_locator))
        return element

    def set_window_size(self, width, height):
        """
        Sets the window size of the browser window.
        """
        self.driver.set_window_size(width, height)

    def get_color(self, element):
        """
        Gets the CSS color property of a given element.
        """
        self.driver.implicitly_wait(3)
        tab_element = self.get_element(element)
        current_color = tab_element.value_of_css_property("background-color")
        return current_color

    def check_elements(self, element, expected):
        with allure.step("Locate and check element on the page"):
            el = self.get_element(element)
            assert el.is_displayed() == expected

    def wait_exaption(self):
        """
        Creates and returns a WebDriverWait instance with custom exceptions.
        """
        wait = WdW(self.driver, timeout=2, poll_frequency=1,
                   ignored_exceptions=[ElementNotVisibleException, NoSuchElementException, TimeoutException])
        return wait

    def wait_not_element(self, by_locator):
        """
        Waits for an element identified by the given locator to disappear.
        """
        try:
            wait = self.wait_exaption()
            wait.until_not(Ec.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False
