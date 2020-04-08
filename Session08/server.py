import socket


PORT = 8080
IP = "192.168.1.105"
# ip ordenador 127.0.0.1
number_con = 0


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
# become a server socket
serversocket.listen(50)
#  max_connections

while True:
    print("Waiting for connections at",IP,",",PORT)
    (clientsocket,address) = serversocket.accept()

# The server waits for the message to arrive
    number_con += 1
    print("CONNECTION: ", number_con, "From the IP: ", IP)

    msg = clientsocket.recv(2000)
    print("Message from client:", end="")
    message = "Hi,I am Belén"
    send_bytes = str.encode(message)
    print(message)
    clientsocket.send(send_bytes)

    clientsocket.close()
