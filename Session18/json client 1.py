
# -- Example of a client that uses the HTTP.client library for requesting the main page from the server
import http.client

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")


conn = http.client.HTTPConnection(SERVER, PORT)

#Send the request message, using the GET method
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse()


print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode("utf-8")


print(f"CONTENT: {data1}")