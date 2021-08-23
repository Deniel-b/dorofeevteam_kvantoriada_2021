import socket
import time

sock = socket.socket()
sock.connect(('192.168.1.52', 3000))
print("connected")

sock.send(b"positive_Y")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"negative_Y")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"negative_X")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"positive_X")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"negative_Z")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"positive_Z")
print(sock.recv(1024))

time.sleep(5)
sock.send(b"negative_rotating")
print(sock.recv(1024))
time.sleep(5)
sock.send(b"positive_rotating")
print(sock.recv(1024))
