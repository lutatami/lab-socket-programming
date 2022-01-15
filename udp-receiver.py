import socket
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5001

# update in 20220115

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

print("20220115 20:04 New version of UDP server started !")
TEST_STR = "20220115 "
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("Update received message:", data.decode('utf8'), " from ", addr)
    currentTime = " " + time.ctime(time.time()) + "\r\n"
    data = TEST_STR.('ascii') + data + currentTime.encode('ascii')
    sock.sendto(data, addr)
