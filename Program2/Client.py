import socket, sys, os
from utility.utils import checkPort

BUFFER_SIZE = 1024

SERVER_PORT = 9000
serverAddress = ("127.0.0.1", SERVER_PORT)

CLIENT_PORT = checkPort()
clientAddress = ("127.0.0.1", CLIENT_PORT)

fileName = sys.argv[1]


if not os.path.exists(fileName):
    exit()

f = open(fileName, "rb")

while True:
    if (f.tell() == ""):
        break

    client = socket.socket(socket.SO_REUSEADDR)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.bind(clientAddress)
    client.connect(serverAddress)
    print(f.tell())

    client.send(f.read(BUFFER_SIZE))
    f.seek(f.tell()+BUFFER_SIZE)

    client.close()

    f.seek(BUFFER_SIZE)


# client.close()
