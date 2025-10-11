# Interacción con Productos - Selenium + Python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración inicial
driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 1️⃣ Ingresar al sitio y loguearse
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar a que cargue la página de inventario
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 2️⃣ Agregar el primer producto al carrito
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto.find_element(By.TAG_NAME, "button").click()

    # 3️⃣ Verificar que el contador del carrito se incremente a "1"
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
    )
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", "El contador del carrito no se incrementó correctamente"
    print("✅ Contador del carrito incrementado correctamente")

    # 4️⃣ Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Esperar a que aparezca el producto en el carrito
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    # 5️⃣ Verificar que el producto agregado aparece correctamente
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto == producto_en_carrito, "El producto del carrito no coincide con el agregado"
    print(f"✅ Producto '{producto_en_carrito}' aparece correctamente en el carrito")

    print("\n🎯 TEST PASSED: Interacción con productos completada exitosamente")

finally:
    driver.quit()
