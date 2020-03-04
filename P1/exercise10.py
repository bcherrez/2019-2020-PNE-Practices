from Seq1 import *

PRACTICE = 1
EXERCISE = 10

FOLDER = "../Session4/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

for gene in GENES:
    s = Seq().read_fasta(FOLDER + gene + EXT) #crea una nueva secuencia de un archivo
    d = s.count() #diccionario con los valores
    list_d = list(d.values()) #una lista con el diccionario de valores
    m = max(list_d)#calula el max valor


    print(f"Gene {gene}: Most frequent Base: {BASES[list_d.index(m)]}")

