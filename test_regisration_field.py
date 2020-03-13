import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc():
        z = str(int(x) + int(y))
        return z
    num_1 = browser.find_element_by_id("num1")
    num_2 = browser.find_element_by_id("num2")
    x = num_1.text
    y = num_2.text
    z = calc()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    browser.find_element_by_css_selector("button.btn.btn-default").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

