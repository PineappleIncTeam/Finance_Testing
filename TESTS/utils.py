import random
import string


def randomize_number(n):
    random_number = random.randint(0, n)
    return random_number


def randomize_number_for_dropdown(n):
    random_number = random.randint(2, n)
    return random_number


def randomize_latin_string(number: int):
    symbols = string.ascii_letters
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_string(str_type, number: int):
    """Generate a random string of the specified type and length."""
    symbols = str_type
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_cyrillic_string(number: int):
    """Generate a random Cyrillic string of the specified length."""
    cyrillic_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    random_string = "".join(random.choice(cyrillic_chars) for _ in range(number))
    return random_string


def randomize_chinese_string(number: int):
    """Generate a random Chinese string of the specified length."""
    chinese_chars = '的一是不了人我在有他这为之大来以个中上们'
    random_string = "".join(random.choice(chinese_chars) for _ in range(number))
    return random_string


def randomize_special_string(number: int):
    special_chars = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
    random_string = "".join(random.choice(special_chars) for _ in range(number))
    return random_string


def randomize_password(up: int, low: int, variant: int):
    # Define character sets
    uppercase_letters = randomize_string(string.ascii_uppercase, up)
    lowercase_letters = randomize_string(string.ascii_lowercase, low)
    digits = randomize_number(9)

    # Ensure at least one uppercase letter and one digit
    password = [uppercase_letters + lowercase_letters + str(digits),
                lowercase_letters + uppercase_letters,
                lowercase_letters + str(digits),
                uppercase_letters + str(digits)
                ]
    return password[variant]
