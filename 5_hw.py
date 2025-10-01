from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CLASS_NAME, "btn_action")

        if username_field and password_field and submit_button:
            print("Элементы найдены")
    except NoSuchElementException:
            print("Элементы не найдены")
