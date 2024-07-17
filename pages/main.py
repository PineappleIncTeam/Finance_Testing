import allure
import random
from typing import Tuple, Union
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WdW
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.common import ElementNotVisibleException, NoSuchElementException, \
    TimeoutException, StaleElementReferenceException
from selenium.common.exceptions import WebDriverException


class Main:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://dev.freenance.store/"
        self.wait = WdW(driver, 10, poll_frequency=1)
        self.objects = []

    MAIN_LOGO = "//img[@alt='Логотип']"
    MAIN_LNK = "//p[contains(text(),'Главная')]"
    ABOUT_US_LNK = "//p[contains(text(),'О нас')]"
    ABOUT_APP_LNK = "//p[contains(text(),'О приложении')]"
    BLOG_LNK = "//p[contains(text(),'Блог')]"
    ENTER_BTN = "//button[contains(text(),'Вход')]"
    REGISTER_BTN = "(//button[contains(text(),'Регистрация')])[1]"
    HEADER_CONTAINER = "//header"

    NAVBAR_BURGER = "//img[@alt='Бургер']"
    NAVBAR_MENU_TXT = "//p[contains(text(), 'Меню')]"
    NAVBAR_X_BTN = "//img[@alt = 'Крестик']"

    COOKIE_CONTAINER = "//h3[contains(text(),'Файлы cookies')]"
    COOKIE_X_BTN = "//img[@alt='крестик']"
    COOKIE_LNK = "//a[contains(text(),'«cookies»')]"
    COOKIE_WIKI_URL = "https://ru.wikipedia.org/wiki/Cookie"
    COOKIE_REG_BTN = "(//button[contains(text(),'Регистрация')])[2]"

    USER_AGREEMENT = "//a[contains(text(),'Пользовательское соглашение')]"

    @allure.step("Go to site")
    def go_to_site(self) -> None:
        """Open site in browser"""
        try:
            self.driver.get(self.base_url)
        except WebDriverException:
            print("PAGE DOWN")

    def is_opened(self, url=None) -> None:
        """Wait url is loaded"""
        if not url:
            url = self.base_url
        self.wait.until(Ec.url_to_be(url))

    def wait_element(self, locator: str) -> bool:
        try:
            self.wait.until(Ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element(self, locator: str) -> object:
        """Get page element using xpath locator and return obj"""
        self.wait.until(
            Ec.presence_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator)

    @allure.step("Wait element to be clickable and click")
    def wait_and_click(self, locator: str):
        """Wait element to be clickable and click it"""
        WdW(self.driver, 20).until(
            Ec.element_to_be_clickable((By.XPATH, locator))).click()

    @allure.step("Wait until element not located")
    def wait_not_present(self, locator: str):
        try:
            WdW(self.driver, 20).until_not(
                Ec.presence_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    @allure.step("Get locators of Header's links")
    def get_header_objects(self) -> None:
        """Get locators of Header's links"""
        self.objects.clear()
        for i in range(1, 5):
            self.objects.append(f'(//p)[{i}]')

    @allure.step("Get two object rectangle position")
    def get_ojb_rect(self,
                     i: int,
                     coordinate: str,
                     border_side: str) -> Tuple[int, int]:
        """Get rectangle borders position of two objects"""
        if i == 100:
            # 100 is just for use this choice
            first_obj = self.get_element(self.objects[0]).rect
            second_obj = self.get_element(self.objects[1]).rect
        else:
            first_obj = self.get_element(self.objects[i]).rect
            second_obj = self.get_element(self.objects[i + 1]).rect
        first_obj_border = first_obj[coordinate] + first_obj[border_side]
        second_obj_border = second_obj[coordinate]
        return first_obj_border, second_obj_border

    @staticmethod
    def get_all_links() -> list:
        """Get list of all Header links exclude Logo and Main url"""
        return [Main.ABOUT_APP_LNK, Main.ABOUT_US_LNK]

    @allure.step("Get random Header link")
    def get_random_link(self) -> str:
        """Get random link from Header's links"""
        links = self.get_all_links()

        return random.choice(links)
