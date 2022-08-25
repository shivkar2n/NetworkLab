import socket, sys, os
from  termcolor import cprint
from utility.utils import checkPort

BUFFER_SIZE = 1024

SERVER_PORT = 9000
serverAddress = ("127.0.0.1", SERVER_PORT)


fileName = sys.argv[1]


if not os.path.exists(fileName):
    exit()

f = open(fileName, "rb")

Loop = True

while Loop:
    CLIENT_PORT = checkPort()
    clientAddress = ("127.0.0.1", CLIENT_PORT)
    client = socket.socket()
    client.bind(clientAddress)
    client.connect(serverAddress)

    initialPos = f.tell()
    client.send(f.read(BUFFER_SIZE))
    finalPos = f.tell()

    print("\n"*100)
    cprint(f"Bytes transferred {initialPos}",'yellow')

    if (initialPos == finalPos):
        cprint("File transferred!",'green')
        Loop = False

    client.close()

