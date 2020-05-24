# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  0.0.1
------------------------------------
@File           :  html2md.py
@Description    :  
@CreateTime     :  2020/5/24 0024 下午 20:18
------------------------------------
@ModifyTime     :  
"""

import codecs
import sys

import tomd


save_file = '/Library/temp/markdown.md'


def run():
    html = getHtml()

    createFile(mdTxt)


def createFile(mdTxt):
    f = codecs.open(save_file, 'w+', 'utf-8')
    f.write(mdTxt)
    # f.write(mdTxt)
    f.close()

from subprocess import Popen

import tomd

ARANGO_IMP_CMD = "python -m pydoc -w {}"

def run_arango_cmd(name):
    with Popen([ARANGO_IMP_CMD.format(name)], shell=True) as arango_imp_cmd:
        print(arango_imp_cmd)

with open("test.html", "r", encoding="utf8") as htmls:
    mdTxt = tomd.Tomd(htmls.read()).markdown

with open("test.md", "w", encoding="utf8") as mds:
    mds.write(mdTxt)
# run_arango_cmd("test")
