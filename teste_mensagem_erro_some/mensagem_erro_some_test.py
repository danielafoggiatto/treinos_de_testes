from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def test_mensagem_erro_some(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    senha = driver.find_element(By.ID, "password")
    senha.send_keys("123456")
    driver.find_element(By.ID, "login-button").click()
    mensagem_erro = driver.find_element(By.XPATH, "//*[@data-test='error']")
    assert mensagem_erro.text == "Epic sadface: Username and password do not match any user in this service"

    driver.refresh()

    mensagem_erro = driver.find_elements(By.XPATH, "//*[@data-test='error']")
    assert len(mensagem_erro) == 0


#Cria uma lista com find_elements() para verificar se tem 1 ou nenhum elemento na lista.. 
