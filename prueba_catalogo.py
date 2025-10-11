# Navegación y Verificación del Catálogo
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 1️⃣ Ingresar al Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2️⃣ Validar redirección a la página de inventario
    assert "/inventory.html" in driver.current_url, "No redirigió al inventario"
    print("✅ Redirección correcta al catálogo")

    # 3️⃣ Validar el título de la página
    print("Título de la página:", driver.title)
    assert driver.title == "Swag Labs", "El título de la página no es correcto"
    print("✅ Título validado correctamente")

    # 4️⃣ Validar presencia de productos
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el catálogo"
    print(f"✅ Se encontraron {len(productos)} productos en el catálogo")

    # 5️⃣ Listar nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto → Nombre: {nombre} | Precio: {precio}")

    # 6️⃣ Validar elementos importantes de la interfaz
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed() and filtro.is_displayed(), "No se encontraron elementos clave (menú o filtro)"
    print("✅ Menú y filtro visibles en la interfaz")

    print("\n🎯 TEST PASSED: Navegación y verificación del catálogo correcta")

    time.sleep(2)

finally:
    driver.quit()
