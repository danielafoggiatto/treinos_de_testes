from selenium.webdriver.common.by import By

def test_menu_home(driver):
    driver.find_element(By.XPATH, "//a[text()='Udemy Courses']").click()
    driver.find_element(By.XPATH, "(//a[text()='Home'])[1]").click()

    home = driver.find_element(By.XPATH, "//a[text()='GUI Elements']")

    assert home.text == "GUI Elements"

def test_menu_udemy_courses(driver):
    driver.find_element(By.XPATH, "//a[text()='Udemy Courses']").click()

    udemy = driver.find_element(By.XPATH, "//u[text()='UDEMY COURSES']")

    assert udemy.text == "UDEMY COURSES"
    

def test_menu_online_trainings(driver):
    driver.find_element(By.XPATH, "//a[text()='Online Trainings']").click()

    udemy = driver.find_element(By.XPATH, "//u[text()='UDEMY COURSES']")

    assert udemy.text == "UDEMY COURSES"

def test_menu_blog(driver):
    driver.find_element(By.XPATH, "//a[text()='Blog']").click()

    trainings = driver.find_element(By.XPATH, "(//*[contains(text(),'Hands-on SQL exercises')])[1]")

    assert trainings.text == "Hands-on SQL exercises"

def test_menu_playright_practice(driver):
    driver.find_element(By.XPATH, "//a[text()='PlaywrightPractice']").click()

    playright = driver.find_element(By.XPATH, "//*[contains(@class, 'post-title')]")

    assert playright.text == "PlaywrightPractice"