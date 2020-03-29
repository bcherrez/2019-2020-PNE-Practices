import socket
import termcolor


PORT = 8081
IP = "192.168.1.45"
MAX_OPEN_REQUESTS = 50

# Counting the number of connections
number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the raw message from the client, if any
        # The server waits for the message to arrive
        msg = clientsocket.recv(2048)
        print("Message from client: ", end="")
        termcolor.cprint(msg.decode("utf-8"), 'green')

        message = "\n\nHello from the teacher's server\n\n"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)

        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()