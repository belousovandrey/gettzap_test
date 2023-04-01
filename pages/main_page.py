import time

import requests
from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def check_regions_cookies(self):
        self.element_is_visible(self.locators.REGIONS_BUTTON).click()
        self.element_is_visible(self.locators.COOKIE_BUTTON).click()

    def login_page_account(self):
        self.element_is_visible(self.locators.MAIN_LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.LOGIN).send_keys('bel3105@rambler.ru')
        self.element_is_visible(self.locators.PASSWORD).send_keys('FYlAEGoL')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(0.25)
        result = self.element_is_not_present(self.locators.LOGIN_ERROR)
        return result

    def registration_account(self):
        self.element_is_visible(self.locators.MAIN_LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.REG_USER_BUTTON).click()
        self.element_is_visible(self.locators.FIO_USER).send_keys('Николаев Андрей')
        self.element_is_visible(self.locators.PHONE_USER).send_keys('89109109419')
        self.element_is_visible(self.locators.EMAIL_USER).send_keys('bel3105@rambler.ru')
        self.element_is_visible(self.locators.AGREEMENT_BOX).click()
        self.element_is_visible(self.locators.REGISTRATION_BUTTON).click()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.ORDER_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            self.element_is_visible(self.locators.ORDER_LINK_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code