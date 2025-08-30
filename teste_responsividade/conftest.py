from selenium import webdriver
import pytest

RESOLUTIONS = [
    (1920, 1080),  
    (1366, 768),  
    (375, 667),    
]

@pytest.fixture(params=RESOLUTIONS, ids=["Desktop", "Tablet", "Mobile"])
def driver(request):
    widht, height = request.param
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver, (widht, height)
    driver.quit()
