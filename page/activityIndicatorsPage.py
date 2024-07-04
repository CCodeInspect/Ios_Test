# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4
from appium.webdriver.common.appiumby import AppiumBy

from base.app import App
from page.search import Search
from utils.logger import logger


class ActivityIndicatorsPage(App):
    _Activity_Indicator = (AppiumBy.IOS_PREDICATE, 'name == "Activity Indicators"')
    _Default = (AppiumBy.IOS_PREDICATE, 'name == "DEFAULT" AND label == "DEFAULT"')
    _Back = (
        AppiumBy.IOS_PREDICATE,
        'name == "UIKitCatalog" AND label == "UIKitCatalog" AND type == "XCUIElementTypeButton"')

    def click_activity_indicators(self):
        logger.info("点击activity indicators")
        self.find_and_click(*self._Activity_Indicator)
        self.find(*self._Default)

    def back_to_previous(self):
        logger.info("返回上一级")
        self.find_and_click(*self._Back)
        return Search()
