#!/usr/bin/env python3
#client

import socket

HOST = '127.0.0.1'
PORT = 42069

print("CLIENT")

# take in user input to send to server
message = input("say something! \n").encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(message)
    data = sock.recv(1024)

#print('Got', repr(data))