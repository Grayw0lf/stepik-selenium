from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

with webdriver.Chrome() as browser:
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("test@test.ru")
    file = browser.find_element_by_name('file')
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
