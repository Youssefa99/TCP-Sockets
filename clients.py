import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnected"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Create a socket for client with IPV4 and type TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # encode message into utf-8
    message = msg.encode(FORMAT)
    msg_length = len(message)
    # Add message length
    send_length = str(msg_length).encode(FORMAT)
    # padding
    send_length += b' ' * (HEADER - len(send_length))
    print(len(send_length))
    client.send(send_length)
    client.send(message)



