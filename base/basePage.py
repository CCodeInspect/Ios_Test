# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/6/29
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def back_to_previous(self):
        pass

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text
