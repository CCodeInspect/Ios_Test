# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/4
import pytest

from base.app import TestApp
from utils.get_data_yaml import get_data_yaml
from utils.logger import logger

data = get_data_yaml('../data/data.yaml')


class TestUiCatelog:
    def setup_class(self):
        self.app = TestApp()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('text', data)
    def test_uicatelog(self, text):
        logger.info('开始执行测试case')
        res = self.main.find_activity_indicators().back_to_previous().click_search().click_default().send_text(text)
        assert res == '123'
