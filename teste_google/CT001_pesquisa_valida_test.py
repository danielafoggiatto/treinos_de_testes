from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.pesquisavalida
def test_CT001_pesquisa_valida(driver):
    driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("pytest")
    driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Keys.RETURN)

    span_todas = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Todas']"))
    )
    assert span_todas.text == "Todas"
    
