# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  mydemo.py
@Description    :  
@CreateTime     :  2021/3/16 0016 下午 21:50
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s |%(lineno)d | %(message)s",
                        datefmt='%Y-%m-%d %H:%M:%S')
conslog = logging.StreamHandler(stream=sys.stdout)
conslog.setLevel(logging.DEBUG)
conslog.setFormatter(fmt)

logger.addHandler(conslog)

logger.debug(666666)
logger.info("测试日志")