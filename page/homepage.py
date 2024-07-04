# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4
from appium.webdriver.common.appiumby import AppiumBy

from base.app import App
from page.activityIndicatorsPage import ActivityIndicatorsPage
from utils.logger import logger


class HomePage(App):
    _Activity_indicators = (AppiumBy.IOS_PREDICATE, 'name == "Activity Indicators"')

    def find_activity_indicators(self):
        logger.info("查找activity indicators是否存在")
        self.find(*self._Activity_indicators)
        return ActivityIndicatorsPage()
