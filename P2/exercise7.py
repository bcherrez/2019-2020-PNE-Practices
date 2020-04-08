
from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

FOLDER = "../Session04/"
GENE = "FRAT1"
FILENAME = "FRAT1.txt"
DNA_FILE = FOLDER + FILENAME

clnt1 = Client(IP, PORT)
clnt2 = Client(IP, PORT + 1)

print(clnt1)
print(clnt2)

s = Seq().read_fasta(DNA_FILE)

bases = str(s)

print(f"Gene {GENE}: {bases}")

LENGTH = 10

# -- Send the initial message to both servers
initial_message = f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases..."

clnt1.talk(initial_message)
clnt2.talk(initial_message)

for i in range(10):

    fragment = bases[i*LENGTH:(i+1)*LENGTH]

    print(f"Fragment {i+1}: {fragment}")

    message = f"Fragment {i+1}: {fragment}"

    # -- even fragments (counting from 0) are sent to server 1
    if i % 2:
        clnt2.talk(message)

    # -- Odd segments are sent to server 2
    else:
        clnt1.talk(message)