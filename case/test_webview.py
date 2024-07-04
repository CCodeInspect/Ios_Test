# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4


# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/2
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup_class(self):
        # 第一次初始化app
        # if self.driver == None:
        # android studio 提供的虚拟机chrome浏览器的版本为124
        # 所以在配置chromedriverExecutable为124版本的驱动
        # 驱动要和移动设备版本一致
        capabilities = {
            "platformName": "iOS",
            "appium:automationName": "XCUITest",
            "appium:bundleId": "com.11zhihu.aaa",
            "appium:udid": "8FE759FA-1D0C-4064-9126-751531CB0BAB",
            "appium:showXcodeLog": True,
            "appium:deviceName": "iPhone 15"
        }

        appium_server_url = "http://127.0.0.1:4723"

        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=UiAutomator2Options().load_capabilities(caps=capabilities)
        )
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        search_lo = (AppiumBy.XPATH, '//label')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_lo))

        ele = self.driver.find_element(*search_lo)
        self.driver.execute_script("arguments[0].click();", ele)  # Use JavaScript to click the element
        self.driver.find_element(AppiumBy.XPATH, '//*[@id="index-kw"]').send_keys("appium")
        search_locator = (AppiumBy.XPATH, '//*[@id="index-bn"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()
