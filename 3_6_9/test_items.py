import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_transmission(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button.btn-add-to-basket')
    assert add_to_basket
