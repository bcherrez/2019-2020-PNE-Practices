
import socket

PORT = 8080
IP = "192.168.124.179"
import socket


PORT = 8080
IP = "192.168.124.179"

while True:
    m = input("Message to send: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
