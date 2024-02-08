from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from data import Data, UrlList
from locators import Locators
import helper_functions
import pytest


# путь до chromedriver
DRIVER_PATH = '../chromedriver'


@pytest.fixture
def driver():
    service = Service(executable_path=DRIVER_PATH)
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# Фикстура заполняет поля для регистрации
@pytest.fixture
def create_account(driver):
    name = helper_functions.random_name()
    email = helper_functions.random_email()
    password = helper_functions.random_pass()

    driver.find_element(*Locators.input_name_field).send_keys(name)
    driver.find_element(*Locators.input_email_field).send_keys(email)
    driver.find_element(*Locators.input_password_field).send_keys(password)

    return name, email, password