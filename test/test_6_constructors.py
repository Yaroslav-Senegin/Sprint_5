from locators import Locators
from data import UrlList
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTabsSwitching:
    # Переход во вкладку "Соусы"
    def test_go_to_souses(driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.souses_tab).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.souses_check))
        
        assert driver.find_element(*Locators.souses_check).is_displayed()

    # Переход во вкладку "Начинки"
    def test_go_to_nachinki(driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.nachinki_tab).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.nachinki_check))
        
        assert driver.find_element(*Locators.nachinki_check).is_displayed()

    # Переход во вкладку "Булки" через "Начинки"
    def test_go_to_bulki(driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.nachinki_tab).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.nachinki_check))
        
        driver.find_element(*Locators.bulki_tab).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.bulki_check))
        
        assert driver.find_element(*Locators.bulki_check).is_displayed()
