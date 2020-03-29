from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)

print(c1)
print(c2)

s = Seq().read_fasta(FOLDER + GENE + EXT)

bases = str(s)

print(f"Gene {GENE}: {bases}")

LENGTH = 10

# -- Send the initial message to both servers
init_msg = f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases..."

c1.talk(init_msg)
c2.talk(init_msg)

for i in range(10):

    frag = bases[i*LENGTH:(i+1)*LENGTH]

    print(f"Fragment {i+1}: {frag}")

    msg = f"Fragment {i+1}: {frag}"

    # -- even fragments (counting from 0) are sent to server 1
    if i % 2:
        c2.talk(msg)

    # -- Odd segments are sent to server 2
    else:
        c1.talk(msg)