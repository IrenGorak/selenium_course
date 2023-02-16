import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys("Iren")

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input1.send_keys("Do")

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input1.send_keys("hj@mail.com")

    element = browser.find_element(By.XPATH, "//*[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join("/Users/ira/selenium_course.py", 'testt.txt')
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
