# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  0.0.1
------------------------------------
@File           :  code0620_yaml_parse.py
@Description    :  
@CreateTime     :  2020/6/20 0020 下午 17:07
------------------------------------
@ModifyTime     :  
"""
from yaml import safe_load

class YamlParser:
    def __init__(self, conf):
        with  open(conf, 'r', encoding='utf8') as f:
            config = safe_load(f)

        for key, value in config.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        return self[item]




if __name__ == '__main__':
    t = YamlParser('test.yaml')
