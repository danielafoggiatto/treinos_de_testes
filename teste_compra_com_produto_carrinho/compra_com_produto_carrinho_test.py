from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def test_imagens_corretas_produto(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cart_contents_container")))

    itens_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(itens_carrinho) == 0, f"Carrinho não está vazio! Itens encontrados: {len(itens_carrinho)}"

    driver.find_element(By.ID, "checkout").click()
    sem_itens_para_compra = driver.find_element(By.CLASS_NAME, "title")
    assert sem_itens_para_compra.text == "Impossível finalizar a compra! Adicione ao menos 1 item no carrinho para continuar!", f"Carrinho vazio, erro na finalização da compra"