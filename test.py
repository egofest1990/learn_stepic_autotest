import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    y = calc(x)
    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    button.click()
    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла