import socket

PORT = 8080
IP = "192.168.124.179"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((IP, PORT))


s.send(str.encode("HELLO FROM THE CLIENT!!!"))

#Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

s.close()