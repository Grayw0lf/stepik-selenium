from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element(By.ID, 'book')
    button.click()
    browser.implicitly_wait(1)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
    time.sleep(10)
