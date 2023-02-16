from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element(By.ID, "num1").text
    number_2 = browser.find_element(By.ID, "num2").text
    summ = str(int(number_1) + int(number_2))
    # .text() - принимает в качестве значения строку! (Тип данных строка str) для корректной суммы надо
    # перевести два числа a и b  в int;
    # (Тип данных число int),
    # затем сумму (a + b) обратно в строку, т.к. значения в открывающемся списке находятся в строчном формате

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=summ)

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

# browser.find_element_by_css_selector("[value='" + y + "']")
finally:
    time.sleep(6)
    browser.quit()