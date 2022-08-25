import socket, time
from  termcolor import cprint


BUFFER_SIZE = 1024
HOST = "127.0.0.1"
PORT = 9000

address = (HOST,PORT)

hostServer = socket.create_server(address,reuse_port=True)
hostServer.listen(1000)

print("\n"*100)
cprint("Waiting for file Transfer...",'green')

temp = str(time.time()).replace('.','_')
f = open(f"files/{temp}",'ab')

while True:
    client, address = hostServer.accept()
    data = client.recv(BUFFER_SIZE)
    f.write(data)
    client.close()

hostServer.close()

