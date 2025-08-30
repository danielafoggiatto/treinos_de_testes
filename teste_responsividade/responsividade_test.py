from selenium.webdriver.common.by import By

def test_responsividade(driver):
    driver, (width, height) = driver

    login = driver.find_element(By.CLASS_NAME, "login_wrapper-inner")
    assert login.is_displayed(), f"Login não está visível na resolução {width}x{height}"
   