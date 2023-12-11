#!/usr/bin/python3
import socket
from threading import Thread

server = socket.socket()
server.bind(('127.0.0.1',5554))
server.listen(1)
print("Server started listening for connnection at port:5555")

clients = []
names = []

def broadcast(message,cl):
    global clients
    for client in clients:
        if client!= cl:
            client.send(message.encode('utf-8'))


def handle(client):
    while True:
        index = clients.index(client)
        print(index)
        name = names[index]
        message = client.recv(1024).decode('utf-8')
        broadcast(f"{name}:{message}",client)

def recv():
    while True:
        conn,addr = server.accept()
        conn.send("uid:".encode('utf-8'))
        name = conn.recv(1024).decode('utf-8')
        print(f"{name} has joined the chat")
        clients.append(conn)
        names.append(name)
        t = Thread(target=handle,args=(conn,))
        t.start()
        # broadcast(f'{name} joined this chat')

recv()
