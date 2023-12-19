from data import Data, UrlList
import helper_functions
import pytest
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    # Попытка регистрации без имени
    def test_registration_without_name(driver):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, '', helper_functions.random_email(), helper_functions.random_pass())
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'

    # Попытка регистрации без имейла
    def test_registration_without_email(driver):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, helper_functions.random_name(), '', helper_functions.random_pass())
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'

    # Попытка регистрации без пароля
    def test_registration_without_pass(driver):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, helper_functions.random_name(), helper_functions.random_email(), '')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_h2).text == 'Регистрация'

    # Попытка регистрации с паролем <6 символов. Проверяем граничные значения 1 и 5
    @pytest.mark.parametrize('password', ['a', 'Test1'])
    def test_registration_password_less_6_synbols(driver, password):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, helper_functions.random_name(), helper_functions.random_email(), password)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.incorrect_pass_message))
        assert driver.find_element(*Locators.incorrect_pass_check).text == 'Некорректный пароль'

    # Регистрация пользователя с имейлом не по формату
    @pytest.mark.parametrize('email', [Data.unform_email[0], Data.unform_email[1]])
    def test_registration_with_incorrect_email(driver, email):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, helper_functions.random_name(), email, helper_functions.random_pass())
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.user_exists_message))
        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'

    # Успешная регистрация
    def test_registration_correct(driver):
        name = helper_functions.random_name()
        email = helper_functions.random_email()
        password = helper_functions.random_pass()
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, name, email, password)
        WebDriverWait(driver, 10).until(expected_conditions. visibility_of_element_located(Locators.login_header_tag_h2))
        assert driver.find_element(*Locators.header_h2).text == 'Вход'

    # Попытка регистрации уже существующего пользователя
    def test_registration_with_exist_user(driver):
        driver.get(UrlList.page_registration_url)
        helper_functions.registration_fields_set(driver, Data.name, Data.email, Data.password)
        WebDriverWait(driver, 10).until(expected_conditions. visibility_of_element_located(Locators.user_exists_message))
        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'
