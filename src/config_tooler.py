# -*- coding: utf-8 -*-

"""
Created on 3/3/21 2:08 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import json
from typing import List
import os


class config_tooler(object):
    def __init__(self):
        self.config_path = './config.json'
        self.total_fund_path = './data/total_fund.json'
        self.total_fund = None
        self.target_fund = None

        if os.path.exists(self.config_path):
            self.read_config()


    def read_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readline()
            result = json.loads(lines)
        return result

    def show_attr(self):
        print(self.__dict__)

    def get_value(self, key: str):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            print("key-value对不吻合，请检查config文档")

    def update_config(self):
        try:
            with open(self.config_path, 'w', encoding='utf-8') as file:
                json.dump(self.__dict__, file, ensure_ascii=False, indent=1)
            print("config更新完成")
        except:
            print("config更新失败")

    def read_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key in data.keys():
                    self.__setattr__(key, data.get(key))
            print("config读取成功")
        except:
            print("config读取失败")

    def update_target(self, target_fund: List[str]):
        self.target_fund = target_fund


if __name__ == '__main__':
    tooler = config_tooler()
    tooler.update_config()
