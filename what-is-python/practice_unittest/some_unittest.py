# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  some_unittest.py
@Description    :  
@CreateTime     :  2021/3/2 0002 下午 22:00
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import unittest

from some__function import some_func

class someTest(unittest.TestCase):

    def test_some_func(self):
        num = some_func("Hello")
        self.assertEqual(num, 5)

if __name__ == '__main__':
    unittest.main()
