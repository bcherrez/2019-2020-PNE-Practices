import json
import termcolor
from pathlib import Path


jsonstring = Path("people-2.json").read_text()


person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'


print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age'])


phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))


for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue', end='')
    print(num)