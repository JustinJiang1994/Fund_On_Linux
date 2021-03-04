# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from monitor import FundMonitor, SystemMonitor
from logger import MyLogger



if __name__ == '__main__':
    sys_monitor = SystemMonitor()
    print(sys_monitor.get_info())

    fund_monitor = FundMonitor()
    print(fund_monitor.get_info("000001"))
