from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects2.html'

    driver = webdriver.Chrome()
    driver.get(link)

    a = driver.find_element_by_id('num1')
    b = driver.find_element_by_id('num2')
    res = int(a.text) + int(b.text) # Переводим строки в числа и складываем

    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(res))

    button = driver.find_element_by_class_name('btn')
    button.click()

finally:
    time.sleep(20)
    driver.quit()
