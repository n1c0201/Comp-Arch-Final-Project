import socket
import threading

PORT = 7501
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS) 

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    connected = True
    while connected:
        message_length = connection.recv(16).decode('utf-8')
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode('utf-8')
            if message == "Disconnect":
                connected = False
        
        print(f"[{address}] {message}")
        connection.send("Message received".encode('utf-8'))
    
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