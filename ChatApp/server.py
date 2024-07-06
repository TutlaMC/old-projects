import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:

            msg_length = conn.recv(HEADER).decode(FORMAT)
        except ConnectionResetError:
            connected = False
        if msg_length:
            msg_length = int(msg_length)
            try:
                msg = conn.recv(msg_length).decode(FORMAT)
            except ConnectionResetError:
                connected = False
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"({addr}) {msg}")
            try:
                conn.send("Msg received".encode(FORMAT))
            except ConnectionResetError:
                connected = False

    conn.close()
        

def start():
    server.listen()
    print(f"Server: {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"People in app {threading.activeCount() - 1}")


print("Running")
start()