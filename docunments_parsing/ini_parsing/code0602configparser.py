# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  0.0.1
------------------------------------
@File           :  code0602configparser.py
@Description    :  
@CreateTime     :  2020/6/2 0002 下午 23:21
------------------------------------
@ModifyTime     :  
"""
import configparser
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('interpolation.ini')
print(config.sections())
for section in config.sections():
    print('-'*50)
    print(section)
    for key in config[section]:
        print(key,'-->',config[section][key])