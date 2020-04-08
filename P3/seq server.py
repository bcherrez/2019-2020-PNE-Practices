
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
    s_length = s.len()
    count_a = s.count_a('A')
    pa = "{:.1f}".format(100 * count_a / s_length)
    count_c = s.count_c('C')
    pc = "{:.1f}".format(100 * count_c / s_length)
    count_g = s.count_g('G')
    pg = "{:.1f}".format(100 * count_g / s_length)
    count_t = s.count_t('T')
    pt = "{:.1f}".format(100 * count_t / s_length)

    response = f"""Sequence: {s}
Total length: {s_length}
A: {count_a} ({pa}%)
C: {count_c} ({pc}%)
G: {count_g} ({pg}%)
T: {count_t} ({pt}%)"""
    return response


def comp_comand(strseq):
    s = Seq(strseq)
    return s.complement()


def rev_comand(strseq):
    s = Seq(strseq)
    return s.reverse()


def gene_comand(name):
    s= Seq()
    s.read_fasta(FOLDER + name + EXT)
    return str(s)


# Configure the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((IP, PORT))

sock.listen()

print("SEQ Server configured!")


while True:
    print("Waiting for clients....")
    try:
        (client_socket, client_ip_port) = sock.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        sock.close()
        exit()
    else:

        req_raw = client_socket.recv(2000)
        req = req_raw.decode()

        #Process the command
        lines = req.split("\n")
        line0 = lines[0].strip()

        #Separate the line into command an argument
        line_comands = line0.split(' ')

        #First element is the command
        comand = line_comands[0]

        #Get the first argument
        try:
            argument = line_comands[1]
        except IndexError:
            argument = ""

        response = ""

        if comand == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif comand == "GET":
            termcolor.cprint("GET", 'green')
            response = get_comand(int(argument))
        elif comand == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_comand(argument)
        elif comand == "COMP":
            termcolor.cprint("COMP", 'green')
            response = comp_comand(argument)
        elif comand == "REV":
            termcolor.cprint("REV", 'green')
            response = rev_comand(argument)
        elif comand == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_comand(argument)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        response += '\n'
        print(response)
        client_socket.send(response.encode())
        client_socket.close()