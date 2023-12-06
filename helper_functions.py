import random
import string
import locators
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
             f"{random.randint(3000, 3999)}@yandex.ru")
    return email

# Метод генерирует пароль из букв латинского алфавита и цифр. Длинной - шесть символов
def random_pass():
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return password

# Метод заполняет поля для регистрации и жмет кнопку
def registration_fields_set(driver, name, email, password):
    driver.find_element(*locators.Locators.input_field1).send_keys(name)
    driver.find_element(*locators.Locators.input_field2).send_keys(email)
    driver.find_element(*locators.Locators.input_field3).send_keys(password)
    driver.find_element(*locators.Locators.registration_button).click()

# Метод заполняет поля для логина и жмет кнопку
def login_fields_set(driver, email, password):
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.login_button_login_page))
    driver.find_element(*locators.Locators.input_field1).send_keys(email)
    driver.find_element(*locators.Locators.input_field2).send_keys(password)
    driver.find_element(*locators.Locators.login_button_login_page).click()
