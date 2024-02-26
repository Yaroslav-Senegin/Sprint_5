from data import Data, UrlList
import pytest
from locators import Locators
import helper_functions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    # Попытка регистрации без имени
    def test_registration_without_name(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_pass())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))
        
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'


    # Попытка регистрации без имейла
    def test_registration_without_email(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_pass())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))
        
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'

    # Попытка регистрации без пароля
    def test_registration_without_pass(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))
        
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'


    # Попытка регистрации с паролем <6 символов. Проверяем граничные значения 1 и 5
    @pytest.mark.parametrize('password', ['a', 'Test1'])
    def test_registration_password_less_6_synbols(self, driver, password):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.incorrect_pass_message))
        
        assert driver.find_element(*Locators.incorrect_pass_check).text == 'Некорректный пароль'


    # Регистрация пользователя с имейлом не по формату
    @pytest.mark.parametrize('email', [helper_functions.mail_with_name_only(), helper_functions.mail_with_error_domain()])
    def test_registration_with_incorrect_email(self, driver, email):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(email)
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_pass())
        driver.find_element(*Locators.registration_button).click() 
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.user_exists_message))
        
        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'


    # Успешная регистрация
    def test_registration_correct(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_pass())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.login_header_tag_h2))
        
        assert driver.find_element(*Locators.header_h2).text == 'Вход'        


    # Попытка регистрации уже существующего пользователя
    def test_registration_with_exist_user(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(Data.name)
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.registration_button).click()        
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.user_exists_message))
        
        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'
