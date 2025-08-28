from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def test_ordenacao_a_z(driver):
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("az")

    produtos = driver.find_elements(By.CLASS_NAME, "inventory-item_name")
    nomes = [p.text for p in produtos]

    assert nomes == sorted(nomes), f"Produtos não estao em ordem de A-Z: {nomes}"


def test_ordenacao_z_a(driver):
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("za")

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item_name ")
    nomes = [p.text for p in produtos]

    assert nomes == sorted(nomes, reverse= True), f"Produtos não estão em ordem Z-A: {nomes}"


def test_ordenacao_lowtohigh(driver):
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")

    elementos_precos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precos = [float(p.text.replace("$", "")) for p in elementos_precos]                            

    assert precos == sorted(precos), f"Preços não estão em ordem crescente: {precos}"


def test_ordenacao_hightolow(driver):
    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("hilo")

    elementos_precos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precos = [float(p.text.replace("$", "")) for p in elementos_precos]

    assert precos == sorted(precos, reverse= True), f"Preços não estão em ordem decrescente: {precos}"