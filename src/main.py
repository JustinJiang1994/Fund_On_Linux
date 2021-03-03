# -*- coding: utf-8 -*-

"""
Created on 3/3/21 4:00 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


from logger import MyLogger


logger = MyLogger().get_logger()
logger.critical("This is a critical log.")