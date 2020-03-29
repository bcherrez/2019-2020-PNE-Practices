import socket
import termcolor

PORT = 8080
IP = "192.168.124.179"

# -- Create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Configure the socket for listening
ls.listen()

num_connections = 0

# -- List for storing info about clients
client_list = []

print("The server is configured!")

while num_connections < 5:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        num_connections += 1

        print(f"CONNECTION {num_connections}. Client IP,PORT: {client_ip_port}")

        # -- Store the client address in the list
        client_list.append(client_ip_port)
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        print("Message received: ", end="")
        termcolor.cprint(msg, "green")

        response = "ECHO: " + msg + "\n"

        cs.send(response.encode())

        cs.close()

print("The following clients has connected to the server: ")
for i, c in enumerate(client_list):
    print(f"Client {i}: {c}")

ls.close()