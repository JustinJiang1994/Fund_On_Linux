# -*- coding: utf-8 -*-

"""
Created on 3/2/21 4:51 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import requests
import json
import re
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
                json.dump(self.__dict__, file, ensure_ascii=False)
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


class fund_watcher(object):
    def __init__(self, total_fund_path):
        # 浏览器头
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.pattern = r'^jsonpgz\((.*)\)'
        self.total_fund = None
        self.last_update_time = None

    def str2list(self, context: str) -> List:
        result = []
        start, end = 0, 0
        while start < len(context) and end <= len(context):
            if context[start] == '[':
                if context[end] == ']':
                    result.append(context[start + 1:end])
                    start = end + 1
            else:
                start += 1
            end += 1
        return result

    def preprocess(self, context: str):
        temp = self.str2list(context)
        result = dict()
        for idx in temp:
            data = idx.split(',')
            assert len(data) == 5
            fund_num = str(data[0].strip('\"'))
            fund_name = data[2].strip('\"')
            fund_type = data[3].strip('\"')
            if fund_num not in result:
                result.setdefault(fund_num, [fund_name, fund_type])
        return result

    def get_fund_type_list(self):
        print("正在更新所有基金列表")
        try:
            url = 'http://fund.eastmoney.com/js/fundcode_search.js'
            res = requests.get(url, headers=self.headers)
            context = re.findall('\[.*\]', res.text)
            context = context[0][1:-1]
            res = self.preprocess(context)
            # 存文件
            with open(self.total_fund_file, 'w', encoding='utf-8') as file:
                json.dump(res, file, ensure_ascii=False)
            print("基金获取并保存完成")
        except:
            print("获取所有基金列表失败")

    def get_info(self, fund_num: str):
        url = "http://fundgz.1234567.com.cn/js/%s.js" % fund_num
        try:
            res = requests.get(url, headers=self.headers)
            context = res.text
            re_result = re.findall(self.pattern, context)
            for idx in re_result:
                data = json.loads(idx)
                if self.last_update_time is None:
                    self.last_update_time = data['gztime']
                    print("-" * 30)
                    print("更新时间:{}".format(self.last_update_time))
                    print("-" * 30)
                if self.last_update_time != data['gztime']:
                    print("-" * 30)
                    print("更新时间:{}".format(self.last_update_time))
                    print("-" * 30)
                print("基金:{} | 收益率: {} %".format(data['name'], data['gszzl']))
        except:
            print("基金代码：{} ，搜索失败".format(fund_num))

    def read_total_fund(self):
        if not os.path.exists(self.total_fund_file):
            print("全量基金文件不存在")
            self.get_fund_type_list()
        with open(self.total_fund_file, 'r', encoding='utf-8') as file:
            self.total_fund = json.load(file)
            print("读取全量基金完成")

    def get_type(self, fund_num: str) -> List:
        if self.total_fund is None:
            self.read_total_fund()
        if fund_num in self.total_fund:
            return self.total_fund.get(fund_num)
        else:
            return []


if __name__ == '__main__':
    target_arr = ["000171", "001102", "005827", "006229", "100038", "110011", "161005", "161017"]
