# -*- coding: utf-8 -*-

"""
Created on 3/3/21 11:43 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import time
import json
import os


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


def parse_json(file_name: str) -> dict:
    """
    读取json文件
    dumps是将dict转化成str格式，loads是将str转化成dict格式。
    dump和load也是类似的功能，只是与文件操作结合起来了。
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    str_lines = "".join(lines)
    if '\n' in str_lines:
        str_lines = str_lines.replace('\n', '')
    result = json.loads(str_lines)
    return result


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_config_path = BASE_DIR + '/config/global_config.json'
    print(parse_json(default_config_path))
    default_config_path = BASE_DIR + '/config/global_config1.json'
    print(parse_json(default_config_path))
