from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/form']"))
    )
    form_button.click()


def form_fill(driver):
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("ankit")

    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "last-name"))
    )
    last_name.send_keys("khanal")

    job_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "job-title"))
    )
    job_title.send_keys("CEO")

    education_level = driver.find_element(By.ID, "radio-button-2")
    education_level.click()

    sex = driver.find_element(By.ID, "checkbox-1")
    sex.click()



    select_element=driver.find_element(By.ID, "select-menu")
    select = Select(select_element)
    select.select_by_value("2")
    

    date_picker = driver.find_element(By.ID, "datepicker")
    date_picker.click()

    feb_24 = driver.find_element(By.XPATH, "//td[text()='24']")
    feb_24.click()
    
    time.sleep(3)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/thanks']"))
    )
    submit_button.click()
    time.sleep(5)


def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    main_page(driver)
    form_fill(driver)
    driver.quit()


if __name__ == "__main__":
    main()