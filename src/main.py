# -*- coding: utf-8 -*-

"""
Created on 3/4/21 4:45 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from recorder import start_system_record, start_fund_record, start_time_record

if __name__ == '__main__':
    show_info_flag = True
    start_time_record(show_info_flag)
    start_system_record(show_info_flag)
    start_fund_record(show_info_flag)
