from selenium import webdriver
import undetected_chromedriver as uc
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/login")

    yield driver

    time.sleep(4)