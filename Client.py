import socket

PORT = 7501
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(msg):
    message = msg.encode('utf-8')
    message_length = len(message)
    send_length = str(message_length).encode('utf-8')
    send_length += b" " * (16 - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))

while True:
    sentMsg = input()
    send(sentMsg)