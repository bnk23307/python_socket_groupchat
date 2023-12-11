#!/usr/bin/python3
import socket
from threading import Thread

name = input("name:")
s = socket.socket()
s.connect(('127.0.0.1',5554))

def recv():
    while True:
        data = s.recv(1024).decode('utf-8')
        if data == "uid:":
            s.send(name.encode('utf-8'))
        print(data)

def send():
    while True:
        msg = input(":>")
        s.send(msg.encode('utf-8'))
t1 = Thread(target=recv,args=())
t2 = Thread(target=send,args=())
t1.start()
t2.start()
