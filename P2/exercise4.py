
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

clnt = Client(IP, PORT)

print(clnt)

# -- Send a message to the server
clnt.debug_talk("First message")
clnt.debug_talk("Second message:Testing!!")