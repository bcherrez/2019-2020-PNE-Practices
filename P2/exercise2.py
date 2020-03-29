from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Print the IP and PORTs
print(c)