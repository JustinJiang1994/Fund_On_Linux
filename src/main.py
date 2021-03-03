# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


from logger import MyLogger
from monitor import FundMonitor

logger = MyLogger().get_logger()

if __name__ == '__main__':
    fund_monitor =FundMonitor()
    fund_monitor.get_info("000001")