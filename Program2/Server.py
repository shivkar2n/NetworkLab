import socket, time

BUFFER_SIZE = 1024
HOST = "127.0.0.1"
PORT = 9000

address = (HOST,PORT)

hostServer = socket.create_server(address,reuse_port=True)
hostServer.listen(1000)

print("Listening for files...")

temp = str(time.time()).replace('.','_')
f = open(f"files/{temp}",'ab')


while True:
    client, address = hostServer.accept()
    data = client.recv(1024)
    f.write(data)
    print(f.tell())
    client.close()

hostServer.close()

