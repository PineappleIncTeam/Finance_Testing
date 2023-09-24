from selenium.webdriver.common.by import By
from PAGES.main import Main


class StartPage(Main):
    def __init__(self, driver):
        super().__init__(driver)

    startpage_login_field = (By.NAME, "username")
    startpage_pass_field = (By.NAME, "password")
    startpage_forvard_btn = (By.XPATH, "//button[contains(text(),'Вперед')]")

    startpage_login_error = (By.CSS_SELECTOR, "div.AuthReg_error__takEU:nth-child(4)")
    startpage_pass_error = (By.XPATH, "//div[contains(text(),'Обязательное поле')]")

    startpage_recovery_link = (By.LINK_TEXT, "Забыли пароль?")
    startpage_register_link = (By.LINK_TEXT, "зарегистрируйтесь")
    startpage_logo_block = (By.CLASS_NAME, "logo_block")

    def start_page_go_to_page(self):
        self.go_to_site()
        login = self.get_element(self.startpage_login_field)
        assert login.is_displayed()

    def start_page_login(self, login, pwd, expected):
        self.go_to_site()
        self.do_element_send_keys("User name", self.startpage_login_field, login)

        self.do_element_send_keys("User password", self.startpage_pass_field, pwd)

        if not expected:
            assert self.wait_not_element(self.startpage_login_error) or self.wait_not_element(self.startpage_pass_error)

        self.do_element_click("Forward", self.startpage_forvard_btn)

    def start_page_redirect(self, link_identifier):
        self.go_to_site()

        if link_identifier == "recovery":
            self.do_element_click('password recovery link', self.startpage_recovery_link)

        elif link_identifier == "register":
            self.do_element_click('registration link', self.startpage_register_link)
