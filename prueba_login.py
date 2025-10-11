# Automatización de Login
# 1. Navegar a la página de login de saucedemo.com
# 2. Ingresar credenciales válidas (usuario: standard_user, contraseña: secret_sauce)
# Validar login exitoso verificando que se haya redirigido a la página de inventario

# Criterios mínimos de aceptación:
# Login automatizado con espera explícita y validación de /inventory.html y "Products/Swag Labs".

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
    # driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(5)

    # validacion de la redireccion de la pagina 
    assert '/inventory.html' in driver.current_url
    print("Login exitoso y redireccion correcta a /inventory.html")

    # Validacion del Titulo
    print("Titulo:", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)

finally:
    driver.quit()