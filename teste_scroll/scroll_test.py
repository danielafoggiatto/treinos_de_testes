from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def test_scroll(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_name ")

    for elemento in elementos:
        driver.execute_script("arguments[0].scrollIntoView();", elemento)
        elemento.is_displayed()