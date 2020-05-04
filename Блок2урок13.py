from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

driver = webdriver.Chrome()
driver.get(link)
# Говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной и когда цена будет 100
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = driver.find_element_by_id("book").click()
x_element = driver.find_element_by_id('input_value')
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
answer = driver.find_element_by_id('answer')
answer.send_keys(y)
submit = driver.find_element_by_id('solve').click()

time.sleep(20)
driver.quit()
