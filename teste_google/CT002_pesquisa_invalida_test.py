from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.invalido
def test_002_pesquisa_invalida(driver):
    driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("asdjioasijfoiaskfopaisf0kopsa")
    driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Keys.RETURN)

    resultado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(By.XPATH, "//*[text()='Sua pesquisa não encontrou nenhum documento correspondente']")
    )

    assert resultado.text == "Sua pesquisa não encontrou nenhum documento correspondente"
