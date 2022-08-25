import socket
def checkPort():
    HOST = "127.0.0.1"
    PORT = 9000
    while (True):
        try:
            address = (HOST,PORT)
            S = socket.socket()
            S.bind(address)
            return PORT
        except Exception as e:
            PORT += 1


