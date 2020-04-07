from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "192.168.1.105"
PORT = 8080

clnt = Client(IP, PORT)

# -- Test the ping method
clnt.ping()

print(f"IP: {clnt.ip}, {clnt.port}")