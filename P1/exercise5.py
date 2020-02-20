from Seq1 import Seq

PRACTICE = 1
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")  #secuencia,longitud y las bases
    for b in ['A', 'C', 'T', 'G']:  #va sobre las bases
        print(f"  {b}: {s.count_base(b)}", end=", ")  #la funcion count cuenta el numero de veces que se repite una base
    print()