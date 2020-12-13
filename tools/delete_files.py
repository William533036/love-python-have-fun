# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  delete_files.py
@Description    :  
@CreateTime     :  2020/12/13 0013 下午 13:19
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""

from pathlib import Path

def condition(name, rules):
    if rules in name:
        return True


def delete_flies(path, condition, rules):
    path_obj = Path(path)
    for file_ in path_obj.iterdir():
        if condition(file_.name, rules):
            file_.unlink()
            print(f"deleted file {file_.name}")

if __name__ == '__main__':
    rules = "(1)"
    path = r"D:\2019千锋网络安全：渗透测试项目实战-DC"
    delete_flies(path, condition, rules)