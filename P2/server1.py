
import socket


PORT = 8080
IP = "192.168.1.45"


number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))

    serversocket.listen(50)

    while True:

        print("Waiting for connections at  ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        print("CONNECTION: . From the IP: ".format(number_con, address))

        msg = clientsocket.recv(2000)
        print("Message from client: ", end="")

        message = "Message received from the Server"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)

        clientsocket.close()

except socket.error:
    print("Problems using port ".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()