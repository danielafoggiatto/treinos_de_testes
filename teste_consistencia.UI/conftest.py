from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()
