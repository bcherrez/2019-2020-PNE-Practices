
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")


conn = http.client.HTTPConnection(SERVER, PORT)

#Send the request message, using the GET method.

try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse()


print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode("utf-8")

# -- Create a variable with the data, form the JSON received
person = json.loads(data1)

print("CONTENT: ")


print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])

termcolor.cprint("Age: ", 'green', end="")
print(person['age'])


phoneNumbers = person['phoneNumber']


termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))


for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue')


    termcolor.cprint("    Type: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'red', end='')
    print(num['number'])