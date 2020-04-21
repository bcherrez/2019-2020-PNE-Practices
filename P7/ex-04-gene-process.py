import http.client
import json
import termcolor
from Seq1 import Seq


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

BASES = ['A', 'T', 'C', 'G']

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'


print()
NAME = input("Write the gene name: ")

REQ = ENDPOINT + GENES[NAME] + PARAMS
URL = SERVER + REQ

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", REQ)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse()


print(f"Response received!: {r1.status} {r1.reason}\n")


data1 = r1.read().decode()


GENE = json.loads(data1)

termcolor.cprint("Gene", 'green', end="")
print(f": {NAME}")
termcolor.cprint("Description", 'green', end="")
print(f": {GENE['desc']}")

GENE_SEQ = GENE['seq']

# -- Create the object sequence from the string
s = Seq(GENE_SEQ)

s_length = s.len()
ca = s.count_base('A')
pa = "{:.1f}".format(100 * ca / s_length)
cc = s.count_base('C')
pc = "{:.1f}".format(100 * cc / s_length)
cg = s.count_base('G')
pg = "{:.1f}".format(100 * cg / s_length)
ct = s.count_base('T')
pt = "{:.1f}".format(100 * ct / s_length)

termcolor.cprint("Total lengh", 'green', end="")
print(f": {s_length}")

termcolor.cprint("A", 'blue', end="")
print(f": {ca} ({pa}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {cc} ({pc}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {cg} ({pg}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {ct} ({pt}%)")

# Dictionary with the values
d_data = s.count()

# Create a list with all the values
l_values = list(d_data.values())

maximum = max(l_values)

termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {BASES[l_values.index(maximum)]}")