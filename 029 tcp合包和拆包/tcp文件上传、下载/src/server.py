#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os, sys, struct, json
PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
USER = []


class Server(object):
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(('127.0.0.1', 9000))
        self.sk.listen()
        self.con, self.addr = self.sk.accept()


    def receive(self):

        if self.con.recv(1) == b'0':
            self.con.close()
            return

        s_first = self.con.recv(4)
        s_first = struct.unpack('i', s_first)[0]
        str_info = self.con.recv(s_first).decode('utf-8')
        info = json.loads(str_info)
        file_name = info['file_name']
        file_size = info['file_size']

        f = open(file_name, mode='wb')
        receive_size = 0
        while True:
            percent = round(receive_size / file_size * 100, 3)
            print('文件接收中，已接收%s%%\r' % percent, end='')
            if percent == 100.000: break
            content = self.con.recv(1024)
            f.write(content)
            receive_size += 1024
        print('文件接收完毕')
        f.close()

    def send(self):
        """
        解析用户即将下载的文件名
        """
        s_first = self.con.recv(4)
        s_size = struct.unpack('i', s_first)[0]
        file_name = self.con.recv(s_size).decode('utf-8')

        if not os.path.exists(file_name):
            self.con.send(b'qq')
            return
        self.con.send(b'ok')

        file_size = os.path.getsize(file_name)
        send_size = 0
        info = {'file_name': file_name, 'file_size': file_size}
        b_info = json.dumps(info).encode('utf-8')
        s_first = struct.pack('i', len(b_info))
        self.con.send(s_first)
        self.con.send(b_info)
        f = open(file_name, mode='rb')
        while True:
            percent = round(send_size / file_size * 100, 3)
            print('文件传输中，已传输%s%% \r' % (percent,), end='')
            chunk = f.read(1024)
            self.con.send(chunk)
            if not chunk: break
            send_size += 1024
        print('文件传输完成')


    def login(self):
        while True:
            if USER: break
            user_name = self.con.recv(1024).decode('utf-8')
            if user_name.strip().upper() == 'Q':
                break
            user_pwd = self.con.recv(1024).decode('utf-8')
            try:
                f = open('user.txt', mode='r', encoding='utf-8')
            except:
                print('用户信息已丢失')
                self.con.send('2'.encode('utf-8'))
                continue

            flag = False
            for i in f:
                name, pwd = i.split(':')
                if name == user_name and pwd == user_pwd:
                    flag = True
                    self.con.send('0'.encode('utf-8'))  # 登陆成功
                    USER.append(name)
                    break
            if flag:
                break
            else:
                self.con.send('1'.encode('utf-8'))  # 用户名或密码错误
        f.close()

    def run(self):
        while not USER: self.login()
        while True:
            choice = self.con.recv(1).decode('utf-8')
            if choice == '1':
                choice = 'receive'
            elif choice == '2':
                choice = 'send'
            elif choice.upper() == 'Q':
                self.con.close()
                break
            getattr(self, choice)()



Server().run()





