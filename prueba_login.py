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
    time.sleep(5)

    # validacion de la redireccion de la pagina 
    assert '/inventory.html' in driver.current_url
    print("Login exitoso y redireccion correcta a /inventory.html")

    assert 'Products/Swag Labs' in driver.title
    print("Titulo de la pagina despues del login:", driver.title)
finally:
    driver.quit()