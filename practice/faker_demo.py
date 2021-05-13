# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  faker_demo.py
@Description    :  
@CreateTime     :  2021/5/13 0013 下午 18:45
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
from faker import Faker

faker = Faker(locale="zh")
for i in range(5):
    print(faker.name())
    print(faker.country())