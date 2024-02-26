import random
import string
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Метод генерирует имя из букв латинского алфавита
def random_name():
    name = (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")
    return name


# Метод генерирует имейл из букв латинского алфавита и цифр
def random_email():
    email = (f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}_"
             f"{''.join(random.choice(string.ascii_lowercase) for i in range(6))}_"
             f"{random.randint(5000, 5999)}@yandex.ru")
    return email


# Метод генерирует пароль из букв латинского алфавита и цифр. Длинной - шесть символов
def random_pass():
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return password


# Метод генерирует имейл только с именем почтового ящика
def mail_with_name_only():
    email = f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(5000, 5999)}"
    return email


# Метод генерирует имейл с ошибкой в домене 
def mail_with_error_domain():
    email = f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(5000, 5999)}@yandex."
    return email