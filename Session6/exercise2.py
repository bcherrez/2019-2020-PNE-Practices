class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        bases = ['A', 'C', 'G', 'T']

        # comprobar que el string se utiliza en la inicialización
        for b in strbases:
            if b not in bases:
                print("ERROR!!")
                self.strbases = "ERROR"
                return
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seqs):
    #Crea una lista de secuencias
    for seq in seqs:
        print(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}")


# -- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)