import socket
import threading

HEADER = 64
PORT = 5050
# makes my device the server to start a Local Network
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnected"

# Determine Address Family IPV4 and type of socket is TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"New Connection {addr} connected....")
    connected = True
    while connected:
        # first message is header of length 64 bytes indicating second message length
        # decode message from byte format into string using utf-8
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            # handle disconnection
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{addr} : {msg}")
    conn.close()

def start():
    server.listen()
    print(f"Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # create a thread for client, each thread handles client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections: {threading.activeCount() - 1}")


print("server is starting.....")

start()

