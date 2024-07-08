# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/6/29
from appium.webdriver.webdriver import WebDriver


class BasePage:
    black_list = []

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except Exception as e:
            print("未找到元素，处理异常")
            for black in self.black_list:
                # 查找黑名单中的每一个元素
                eles = self.driver.find_elements(*black)
                if len(eles) > 0:
                    return self.find_and_send(by, locator)
            raise e

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_gettext(self, by, locator):
        return self.find(by, locator).text
