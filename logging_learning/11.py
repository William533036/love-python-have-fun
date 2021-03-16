# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  11.py
@Description    :  
@CreateTime     :  2021/3/16 0016 下午 22:22
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import logging
import logging.config
import yaml

with open("log_conf.yaml","r", encoding="U8") as conf:
    logging.config.dictConfig(yaml.safe_load(conf))

logger = logging.getLogger("simpleExample")

logger.info(666666666)