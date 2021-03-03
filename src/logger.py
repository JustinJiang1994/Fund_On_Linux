# -*- coding: utf-8 -*-

"""
Created on 3/3/21 2:07 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import logging
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
default_config_path = BASE_DIR + '/config/global_config.json'

with open(default_config_path, 'r', encoding='utf-8') as file:
    config_dict = json.load(file)


class logger(object):
    def __init__(self, project, level=logging.INFO):
        self.logger = logging.getLogger(project)  # 得到一个logger对象
        self.project = project
        file_handler = logging.FileHandler(config_dict["logging_path"] + project + '.log',
                                           encoding='utf-8')  # 指定输出的文件路径，将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(log_format)
        self.logger.addHandler(file_handler)  # 为logger添加的日志处理器
        self.logger.setLevel(level)  # 指定日志的最低输出级别，默认为Info级别

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    project_name = "monitor"
    test = logger(project_name).get_logger()
    test.critical("This is a critical log.")
