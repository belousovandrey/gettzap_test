import time

from pages.main_page import MainPage


class TestLoginPage:

    def test_login_page(self, driver):
        login_page = MainPage(driver, 'https://gettzap.ru/')
        login_page.open()
        login_page.check_regions_cookies()
        result = login_page.login_page_account()
        assert result != True, "Запрашиваемый ресурс не был найден Неверный логин или пароль"

    def test_registration_page(self, driver):
        registration_page = MainPage(driver, 'https://gettzap.ru/')
        registration_page.open()
        registration_page.check_regions_cookies()
        registration_page.registration_account()
        time.sleep(3)

    def test_check_link(self, driver):
        links_page = MainPage(driver, 'https://gettzap.ru/')
        links_page.open()
        links_page.check_regions_cookies()
        links_page.login_page_account()
        time.sleep(3)
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken or url is incorrect"