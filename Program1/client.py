import socket, termcolor
from utils import checkPort

SERVER_PORT = 9000
serverAddress = ("127.0.0.1", SERVER_PORT)

CLIENT_PORT = checkPort()
clientAddress = ("127.0.0.1", CLIENT_PORT)

name = input("Enter your name: ")
print("\n"*1000)

while (True):
    rawMsg = input()
    if (rawMsg == "exit"):
        break
    print("\n"*1000)

    client = socket.socket(socket.SO_REUSEADDR)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.bind(clientAddress)
    client.connect(serverAddress)

    msg = bytes(f"{name} : {rawMsg}",'utf-8')
    noBytes = client.send(msg)
    client.close()



