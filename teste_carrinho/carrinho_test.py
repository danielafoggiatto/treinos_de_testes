from selenium.webdriver.common.by import By
import pytest

def test_adicionar_ao_carrinho(driver): 
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-link']").click()

    itens = driver.find_elements(
    By.XPATH, "//*[@data-test='inventory-item-name']")

    assert len(itens) == 2


def test_remover_item(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-link']").click()

    remove_item = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_item.click()

    itens = driver.find_elements(
    By.XPATH, "//*[@data-test='inventory-item-name']")

    assert len(itens) == 1
    driver.find_element(By.ID, "continue-shopping").click()

def test_finalizar_compra(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-link']").click()

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Daniela")
    driver.find_element(By.ID, "last-name").send_keys("Foggiatto")
    driver.find_element(By.ID, "postal-code").send_keys("000000-000")

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    finalizado = driver.find_element(By.XPATH, "//*[text()='Thank you for your order!']")

    assert finalizado.text == "Thank you for your order!"