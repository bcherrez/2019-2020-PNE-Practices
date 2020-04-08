import socket
import termcolor

PORT = 8080
IP = "192.168.1.105"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid the problem of Port already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


s.bind((IP, PORT))

s.listen()

number_con = 0

# -- List for storing info about clients
client_list = []

print("The server is configured!")

while number_con < 5:
    print("Waiting for Clients to connect")

    try:
        (client_socket, client_ip_port) = s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        s.close()
        exit()

    else:

        number_con += 1

        print("CONNECTION: ", number_con, "From the client IP,PORT: ", client_ip_port)

        # -- Store the client address in the list
        client_list.append(client_ip_port)
        message_raw = client_socket.recv(2048)
        message = message_raw.decode()

        print("Message received: ", end="")
        termcolor.cprint(message, "green")

        response = "ECHO: " + message + "\n"

        client_socket.send(response.encode())

        client_socket.close()

print("The following clients has connected to the server: ")
for i, c in enumerate(client_list):
    print(f"Client {i}: {c}")

s.close()