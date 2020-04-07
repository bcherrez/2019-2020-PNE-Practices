import socket

PORT = 8080
IP = "192.168.124.179"

while True:
    m = input("Message to send: ")

    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    # Send data
    s.send(str.encode(m))

    s.close()
