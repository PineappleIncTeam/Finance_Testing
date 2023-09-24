import allure
import pytest
from allure_commons.types import Severity
from TESTS.params import params_register_page_verify_email_field, params_register_page_verify_login_field, \
    params_register_page_verify_pass_field, params_register_page_verify_pass_confirm_field, \
    params_register_page_exist_user_values


@allure.suite("Register Page")
class TestRegisterPage:
    @allure.title("Open Register Page")
    @allure.feature("Register page")
    @allure.description("""
    Redirect to the register page after 'registration' click on start page. 
    
    Precondition:
    - Navigate to the start page.

    Expected Result:
    - The register page opens successfully in the browser.
    - All necessary elements are visible.
    """)
    @allure.severity(Severity.NORMAL)
    def test_register_page_open(self, registerpage):
        registerpage.start_page_redirect("register")

    @allure.title("Check Already Registered Page")
    @allure.feature("Already register link")
    @allure.description("""
    Click on the "Already Registered" link and check the redirection, back to Start page.
    
    Preconditions:
        
    Expected result:
    - User redirected back start page after click 'Already Registered' link on registration page. 
    """)
    @allure.severity(Severity.NORMAL)
    def test_register_page_already_registered_link(self, registerpage):
        registerpage.register_check_already_registered_link()

    @allure.title("Verify Email Field on Register Page")
    @allure.feature("Email field error")
    @allure.description("""
    Verify the email field on the Register Page with different values.
    If value is no valid, proper error message should be displayed.

    Precondition:
    - User is on the Register Page.

    Expected Result:
    - If value is not match with proper requirements for email,
    an error message should be displayed as specified in 'error'.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("val, expected", params_register_page_verify_email_field)
    def test_register_email_field_validation(self, registerpage, val, expected):
        registerpage.register_check_email_field_validation(val, expected)

    @allure.title("Verify Login Field on Register Page")
    @allure.feature("Login field error")
    @allure.description("""
        Verify the login field on the Register Page with different values.
        If value is no valid, proper error message should be displayed.

        Precondition:
        - User is on the Register Page.

        Expected Result:
        - If value is not match with proper requirements for login,
        an error message should be displayed as specified in 'error'.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("value, expected", params_register_page_verify_login_field)
    def test_register_login_field_validation(self, registerpage, value, expected):
        registerpage.register_check_login_field_validation(value, expected)

    @allure.title("Verify Password Field on Register Page")
    @allure.feature("Password field error")
    @allure.description("""
        Verify the password field on the Register Page with different values.
        If value is no valid, proper error message should be displayed.

        Precondition:
        - User is on the Register Page.

        Expected Result:
        - If value is not match with proper requirements for password,
        an error message should be displayed as specified in 'error'.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("value, expected", params_register_page_verify_pass_field)
    def test_register_password_field_validation(self, registerpage, value, expected):
        registerpage.register_check_password_field_validation(value, expected)

    @allure.title("Verify Password Confirmation Field on Register Page")
    @allure.description("""
        Verify the password confirmation field on the Register Page.

        Precondition:
        - User is on the Register Page.

        Expected Result:
        - If values is not match in both fields (for password and confirm),
        an error message should be displayed as specified in 'error'.
    """)
    @pytest.mark.parametrize("val, expected, validation", params_register_page_verify_pass_confirm_field)
    def test_register_password_confirm(self, registerpage, val, expected, validation):
        registerpage.register_check_verify_pass_confirm(val, expected, validation)

    @allure.title("Register with Existing User")
    @allure.feature("exist user registration error")
    @allure.description("""
        Attempt to register with an existing user's credentials.
        Proper error message should be showed.

        Precondition:
        - User is on the Register Page.
        - User is all ready registered in the system.

        PostCondition:
        - User is not re registered.
        - User is on the Registration Page.

        Expected Result:
        - Registration should not be successful.
        - Error message should be showed if user use exist login or email.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("email, login, pwd", params_register_page_exist_user_values)
    def test_register_check_exist_user(self, registerpage, email, login, pwd):
        registerpage.register_check_exist_user(email, login, pwd)
