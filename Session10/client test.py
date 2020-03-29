from Client0 import Client

PORT = 8080
IP = "192.168.124.179"

for i in range(5):

    # -- Create a client object
    c = Client(IP, PORT)

    # -- Send a message to the server
    c.debug_talk(f"Message {i}")