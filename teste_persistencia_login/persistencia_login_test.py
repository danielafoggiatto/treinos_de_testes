from selenium import webdriver

def test_persistencia_login(login_session):
    driver2 = webdriver.Chrome()
    driver2.get("https://www.saucedemo.com/inventory.html")

    for cookie in login_session:
        driver2.add_cookie(cookie)

    driver2.refresh()

    assert "inventory.html" in driver2.current_url, "Login persistence failed"

    driver2.quit()