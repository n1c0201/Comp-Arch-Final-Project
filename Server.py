# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:13:02 2021

@author: jerem
"""

import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS) 

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
        
        print(f"[{address}] {message}")
        connection.send("Message received".encode(FORMAT))
    
    connection.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target = handle_client, args = (connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Starting server...")
start()