import time

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_regions_cookies(self):
        self.element_is_visible(self.locators.REGIONS_BUTTON).click()
        self.element_is_visible(self.locators.COOKIE_BUTTON).click()
        self.element_is_visible(self.locators.MAIN_LOGIN_BUTTON).click()

    def login_page_account(self):
        self.element_is_visible(self.locators.LOGIN).send_keys('bel3105@rambler.ru')
        self.element_is_visible(self.locators.PASSWORD).send_keys('bel3105@rambler.ru')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        result = self.element_is_present(self.locators.LOGIN_ERROR)
        return result
        time.sleep(5)
