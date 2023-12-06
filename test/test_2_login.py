from data import Data
import helper_functions
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Логин с главной страницы
def test_login_from_main_page(driver):
    driver.get(Locators.page_main_url)
    driver.find_element(*Locators.login_button_main).click()
    helper_functions.login_fields_set(driver, Data.email, Data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_displayed()

# Логин со страницы личного кабинета
def test_login_from_account(driver):
    driver.get(Locators.page_main_url)
    driver.find_element(*Locators.personal_account_button).click()
    helper_functions.login_fields_set(driver, Data.email, Data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_displayed()

# Логин со страницы логина
def test_login_from_login_page(driver):
    driver.get(Locators.page_login_url)
    helper_functions.login_fields_set(driver, Data.email, Data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_displayed()

# Логин сразу после регистрации
def test_login_after_registration(driver):
    name = helper_functions.random_name()
    email = helper_functions.random_email()
    password = helper_functions.random_pass()
    driver.get(Locators.page_registration_url)
    helper_functions.registration_fields_set(driver, name, email, password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_button_login_page))
    helper_functions.login_fields_set(driver, email, password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_displayed()

# Логин со страницы восстановления пароля
def test_login_from_recovery_pass(driver):
    driver.get(Locators.page_login_url)
    driver.find_element(*Locators.recovery_pass_link).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.recovery_pass_button))
    driver.find_element(*Locators.login_link_from_recovery_pass).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_button_login_page))
    helper_functions.login_fields_set(driver, Data.email, Data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_displayed()
