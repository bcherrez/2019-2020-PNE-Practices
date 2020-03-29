import socket
import termcolor


PORT = 8080
IP = "192.168.1.45"
MAX_OPEN_REQUESTS = 50

number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:

        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        msg = clientsocket.recv(2048)
        print("Message from client: ", end="")
        termcolor.cprint(msg.decode("utf-8"), 'green')

        message = "Message received from the Server"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)

        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()