
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

#List for storing the A percentages
list_A = []

#Repeat the process for all the genes
for name in GENES:

    REQ = ENDPOINT + GENES[name] + PARAMS
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


    gene = json.loads(data1)

    termcolor.cprint("Gene", 'green', end="")
    print(f": {name}")
    termcolor.cprint("Description", 'green', end="")
    print(f": {gene['desc']}")

    genestr = gene['seq']

    #Create the object sequence from the string
    s = Seq(genestr)

    sl = s.len()
    ca = s.count_base('A')
    pa = "{:.1f}".format(100 * ca / sl)
    cc = s.count_base('C')
    pc = "{:.1f}".format(100 * cc / sl)
    cg = s.count_base('G')
    pg = "{:.1f}".format(100 * cg / sl)
    ct = s.count_base('T')
    pt = "{:.1f}".format(100 * ct / sl)

    termcolor.cprint("Total lengh", 'green', end="")
    print(f": {sl}")

    termcolor.cprint("A", 'blue', end="")
    print(f": {ca} ({pa}%)")
    termcolor.cprint("C", 'blue', end="")
    print(f": {cc} ({pc}%)")
    termcolor.cprint("G", 'blue', end="")
    print(f": {cg} ({pg}%)")
    termcolor.cprint("T", 'blue', end="")
    print(f": {ct} ({pt}%)")

    d = s.count()


    ll = list(d.values())


    m = max(ll)


    termcolor.cprint("Most frequent Base", 'green', end="")
    print(f": {BASES[ll.index(m)]}")

    # Add the A percentage to the list
    list_A.append(pa)

mpa = max(list_A)


i = list_A.index(mpa)

genes_list = list(GENES.keys())


# print(f"Maximum percentage of A's is in the {genes_list[i]} gene, with {mpa}%")