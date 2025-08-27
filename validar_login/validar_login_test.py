from selenium.webdriver.common.by import By

def test_login_valido(driver):
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//*[contains(@class, 'btn') and text()='Login']").click()

    esperado = driver.find_element(By.ID, "flash")

    assert esperado.text == "You logged into a secure area!"

def test_login_invalido(driver):
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//*[contains(@class, 'btn') and text()='Login']").click()

    esperado = driver.find_element(By.ID, "flash")

    assert esperado.text == "Your password is invalid!"


def test_campo_vazio(driver):
    driver.find_element(By.XPATH, "//*[contains(@class, 'btn') and text()='Login']").click()

    esperado = driver.find_element(By.ID, "flash")

    assert esperado.text == "Your username is invalid!"