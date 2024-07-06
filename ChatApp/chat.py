import socket
from tkinter import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.40.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect():
    try:
        client.connect(ADDR)
    except Exception:
        print("e")

connect()


    

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


    
    
connected = True

while connected:
    message = input("Message: ")
    if message == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        connected = False
    send(message)