from selenium.webdriver.common.by import By

def test_tamanho_botoes(driver):
    botao_login = driver.find_element(By.ID, "login-button")

    tamanho = botao_login.size
    largura = tamanho['width']
    altura = tamanho['height']

    assert largura >= 44 and altura >= 44, f"Tamanho do botão de login é {largura}x{altura}, deve ser pelo menos 44x44 pixels."