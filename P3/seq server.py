
import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

# -- Sequences for the GET command
SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


def get_comand(n):
    return SEQ_GET[n]


def info_comand(strseq):
    """INFO seq
    returns: The string with the information
    """
    #Create the object sequence from the string
    s = Seq(strseq)
    sl = s.len()
    ca = s.count_base('A')
    pa = "{:.1f}".format(100 * ca / sl)
    cc = s.count_base('C')
    pc = "{:.1f}".format(100 * cc / sl)
    cg = s.count_base('G')
    pg = "{:.1f}".format(100 * cg / sl)
    ct = s.count_base('T')
    pt = "{:.1f}".format(100 * ct / sl)

    resp = f"""Sequence: {s}
Total length: {sl}
A: {ca} ({pa}%)
C: {cc} ({pc}%)
G: {cg} ({pg}%)
T: {ct} ({pt}%)"""
    return resp


def comp_comand(strseq):
    s = Seq(strseq)
    return s.complement()


def rev_comand(strseq):
    s = Seq(strseq)
    return s.reverse()


def gene_comand(name):
    s = Seq()
    s.read_fasta(FOLDER + name + EXT)
    return str(s)


# Configure the server
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")


while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        req_raw = cs.recv(2000)
        req = req_raw.decode()

        #Process the command
        lines = req.split("\n")
        line0 = lines[0].strip()

        #Separate the line into command an argument
        lcomands = line0.split(' ')

        #First element is the command
        comand = lcomands[0]

        #Get the first argument
        try:
            arg = lcomands[1]
        except IndexError:
            arg = ""

        response = ""

        if comand == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif comand == "GET":
            termcolor.cprint("GET", 'green')
            response = get_comand(int(arg))
        elif comand == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_comand(arg)
        elif comand == "COMP":
            termcolor.cprint("COMP", 'green')
            response = comp_comand(arg)
        elif comand == "REV":
            termcolor.cprint("REV", 'green')
            response = rev_comand(arg)
        elif comand == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_comand(arg)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        response += '\n'
        print(response)
        cs.send(response.encode())
        cs.close()