# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  all.py
@Description    :  
@CreateTime     :  2021/4/11 0011 下午 22:52
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')