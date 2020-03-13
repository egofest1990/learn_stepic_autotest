import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()

    # Отправляем заполненную форм
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()