
import json
import termcolor
from pathlib import Path


jsonstring = Path("people-1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'


firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']


print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)