from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.105"
PORT = 8080

GENE = "U5"
FOLDER = "../Session04/"
FILENAME = "U5.txt"
DNA_FILE = FOLDER + FILENAME

clnt = Client(IP, PORT)

print(clnt)

# -- Read the Gene from a file

s =Seq().read_fasta(DNA_FILE)


# -- Send the Gene
clnt.debug_talk(f"Sending {GENE} Gene to the server...")
clnt.debug_talk(str(s))
