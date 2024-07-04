# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4
from appium.webdriver.common.appiumby import AppiumBy

from base.app import TestApp
from utils.logger import logger


class Search(TestApp):
    _SEARCH = (AppiumBy.IOS_PREDICATE, '//XCUIElementTypeStaticText[@name="Search"]')
    _DEFAULT = (AppiumBy.IOS_PREDICATE, 'name == "Default"')
    _TEXT = (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"')

    def click_search(self):
        self.find_and_click(*self._SEARCH)
        return self

    def click_default(self):
        self.find_and_click(*self._DEFAULT)
        return self

    def send_text(self, text):
        text = self.find_and_send(*self._TEXT, text)
        logger.info("结束测试")
        return text
