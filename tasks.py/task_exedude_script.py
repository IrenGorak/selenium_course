import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    browser.find_element(By.CSS_SELECTOR, "input[type='radio'][value='robots']").click()

    button.click()

finally:
    time.sleep(3)
    browser.quit()
