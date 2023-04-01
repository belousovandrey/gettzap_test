import time

from pages.main_page import MainPage


class TestLoginPage:

    def test_login_page(self, driver):
        login_page = MainPage(driver, 'https://gettzap.ru/')
        login_page.open()
        login_page.check_regions_cookies()
        result = login_page.login_page_account()
        assert "Запрашиваемый ресурс не был найден Неверный логин или пароль" != result.text, "Запрашиваемый ресурс не был найден Неверный логин или пароль"

    def test_registration_page(self,driver):
        registration_page = MainPage(driver, 'https://gettzap.ru/')
        registration_page.open()
        registration_page.check_regions_cookies()
        registration_page.registration_account()
        time.sleep(3)