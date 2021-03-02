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


class catcher(object):
    def __init__(self):
        # 浏览器头
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.pattern = r'^jsonpgz\((.*)\)'

    def get_info(self, fund_num: str):
        url = "http://fundgz.1234567.com.cn/js/%s.js" % fund_num
        res = requests.get(url, headers=self.headers)
        context = res.text
        re_result = re.findall(self.pattern, context)
        for idx in re_result:
            data = json.loads(idx)
            print("更新时间:{}".format(data['gztime']))
            print("基金:{} | 收益率: {} %".format(data['name'], data['gszzl']))


if __name__ == '__main__':
    test = catcher()
    code = "000171"
    test.get_info(code)
