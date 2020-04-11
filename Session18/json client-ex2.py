import http.client
import json
import termcolor

PORT = 8080
SERVER = '127.0.0.1'

print(f"\nConnecting to server: {SERVER}, {PORT}\n")


conn = http.client.HTTPConnection(SERVER, PORT)

# Send the request message, using the GET method. We are

try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("Can not connect to the Server")
    exit()

r1 = conn.getresponse()


print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode("utf-8")


persons = json.loads(data1)

print("CONTENT: ")

print(f"Total people in the Database: {len(persons)}")

for person in persons:

    # Print the information on the console
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