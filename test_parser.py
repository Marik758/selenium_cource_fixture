import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    assert browser.find_elements(By.XPATH, "//*[@id='add_to_basket_form']/button"), 'Button not found'
    time.sleep(3)
    browser.quit()
