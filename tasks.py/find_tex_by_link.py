from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"


browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element(By.LINK_TEXT, "224592") #пошук по точному співпідінню назви лінки
link.click()
input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ira")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Horak")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Lvivv")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Ukraine")
button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
time.sleep(10)
browser.quit()

