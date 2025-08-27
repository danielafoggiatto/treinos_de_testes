from selenium import webdriver
import undetected_chromedriver as uc
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    yield driver

    time.sleep(2)