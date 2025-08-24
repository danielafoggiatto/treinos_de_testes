from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.sorte
def test_003_estou_com_sorte(driver):
    driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys("pytest")

    botao_sorte = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Estou com sorte']"))
    )
    botao_sorte.click()

    logo = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//img[@class='sidebar-logo']"))
)

    assert logo.is_displayed()
