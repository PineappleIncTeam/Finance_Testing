import allure
import pytest
from allure_commons.types import Severity
from TESTS.params import params_recovery_page_email_validation


@allure.suite("Recovery Page")
class TestRecoveryPage():
    @allure.title("Open Recovery Page")
    @allure.feature("Open Recovery")
    @allure.description("""
    Redirect to the recovery page after 'password recovery' click on start page. 

    Precondition:
    - Navigate to the start page.

    Expected Result:
    - The recovery page opens successfully in the browser.
    - All necessary elements are visible.
    """)
    @allure.severity(Severity.BLOCKER)
    def test_recovery_page_go_to_site(self, recoverypage):
        recoverypage.start_page_redirect("recovery")

    @allure.title("Open Recovery Page")
    @allure.feature("Return link")
    @allure.description("""
    Redirect back to start page after 'return back' link click.

    Precondition:

    Expected Result:
    - User redirected back to start page after 'return back' link click.
    """)
    @allure.severity(Severity.NORMAL)
    def test_recovery_check_return_link(self, recoverypage):
        recoverypage.recovery_check_return_link()

    @allure.title("Open Recovery Page")
    @allure.feature("Email validation")
    @allure.description("""
    If user setup invalid values or empty to Email field in recovery page 
    error message shows 'Обязательное поле' or 'Введёт некорректный email'.

    Params:
    - Empty field
    - Wrong email (unregistered in the system)

    Expected Result:
    - After user filed email field in recovery form and click 'Recovery' button
    error message shows up ('Обязательное поле' or 'Введёт некорректный email')
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("value, expected", params_recovery_page_email_validation)
    def test_recovery_check_email_validation(self, recoverypage, value, expected):
        recoverypage.recovery_check_email_validation(value, expected)