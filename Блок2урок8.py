from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:

    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element_by_name('firstname')
    first_name.send_keys('Dron')
    last_name = driver.find_element_by_name('lastname')
    last_name.send_keys('Skm')
    email = driver.find_element_by_name('email')
    email.send_keys('test@gmail.com')
    element = driver.find_element_by_id('file')
    x = element.get_attribute('type')
    current_dir = os.path.abspath(os.path.dirname('testfile.txt'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'testfile.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    submit = driver.find_element_by_class_name('btn').click()

finally:
    time.sleep(30)

    driver.quit()