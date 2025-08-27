from selenium import webdriver
import undetected_chromedriver as uc
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")

    yield driver
    driver.quit()
