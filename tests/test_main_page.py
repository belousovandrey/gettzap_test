import time

from pages.base_page import BasePage
from pages.main_page import MainPage


def test_login_page(driver):
    login_page = MainPage(driver, 'https://gettzap.ru/')
    login_page.open()
    login_page.check_regions_cookies()
    result = login_page.login_page_account()
    assert "Запрашиваемый ресурс не был найден Неверный логин или пароль" != result.text ,"Запрашиваемый ресурс не был найден Неверный логин или пароль"

