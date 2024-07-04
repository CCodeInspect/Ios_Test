# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4
import pytest

from base.app import App
from utils.get_data_yaml import get_data_yaml
from utils.get_screenShot_and_pageSource import ui_screenshot_and_pagesource
from utils.logger import logger

data = get_data_yaml('../data/data.yaml')


class TestUiCatelog:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('text', data)
    @ui_screenshot_and_pagesource(on_success=True)
    def test_uicatelog(self, text):
        logger.info('开始执行测试case')
        self.main.find_activity_indicators()
        # .back_to_previous().click_search().click_default().send_text(text)
        # assert res == '123'
