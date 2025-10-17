# Sitio Web a Analizar: wwww.saucedemo.com
# Fecha de Entrega: 7 días a partir de la Clase 8
# Formato de Entrega: Código subido a Github
# Tecnologías a usar: Python, Pytest, Selenium WebDriver, Git y Github
# Estructura: 2 archivos separados (test y funciones aux) con comentarios descriptivos y usar nomenclatura significativa para los elementos

from selenium import webdriver
import time 

driver = webdriver.Chrome()

try: 
    driver.get("https://www.saucedemo.com/")
    print("Titulo:", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)
finally:
    driver.quit()