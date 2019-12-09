from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x1 = int(browser.find_element_by_id('num1').text)
    x2 = int(browser.find_element_by_id('num2').text)
    y = str(x1 + x2)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
