import pytest
from TESTS.utils import randomize_latin_string, randomize_number, \
    randomize_special_string, randomize_chinese_string, \
    randomize_cyrillic_string, randomize_password

from TESTS.settings import user_login, user_pass, user_email

params_start_page_login_invalid = [
    pytest.param("", "", True, id="Empty fields"),
    pytest.param(user_login, "", True, id="Empty password"),
    pytest.param("", user_pass, True, id="Empty login"),
    pytest.param(randomize_latin_string(6), randomize_password(3, 3, 0), True, id="Wrong user data values"),
    pytest.param(user_login, randomize_password(3, 3, 0), True, id="Wrong password"),
    pytest.param(randomize_latin_string(6), user_pass, True, id="Wrong login")
]

params_income_new_category_names_invalid = [
    pytest.param(randomize_latin_string(15), id="String 15"),
    pytest.param(f"{randomize_latin_string(5)} {randomize_latin_string(5)}", id="Space between two string(5)"),
    pytest.param("document.body.style.backgroundColor = 'red';", id="Script"),
    pytest.param("", id="Empty"),
    pytest.param(randomize_chinese_string(14), id="14 Chinese")
]

params_income_new_category_names_valid = [
    pytest.param(randomize_latin_string(10), id="Valid 10")
]

params_recovery_page_email_validation = [
    pytest.param("", False, id="Empty field"),
    pytest.param(f"{randomize_latin_string(5)}@{randomize_latin_string(5)}.{randomize_latin_string(5)}",
                 False, id="Invalid email")
]

params_register_page_verify_email_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: string"),
    pytest.param(randomize_number(100), False,
                 id="Format: int"),
    pytest.param(f"@{randomize_latin_string(3)}.{randomize_latin_string(3)}", False, id="Format: @chars.chars"),
    pytest.param(f"{randomize_latin_string(3)}@", False, id="Format: chars@"),
    pytest.param(f"{randomize_latin_string(3)}@{randomize_latin_string(3)}", False, id="Format: chars@chars")
]
#
params_register_page_verify_login_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: invalid value (5 chars)"),
    pytest.param(randomize_latin_string(33), False, id="Format: invalid value (33 chars)"),
    pytest.param(randomize_special_string(10), False, id="Format: invalid special"),
    pytest.param(randomize_cyrillic_string(10), False, id="Format: invalid cyrillic"),
    pytest.param(randomize_chinese_string(10), False, id="Format: invalid chinese")
]
#
params_register_page_verify_pass_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: invalid value (5 chars)"),
    pytest.param(randomize_number(10000), False, id="Format: invalid value (5 int)"),
    pytest.param(randomize_password(2, 2, 0), False, id="Format: invalid value (5 chars),2 up 2 low 1 int"),
    pytest.param(randomize_password(1, 31, 0), False, id="Format: invalid value (33 chars),1 up 31 low 1 int"),
    pytest.param(randomize_password(5, 5, 1), False, id="Format: invalid value (10 chars),5 up 5 low 0 int"),
    pytest.param(randomize_password(5, 5, 2), False, id="Format: invalid value (6 chars),0 up 5 low 1 int"),
    pytest.param(randomize_password(5, 5, 3), False, id="Format: invalid value (6 chars),5 up 0 low 1 int")
]

params_register_page_verify_pass_confirm_field = [
    pytest.param(randomize_password(3, 3, 0), True, True, id="Format: valid pass: 3 low 3 up int"),
    pytest.param(randomize_password(3, 3, 0), True, False, id="Format: valid pass: 3 low 3 up int")
]

params_register_page_exist_user_values = [
    pytest.param(f"{randomize_latin_string(5)}@{randomize_latin_string(5)}.{randomize_latin_string(5)}",
                 user_login,
                 randomize_password(3, 3, 0), id="Exist login"),
    pytest.param(user_email,
                 randomize_latin_string(10),
                 randomize_password(3, 3, 0),
                 id="Exist Email"),
    pytest.param(user_email, user_login, randomize_password(3, 3, 0), id="Exist email and login")
]