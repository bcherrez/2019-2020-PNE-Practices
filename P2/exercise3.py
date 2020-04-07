
from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

clnt = Client(IP, PORT)

print(clnt)

# -- Send a message to the server
print("Sending a message to the server...")
response = clnt.talk("Hi, I am Belén")
print(f"Response: {response}")
