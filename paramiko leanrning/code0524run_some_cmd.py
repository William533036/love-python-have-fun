# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  0.0.1
------------------------------------
@File           :  code0524run_some_cmd.py
@Description    :  
@CreateTime     :  2020/5/24 0024 下午 16:49
------------------------------------
@ModifyTime     :  
"""


import time

import paramiko

class InteractToServer:
    def __init__(self, host, pwd, port=22, username="root"):
        self._host = host
        self._pwd = pwd
        self._port = port
        self._username = username
        self._connection()


    def _connection(self):
        self.trans = paramiko.Transport(sock=(self._host, self._port))
        self.trans.start_client()
        # 用户名密码方式
        self.trans.auth_password(username=self._username, password=self._pwd)
        self.channel = self.trans.open_session()
        self.channel.settimeout(7200)
        # 获取一个终端
        self.channel.get_pty(width=200,height=200,)
        # 激活器
        self.channel.invoke_shell()

    def send_cmd(self, cmd_result_tuple):
        self.channel.send(cmd_result_tuple[0]+"\n")
        while True:
            time.sleep(0.2)
            rst = self.channel.recv(1024)
            rst = rst.decode('utf-8')
            print("+++++++++")
            print(rst)
            print("+++++++++")
            # 通过命令执行提示符来判断命令是否执行完成
            if cmd_result_tuple[1] in rst:
                # self.channel.send('yes\r')  # 【坑3】 如果你使用绝对路径，则会在home路径建立文件夹导致与预期不符
                break

    def close_connection(self):
        self.channel.close()
        self.trans.close()


if __name__ == '__main__':
    terminal = InteractToServer(host="192.168.1.115", port=22,username='root', pwd="")
    cmd = ('ls','anaconda' )
    terminal.send_cmd(cmd)
    cmd = ('cd /home','home' )
    terminal.send_cmd(cmd)
    cmd = ('ll','home' )
    terminal.send_cmd(cmd)
    cmd = ('cd huangyingjie','huangyingjie' )
    terminal.send_cmd(cmd)
    cmd = ('ll','projects' )
    terminal.send_cmd(cmd)
    terminal.close_connection()
