import socket

PORT = 8080
IP = "192.168.1.105"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid the problem of Port already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((IP, PORT))

s.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (client_socket, client_ip_port) = s.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        s.close()
        exit()
    else:

        print("A client has connected to the server!")

        message_raw = client_socket.recv(2000)

        # -- We decode it for converting it readable
        message = message_raw.decode()
        print(f"Message received: {message}")
        response = "Hello. I am the Happy Server :-) \n"
        print({response})
        client_socket.send(response.encode())
        client_socket.close()



