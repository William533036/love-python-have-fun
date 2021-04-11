# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  code2021-4-11.py
@Description    :  
@CreateTime     :  2021/4/11 0011 下午 19:24
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import os

import pytest

@pytest.fixture(scope="function",
                params=['成龙', '甄子丹', '菜10'],
                ids=['c1', 'zzd', 'c10'])
def demo_fixture(request):
    print("我执行在前面哦")
    yield request.param
    print("最后面是我执行哦")
class TestDemo:
    age=18

    def test_01_demo(self, demo_fixture):
        print("hello world!")
        print(str(demo_fixture))


    @pytest.mark.skipif(age>18, reason="已成年，满足条件")
    @pytest.mark.test
    def test_02_demo(self):
        print("hello 222!")
        assert 1==2

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./ --clean')