# -*- coding: utf-8 -*-

"""
Created on 3/3/21 11:43 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import time
import json


def int_to_time(int_time):
    """
    将int time时间戳转换为特定格式的时间
    :param int_time:
    :return:
    """
    time_arr = time.localtime(int_time)
    result = time.strftime("%Y-%m-%d %H:%M:%S", time_arr)
    return result


def time_to_int(str_time):
    """
    将时间格式转换为整数类型
    :param str_time:
    :return:
    """
    time_arr = time.strftime(str_time, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_arr))
    return time_stamp


def parse_json(file_name):
    """
    读取json文件
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readline()
        result = json.loads(lines)
    return result
