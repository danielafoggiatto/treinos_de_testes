from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.img
def test_004_imagens(driver):
    driver.find_element(By.XPATH, "//*[text()='Imagens']").click()
    driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys("pytest")
    driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys(Keys.RETURN)
    
    resultado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(By.XPATH, "//span[text()='Imagens']")
    )

    assert resultado.text == "Imagens"