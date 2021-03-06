# -*- coding: utf-8 -*-

"""
Created on 3/4/21 4:45 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from recorder import start_system_record, start_fund_record, start_time_record, start_index_record, start_stock_record, \
    start_mao_record

if __name__ == '__main__':
    print_info_flag = False
    start_time_record(print_info_flag)  # 时间
    start_system_record(print_info_flag)  # 系统状态
    start_fund_record(print_info_flag)  # 基金
    start_index_record(print_info_flag)  # 指数
    start_stock_record(print_info_flag)  # 特定股票
    start_mao_record(print_info_flag)  # 茅系股票
