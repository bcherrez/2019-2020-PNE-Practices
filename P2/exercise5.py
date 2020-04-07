
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

FOLDER = "../Session04/"
EXT = ".txt"
GENE = "U5"

clnt = Client(IP, PORT)

print(clnt)

# -- Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)

# -- Send the Gene
clnt.debug_talk(f"Sending {GENE} Gene to the server...")
clnt.debug_talk(str(s))