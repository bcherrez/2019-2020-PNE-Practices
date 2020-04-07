import socket

# SERVER IP, PORT
PORT = 8080
IP= "192.168.124.179"


# create the socket
# parameters: AF_INET y SOCK_STREAM
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data
# Encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT"))

# Close the socket
s.close()