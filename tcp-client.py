#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import socket

IP = '3.34.178.210'
TCP_PORT = 54147
BUFFER_SIZE = 1024
MESSAGE = ''

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, TCP_PORT))
    MESSAGE = input('Input: ')
    if(MESSAGE=='q'):
        break
    s.send(MESSAGE.encode('utf-8'))
    print('Sending data:', MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print('Data from server:', data.decode('utf-8'))

s.close()
