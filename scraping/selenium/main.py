from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
import time

USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    #% configurando nuestro navegador
    service = Service(ChromeDriverManager().install()) #$ si no tienes chrome instalalo y si ya actulizalo
    options = webdriver.ChromeOptions() #$ pasarle unos parametros a mi navegador
    #options.add_argument("--headless") #$ yo lo quiero correr en modo minimizado o sin entorno grafico
    options.add_argument("--window-size=1920,1080") #$ definiendole un tamaño a mi navegador
    driver = Chrome(service=service, options=options)
    driver.get("https://www.saucedemo.com/") #$ llamamos una ruta dentro de nuestro navegador
    
    #% opteniendo elemento y pasando valores
    #? loggin
    #*user
    user_input = driver.find_element(By.ID, "user-name") #$ encuentre un objeto por su id 
    user_input.send_keys(USER) #$ luego enviale el  valor que quiere agregarle
    #*password
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(PASSWORD)
    #* button seccion
    button = driver.find_element(By.ID,"login-button")
    button.click()

    #? compras

    #* button compra
    time.sleep(2)
    cx1 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
    cx1.click()

    cx2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
    cx2.click()

    #* carrito de compra
    time.sleep(2)
    carShop = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carShop.click()

    #* btn comprar
    time.sleep(2)
    shop = driver.find_element(By.ID,"checkout")
    shop.click()

    #* rellenar datos
    driver.find_element(By.ID,"first-name").send_keys("andres")
    time.sleep(2)
    driver.find_element(By.ID,"last-name").send_keys("narvaez")
    time.sleep(2)
    driver.find_element(By.ID,"postal-code").send_keys("869034")
    time.sleep(2)
    driver.find_element(By.ID,"continue").click()
    time.sleep(3)
    driver.find_element(By.ID,"finish").click()

    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
        main()