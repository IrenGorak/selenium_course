import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    # # проверяем значение атрибута checked у people_radio
    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"
    #
    # # проверяем значение атрибута checked у robots_radio
    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # print("value of robots_radio: ", robots_checked)
    # assert robots_checked is None
    #
    # # проверяем значение атрибута disabled у кнопки Submit
    # button = browser.find_element_by_css_selector('.btn')
    # button_disabled = button.get_attribute("disabled")
    # print("value of button Submit: ", button_disabled)
    # assert button_disabled is None
    #
    # # проверяем значение атрибута disabled у кнопки Submit после таймаута
    # time.sleep(10)
    # button_disabled = button.get_attribute("disabled")
    # print("value of button Submit after 10sec: ", button_disabled)
    # assert button_disabled is not None

finally:
    time.sleep(5)
    browser.quit()
    
