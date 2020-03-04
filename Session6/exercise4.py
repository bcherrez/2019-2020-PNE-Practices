import termcolor


class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        bases = ['A', 'C', 'G', 'T']
        for b in strbases:
            if b not in bases:
                print("ERROR!")
                self.strbases = "ERROR"
                return

        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seqs, color):
    for seq in seqs:
        termcolor.cprint(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}", color)


def generate_seqs(pattern, number):
    #crea una lista de secuencias en el que se repite de 1 al número, lista con secuencias
    seqs = []

    for i in range(1, number + 1):
        seqs.append(Seq(pattern * i))

    return seqs
ping

# -- Main program

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1", 'blue')
print_seqs(seq_list1, "blue")


termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')
