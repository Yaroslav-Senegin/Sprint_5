from data import Data, UrlList
import helper_functions
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    # Переход по клику на «Личный кабинет» с главной страницы
    def test_go_to_account_from_main(driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.login_button_main).click()
        helper_functions.login_fields_set(driver, Data.email, Data.password)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.profile_link))
        assert driver.find_element(*Locators.profile_link)
