from Seq1 import Seq

PRACTICE = 1
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"  Bases: {s.count()}")  #dicionario de numero de bases
