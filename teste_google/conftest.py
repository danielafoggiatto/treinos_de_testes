from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get('https://www.google.com/')
    driver.maximize_window()

    yield driver

    driver.quit()