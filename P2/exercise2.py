
from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

# -- Create a client object
clnt = Client(IP, PORT)

# -- Print the IP and PORTs
print(clnt)