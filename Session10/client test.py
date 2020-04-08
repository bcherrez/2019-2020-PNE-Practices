from Client0 import Client

PORT = 8080
IP = "192.168.1.105"

for i in range(5):

    # -- Create a client object
    clnt = Client(IP, PORT)

    # -- Send a message to the server
    clnt.debug_talk(f"Message {i}")
