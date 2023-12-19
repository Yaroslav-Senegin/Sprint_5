from data import Data, UrlList
import helper_functions
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    # Выход по кнопке «Выйти» в личном кабинете
    def test_logout(driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.login_button_main).click()
        helper_functions.login_fields_set(driver, Data.email, Data.password)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.profile_link))
        driver.find_element(*Locators.logout_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_button_login_page))
        assert driver.find_element(*Locators.login_button_login_page)
