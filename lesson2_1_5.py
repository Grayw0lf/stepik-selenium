from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    robots_rule = browser.find_element_by_id('robotsRule')
    robots_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
