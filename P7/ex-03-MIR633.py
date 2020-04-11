import http.client
import json
import termcolor

# Sequence id endpoint
GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

NAME = 'MIR633'
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
REQ = ENDPOINT + GENES[NAME] + PARAMS
URL = SERVER + REQ

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", REQ)

except ConnectionRefusedError:
    print("Cannot connect to the Server")
    exit()


r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode()


gene = json.loads(data1)

termcolor.cprint("Gene", 'green', end="")
print(f": {NAME}")
termcolor.cprint("Description", 'green', end="")
print(f": {gene['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {gene['seq']}")