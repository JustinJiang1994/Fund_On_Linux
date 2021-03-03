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
from threading import Timer
import datetime
import psutil
from logger import MyLogger
from utils import parse_json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
default_config_path = BASE_DIR + '/config/global_config.json'


class fund_monitor(object):
    """
    基金收益查看器
    """
    def __init__(self):
        # 浏览器头
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.pattern = r'^jsonpgz\((.*)\)'
        self.total_fund = None
        self.last_update_time = None
        self.global_config = parse_json(default_config_path)
        self.total_fund_file = self.global_config["total_fund_path"]
        self.logger = MyLogger().get_logger()

    def str2list(self, context: str) -> List:
        """
        用于处理回来的数据的第一步
        :param context:
        :return:
        """
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

    def preprocess(self, context: str) -> dict:
        """
        回来数据的预处理主入口
        :param context:
        :return: dict, 形式为fund_num, [fund_name, fund_type]
        """
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
        self.logger.info("正在更新所有基金列表")
        try:
            url = 'http://fund.eastmoney.com/js/fundcode_search.js'
            res = requests.get(url, headers=self.headers)
            context = re.findall('\[.*\]', res.text)
            context = context[0][1:-1]
            res = self.preprocess(context)
            # 存文件
            with open(self.total_fund_file, 'w', encoding='utf-8') as file:
                json.dump(res, file, ensure_ascii=False)
        except:
            self.logger.waring("获取所有基金列表失败")
        else:
            self.logger.info("基金获取并保存完成")


    def get_info(self, fund_num: str) -> str:
        url = "http://fundgz.1234567.com.cn/js/%s.js" % fund_num
        try:
            res = requests.get(url, headers=self.headers)
            context = res.text
            re_result = re.findall(self.pattern, context)
            for idx in re_result:
                data = json.loads(idx)
                fund_num = data["fundcode"]
                fund_type = self.get_type(fund_num)
                return "基金:{} | {} | 收益率: {} %".format(data['name'], fund_type, data['gszzl'])
        except:
            return "基金代码：{} ，搜索失败".format(fund_num)

    def read_total_fund(self):
        try:
            if not os.path.exists(self.total_fund_file):
                raise OSError("全量基金文件不存在")
                self.get_fund_type_list()
            with open(self.total_fund_file, 'r', encoding='utf-8') as file:
                self.total_fund = json.load(file)
        except OSError as e:
            self.logger.waring("读取全量基金失败，文件不存在：{}".format(e))
        else:
            self.logger.info("读取全量基金完成")

    def get_type(self, fund_num: str) -> List:
        if self.total_fund is None:
            self.read_total_fund()
        if fund_num in self.total_fund:
            return self.total_fund.get(fund_num)[1]
        else:
            return []


class system_monitor(object):
    def __init__(self):
        print()


class router(object):
    def __init__(self):
        print("当前时间：{}".format(datetime.datetime.now()))
        print("----- router 初始化完成 -----")


if __name__ == '__main__':
    monitor = fund_monitor()
    print(monitor.get_info("000001"))
