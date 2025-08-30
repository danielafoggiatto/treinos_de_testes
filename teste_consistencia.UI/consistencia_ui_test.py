from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_consistencia_ui(driver):
    botao_login = driver.find_element(By.ID, "login-button")
    cor_login = botao_login.value_of_css_property("background-color")
    fonte_login = botao_login.value_of_css_property("font-family")
    tamanho_fonte_login = botao_login.value_of_css_property("font-size")    
    
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.maximize_window()
    
    botao_inventory = driver.find_element(By.CLASS_NAME, "btn_inventory")
    cor_inv = botao_inventory.value_of_css_property("background-color")
    fonte_inv = botao_inventory.value_of_css_property("font-family")
    tamanho_fonte_inv = botao_inventory.value_of_css_property("font-size")

    assert cor_inv == cor_login, f"Cores de fundo diferentes: {cor_inv} vs {cor_login}"
    assert fonte_inv == fonte_login, f"Fontes diferentes: {fonte_inv} vs {fonte_login}"
    assert tamanho_fonte_inv == tamanho_fonte_login, f"Tamanhos de fonte diferentes: {tamanho_fonte_inv} vs {tamanho_fonte_login}"

    