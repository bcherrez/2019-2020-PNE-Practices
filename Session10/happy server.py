import socket

PORT = 8080
IP = "192.168.124.179"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

# -- Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:

        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)

        # -- We decode it for converting it readable
        msg = msg_raw.decode()
        print(f"Message received: {msg}")
        response = "HELLO. I am the Happy Server :-)\n"
        cs.send(response.encode())
        cs.close()



