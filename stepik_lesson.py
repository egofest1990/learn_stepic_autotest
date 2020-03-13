from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button.click()
browser.execute_script("window.scrollBy(0, 450);")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_value = browser.find_element_by_id("input_value")
x = x_value.text
y = calc(x)
button = browser.find_element_by_id("solve")
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_id("answer").send_keys(y)
button.click()

browser.quit()
