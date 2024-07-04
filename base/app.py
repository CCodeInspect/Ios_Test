# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/6/29
from appium import webdriver
from appium.options.android import UiAutomator2Options

from base.basePage import BasePage
from utils.logger import logger


class App(BasePage):
    def start(self):
        # 第一次初始化app
        # if self.driver == None:
        print("此时driver为None: ", self.driver)
        capabilities = {
            "platformName": "iOS",
            "appium:automationName": "XCUITest",
            "appium:bundleId": "com.11zhihu.aaa",
            "appium:udid": "8FE759FA-1D0C-4064-9126-751531CB0BAB",
            "appium:showXcodeLog": True,
            "appium:deviceName": "Phone 15"
        }
        # capabilities = {
        #     "platformName": "iOS",
        #     "appium:automationName": "xcuitest",
        #     "appium:bundleId": "com.11zhihu.aaa",
        #     "appium:udid": "00008101-001248DC22E0001E",
        #     "appium:showXcodeLog": True,
        #     "appium:deviceName": "iPhone 12 mini",
        #     "platformVersion": "17.5.1"
        # }

        appium_server_url = "http://127.0.0.1:4723"
        # 因为当前我只安装了appium server
        # 且appium server为appium2.11.1版本
        # 所以appium_server_url我没有传http://127.0.0.1:4723/wd/hub，会报错
        # 而是传了http://127.0.0.1:4723
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=UiAutomator2Options().load_capabilities(caps=capabilities)
        )
        self.driver.implicitly_wait(10)
        # else:
        #     # 直接启动app，节省启动app时间
        #     self.driver.activate_app(app_id="com.xueqiu.android")
        print("此时driver是个对象并且拿到了: ", self.driver)
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        logger.info("正在登录")
        from page.homepage import HomePage
        return HomePage(self.driver)
