from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_formulario_aceita_dados_corretos(driver):
    driver.find_element(By.XPATH, "//*[@data-qa='name']").send_keys("Daniela")
    email = driver.find_element(By.XPATH, "//*[@data-qa='email']")
    email.send_keys("danielaf")
    driver.find_element(By.XPATH, "//*[@data-qa='submit-button']").click()
    
    validation_message = email.get_attribute("validationMessage")
    print(validation_message)
    
    assert "@" in validation_message, f"Esperado '@' na mensagem, mas foi: {validation_message}"

    