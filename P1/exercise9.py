from Seq1 import Seq

PRACTICE = 1
EXERCISE = 9

FOLDER = "../Session4/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
s = Seq()

# lee la secuencia de un archivo
# abre un archivo ADN in formato FASTA y devuelve la secuencia como un str ( caracteres A,T,G,C

s.read_fasta(FOLDER + GENES[0] + EXT) #genes empiezan en el indice 0

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Reverse:   {s.reverse()}")
print(f"  Complement:  {s.complement()}")
