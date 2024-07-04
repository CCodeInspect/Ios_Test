# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/1
import yaml

import data
from utils.logger import logger


def get_data_yaml(file):
    logger.info("获取数据中")
    with open(file) as f:
        data = yaml.safe_load(f)
        return data
