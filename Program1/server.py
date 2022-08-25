import socket, random
from termcolor import colored, cprint
from utility.utils import COLORS

PORT = 9000
address = ("127.0.0.1", PORT)

users = {}

hostServer = socket.create_server(address,reuse_port=True)
hostServer.listen(1000)

with open('./heading.txt', 'rb') as f:
    lines = f.readlines()

print("\n")
for line in lines:
    print(line.decode(),end="")

print(f"Inspired by @udiptapathak13")

while (True):
    client, address = hostServer.accept()
    _ , CLIENT_PORT = address
    data = client.recv(100)

    if (not users.get(CLIENT_PORT)):
        users[CLIENT_PORT] = COLORS[random.randint(0,len(COLORS)-1)]
    cprint(data.decode(),users[CLIENT_PORT])
    client.close()

hostServer.close()
