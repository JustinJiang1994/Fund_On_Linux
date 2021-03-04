# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from monitor import FundMonitor, SystemMonitor
from utils import parse_json
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

# system_period = global_config["record_system_period"]
system_period = 1.0
fund_period = global_config["record_fund_period"]

def start_system_record():
    line = sys_monitor.get_info()
    logger.info(line)
    Timer(system_period, start_system_record).start()

if __name__ == '__main__':
    start_system_record()