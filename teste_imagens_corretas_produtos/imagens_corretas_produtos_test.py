from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def test_imagens_corretas_produto(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    imagens = driver.find_elements(By.XPATH, "//img[@class='inventory_item_img']")
    assert imagens, "Nenhuma imagem de produto encontrada!"
     
    for img in imagens:
        assert img.is_displayed(), "Imagem não visível"
        src = img.get_attribute("src")

        response = requests.get(src)
        assert response.status_code == 200, f"Imagem quebrada: {src}"