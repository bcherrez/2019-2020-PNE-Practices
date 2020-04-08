import socket
import termcolor

PORT = 8080
IP = "192.168.1.105"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Avoid the problem of Port already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


s.bind((IP, PORT))

# socket for listening
s.listen()

print("The server is configured!")

while True:

    print("Waiting for Clients to connect")

    try:
        (client_socket, client_ip_port) = s.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")

        s.close()
        exit()

    else:

        print("A client has connected to the server!")
        message_raw = client_socket.recv(2000)

        message = message_raw.decode()

        print("Message received: ", end="")
        termcolor.cprint(message, "green")

        response = "ECHO: " + message + "\n"
        client_socket.send(response.encode())
        client_socket.close()