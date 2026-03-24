from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Radio Button']"))
    )
    form_button.click()
    time.sleep(3)

def radio_button(driver):
    # radiobutton1 = driver.find_element(by=By.ID, value = "radio-button-1")
    # radiobutton1.click()


    radiobutton2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='exampleRadios'][value='option2']"))
    )
    radiobutton2.click()


    # radiobutton3 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='exampleRadios'][value='option3']"))
    # )
    # radiobutton3.click()


    time.sleep(3)


def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    radio_button(driver)
    driver.quit()

if __name__ == "__main__":
    main()