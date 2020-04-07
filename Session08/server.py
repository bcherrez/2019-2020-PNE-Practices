import socket


PORT = 8080
IP = "192.168.1.105 "
# 127.0.0.1 ip ordenador

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
# become a server socket
serversocket.listen(50)
#  max_connections

while True:
    print("Waiting for connections")
    (clientsocket, address) = serversocket.accept()

# The server waits for the message to arrive
    msg = clientsocket.recv(2000)
    print("Message from client:", end="")
    message = "Hi,I am Belén"
    send_bytes = str.encode(message)

    clientsocket.send(send_bytes)

    clientsocket.close()
