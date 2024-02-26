from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import UrlList
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1440,800")
    driver = webdriver.Chrome(options=options)
    driver.get(UrlList.page_main_url)
    yield driver
    driver.quit()
