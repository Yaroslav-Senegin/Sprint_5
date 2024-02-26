from data import Data, UrlList
import pytest
from locators import Locators
import helper_functions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    # Попытка регистрации без имейла
#    def test_registration_without_email(self, driver):
 #       driver.get(UrlList.page_registration_url)
#        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_name())
#        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_pass())
#        driver.find_element(*Locators.registration_button).click()
 #       WebDriverWait(driver, 10).until(
 #           expected_conditions.visibility_of_element_located(Locators.registration_button))
 #       
 #       assert driver.find_element(*Locators.header_h2).text == 'Регистрация'


    # Попытка регистрации с паролем <6 символов. Проверяем граничные значения 1 и 5
    @pytest.mark.parametrize('password', [helper_functions.unform_email_1(), helper_functions.unform_email_2()])
    def test_registration_password_less_6_synbols(self, driver, password):
        driver.get(UrlList.page_registration_url)

        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(password)

        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.incorrect_pass_message))
        
        assert driver.find_element(*Locators.incorrect_pass_check).text == 'Некорректный пароль'



