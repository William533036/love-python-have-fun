# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  code2021-3-27_demo01.py
@Description    :  
@CreateTime     :  2021/3/27 0027 下午 15:56
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""
import urllib.request
uapools=[
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201", # QQ浏览器极速模式
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",   # 谷歌
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",   # 遨游
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"   # 火狐
    ]
url="http://blog.csdn.net"
#头文件格式 header=("User-Agent"，具体用户代理值)
headers=("User-Agent",uapools[0])
opener=urllib.request.build_opener()
opener.addheaders.append(headers)

data=opener.open(url)
print(data.read().decode("U8"))


ip="1.1.1.1:996"
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url="http://www/baidu.com"
data=urllib.request.urlopen(url).read().decode("utf-8", "ignore")
print(data)