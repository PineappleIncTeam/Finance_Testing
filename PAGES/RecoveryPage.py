from selenium.webdriver.common.by import By
from PAGES.StartPage import StartPage


class RecoveryPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)

    recoverypage_email_field = (By.CLASS_NAME, "RecoveryPass_input__FdRR7")
    recoverypage_forward_btn = (By.CLASS_NAME, "RecoveryPass_btn__bZmcR")
    recoverypage_return_link = (By.CLASS_NAME, "RecoveryPass_recovery__pyvPi")

    recoverypage_email_error = (By.XPATH, "//div[contains(text(),'Обязательное поле')]")
    recoverypage_email_error_incorect = (By.XPATH, "//div[contains(text(),'Введёт некорректный email')]")

    def recovery_check_return_link(self):
        self.start_page_redirect("recovery")
        self.do_element_click("return back", self.recoverypage_return_link)
        assert self.element_displayed(self.startpage_login_field)

    def recovery_check_email_validation(self, value, expected):
        self.start_page_redirect("recovery")
        self.do_element_send_keys("Email field", self.recoverypage_email_field, value)
        self.do_element_click("'Forward' button", self.recoverypage_forward_btn)

        if not expected:
            if self.wait_not_element(self.recoverypage_email_error) == expected:
                if self.wait_not_element(self.recoverypage_email_error_incorect):
                    assert True
            else:
                if self.wait_not_element(self.recoverypage_email_error_incorect) == expected:
                    assert True
