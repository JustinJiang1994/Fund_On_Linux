# -*- coding: utf-8 -*-

"""
Created on 3/3/21 2:16 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class global_config_tooler(object):
    def __init__(self):
        self.global_config_path = BASE_DIR + '/config/global_config.json'
        self.total_fund_path = BASE_DIR + '/data/total_fund.json'
        self.target_fund = ["000171", "001102", "005827", "006229", "100038", "110011", "161005", "161017"]
        self.target_stock = ['601318', '600036']  # 中国平安, 招商银行
        self.target_mao = ['600519', '300274', '688169', '000858', '601888', '600760', '000333', '000538', '300015',
                           '002352']  # 茅系列
        self.target_index = ['hs300', 'zh500', 'zxb', 'cyb']  # 沪深300, 中证500, 中小板, 创业版

        self.logging_path = BASE_DIR + '/log/'

        self.record_system_period = 1.0 * 60 * 10
        self.record_time_period = 1.0 * 60 * 10

        self.record_fund_period = 1.0 * 60 * 5
        self.record_stock_period = 1.0 * 60 * 5
        self.record_index_period = 1.0 * 60 * 5

    def build_global_config(self):
        with open(self.global_config_path, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    test = global_config_tooler()
    test.build_global_config()
