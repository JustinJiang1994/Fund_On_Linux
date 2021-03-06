# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from monitor import FundMonitor, SystemMonitor, StockMonitor
from utils import parse_json, get_time
from logger import MyLogger
from threading import Timer
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
global_config_path = BASE_DIR + '/config/global_config.json'
global_config = parse_json(global_config_path)
target_fund = global_config.get("target_fund")

logger = MyLogger("looper.py").get_logger()

fund_monitor = FundMonitor()
sys_monitor = SystemMonitor()
stock_monitor = StockMonitor()

system_period = global_config["record_system_period"]
fund_period = global_config["record_fund_period"]
time_period = global_config["record_time_period"]
stock_period = global_config["record_stock_period"]
index_period = global_config["record_index_period"]


def start_system_record(print_info=False):
    line = sys_monitor.get_info()
    if print_info:
        print(line)
    logger.info(line)
    Timer(system_period, start_system_record).start()


def start_fund_record(print_info=False):
    lines = fund_monitor.get_target_fund_info()
    # for line in lines:
    #     if print_info:
    #         print(line)
    #     logger.info(line)
    # Timer(fund_period, start_system_record).start()


def start_time_record(print_info=False):
    current = get_time()
    formatter = "----- 当前时间为： {} -----".format(current)
    if print_info:
        print(formatter)
    logger.info(formatter)
    Timer(time_period, start_time_record).start()


def start_stock_record(print_info=False):
    lines = stock_monitor.get_total_stock()
    for line in lines:
        if print_info:
            print(line)
        logger.info(line)
    Timer(stock_period, start_stock_record).start()


def start_index_record(print_info=False):
    lines = stock_monitor.get_total_index()
    for line in lines:
        if print_info:
            print(line)
        logger.info(line)
    Timer(index_period, start_index_record).start()


def start_mao_record(print_info=False):
    lines = stock_monitor.get_total_mao()
    for line in lines:
        if print_info:
            print(line)
        logger.info(line)
    Timer(stock_period, start_mao_record).start()


if __name__ == '__main__':
    print_flag = True
    start_system_record(print_flag)
    start_time_record(print_flag)
    start_fund_record(print_flag)
    start_index_record(print_flag)
    start_stock_record(print_flag)
    start_mao_record(print_flag)
