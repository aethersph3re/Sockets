#!/usr/bin/env python3
#server

import socket

HOST = '127.0.0.1'
PORT = 42069

# note AF_INET is meant for IPv4
# use 'with' to avoid needing to use the .close() function

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    connection, address = sock.accept()     

    with connection:
        print('Connected by', address)

        # the while loop listens for data - if nothing is received the 
        # connection is automatically closed for you 

        while True:
            data = connection.recv(1024)
            print('data:', data)
            if not data:
                break
            connection.sendall(data) 
