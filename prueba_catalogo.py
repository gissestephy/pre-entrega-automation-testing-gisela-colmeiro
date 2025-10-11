# Navegación y Verificación del Catálogo
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # Ingresar al Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(5)

    # validacion de la redireccion de la pagina 
    assert '/inventory.html' in driver.current_url

    # Validacion del Titulo
    print("Titulo:", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)

    # Valida productos
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")    
    productos[0].find_element(By.TAG_NAME,"button").click()  # Agregar primer producto al carrito
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

    print("TEST PASSED: Producto agregado al carrito correctamente.")

    time.sleep(5)

finally:
    driver.quit()