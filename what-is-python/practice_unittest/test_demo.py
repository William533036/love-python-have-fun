# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  test_demo.py
@Description    :  
@CreateTime     :  2021/4/11 0011 上午 11:13
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

import warnings

@pytest.fixture()
def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1


def test_one():
    assert api_v1() == 1