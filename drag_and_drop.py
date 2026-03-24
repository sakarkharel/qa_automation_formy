from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Drag and Drop']"))
    )
    form_button.click()
    time.sleep(3)

def drag_and_drop(driver):
    drag = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='image']//img")))
    drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='box']")))
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    time.sleep(5)

def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    drag_and_drop(driver)
    driver.quit()

if __name__ == "__main__":
    main()


