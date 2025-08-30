from selenium import webdriver
import undetected_chromedriver as uc
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()
