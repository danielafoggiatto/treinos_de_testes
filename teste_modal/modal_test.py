from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modal(driver):
    imagem = driver.find_element(By.XPATH, "(//img[@alt='ecommerce website products'])[1]")

    ActionChains(driver).move_to_element(imagem).perform()

    botao_add = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[contains(@class,'overlay-content')]//a[contains(@class,'add-to-cart')])[1]")))

    botao_add.click()

    modal = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal-title') and text()='Added!']")))

    assert modal.text == "Added!"
