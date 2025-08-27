from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_botoes_add(driver):
    botoes_padrao = driver.find_elements(By.XPATH, ".//div[contains(@class, 'productinfo')]//a[contains(@class, 'add-to-cart')]")
                                         
    botoes_hover = driver.find_elements(By.XPATH, ".//div[contains(@class, 'overlay-content')]//a[contains(@class, 'add-to-cart')]")

    assert len(botoes_padrao) == 40
    assert len(botoes_hover) == 34
        