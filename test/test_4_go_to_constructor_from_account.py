from data import Data
import helper_functions
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Переход по клику на «Конструктор» и на логотип Stellar Burgers
def test_go_to_constructor_from_account(driver):
    driver.get(Locators.page_login_url)
    helper_functions.login_fields_set(driver, Data.email, Data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.profile_link))
    driver.find_element(*Locators.constructor_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.make_burger_tag_h1))
    assert driver.find_element(*Locators.make_burger_tag_h1).is_displayed()
