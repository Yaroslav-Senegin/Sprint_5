from data import Data, UrlList
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    # Переход по клику на «Личный кабинет» с главной страницы
    def test_go_to_account_from_main(self, driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.login_button_main).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.profile_link))
        
        assert driver.find_element(*Locators.profile_link)
