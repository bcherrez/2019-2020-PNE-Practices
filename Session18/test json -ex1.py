import json
import termcolor
from pathlib import Path


jsonstring = Path("people-EX01.json").read_text()


persons = json.loads(jsonstring)

print(f"Total people in the Database: {len(persons)}")

for person in persons:


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

