from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element_by_id('input_value')
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = x_element.text
    y = calc(x)

    answer = driver.find_element_by_id('answer')
    answer.send_keys(y)
    # Прокрутка страницы с помощью данного скрипта
    driver.execute_script('window.scrollBy(0, 120);')

    robot = driver.find_element_by_id('robotCheckbox')
    robot.click()

    robots_rule = driver.find_element_by_id('robotsRule')
    robots_rule.click()

    button = driver.find_element_by_class_name('btn')
    button.click()

finally:
    time.sleep(10)

    driver.quit()