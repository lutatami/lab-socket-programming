# coding: utf-8
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5001
server_addr = (UDP_IP, UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

while True:
    message = input("Input: ")
    sock.sendto(message.encode(), server_addr) 
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode('utf-8'))

