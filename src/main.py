# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from monitor import FundMonitor, SystemMonitor
from logger import MyLogger
from utils import parse_json
import os


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_config_path = BASE_DIR + '/config/global_config.json'
    global_config = parse_json(global_config_path)
    target_fund = global_config.get("target_fund")

    sys_monitor = SystemMonitor()
    print(sys_monitor.get_info())

    fund_monitor = FundMonitor()
    for target in target_fund:
        print(fund_monitor.get_info(target))
