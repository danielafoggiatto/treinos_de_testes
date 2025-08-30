import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navegacao_links(login_session):
    driver = login_session

    links_texto = [link.text for link in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    for nome in links_texto:
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nome))
        )
        link.click()

        detalhe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))
        )
        assert nome == detalhe.text

        driver.back()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
