# -*- coding: utf-8 -*-

"""
Created on 3/3/21 2:16 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import json
import logging

class config_tooler(object):
    def __init__(self):
        self.global_config_path = '../config/global_config.json'
        self.total_fund_path = '../data/total_fund.json'
        self.logging_path = '../log/monitor.log'
        self.target_fund = ["000171", "001102", "005827", "006229", "100038", "110011", "161005", "161017"]

    def build_tooler(self):
        try:
            with open(self.global_config_path, 'w', encoding='utf-8') as file:
                json.dump(self.__dict__, file, ensure_ascii=False, indent=1)
            print("config更新完成")
        except:
            print("config更新失败")


if __name__ == '__main__':
    test = config_tooler()
    test.build_tooler()