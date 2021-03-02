# -*- coding: utf-8 -*-

"""
Created on 3/2/21 4:51 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com

["000171", 001102, 005827, 006229, 100038, 110011, 161005, 161017, 161125, 161130]
"""

import requests
import json
import re
import datetime
from typing import List


class catcher(object):
    def __init__(self):
        # 浏览器头
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.pattern = r'^jsonpgz\((.*)\)'

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
            fund_num, fund_name, fund_type = data[0], data[2], data[3]
            if fund_num not in result:
                result.setdefault(fund_num, [fund_name, fund_type])
        return result

    def get_fund_type_list(self):
        print("正在更新所有基金列表")
        strtoday = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        try:
            url = 'http://fund.eastmoney.com/js/fundcode_search.js'
            res = requests.get(url, headers=self.headers)
            context = re.findall('\[.*\]', res.text)
            context = context[0][1:-1]
            res = self.preprocess(context)
            # 存文件
            with open('./data/total_fund.json', 'w', encoding='utf-8') as file:
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
                print("更新时间:{}".format(data['gztime']))
                print("基金:{} | 收益率: {} %".format(data['name'], data['gszzl']))
        except:
            print("基金代码：{} ，搜索失败".format(fund_num))


if __name__ == '__main__':
    test = catcher()
    code = "000171"
    # test.get_info(code)
    test.get_fund_type_list()
