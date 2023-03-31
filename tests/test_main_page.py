import time

from pages.base_page import BasePage



def test_login_page(driver):
    login_page = BasePage(driver, 'https://gettzap.ru/')
    login_page.open()
    time.sleep(5)