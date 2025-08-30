from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/contact_us?utm_source=chatgpt.com")
    driver.maximize_window()

    yield driver
    driver.quit()
