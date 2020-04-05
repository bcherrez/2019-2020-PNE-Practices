class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # inicia la secuencia con el valor.
        # pasa como un argumento al crear el objeto
        bases = ['A', 'C', 'G', 'T']

        # comprobar  que las secuencias dadas sean correctas
        for b in strbases:
            if b not in bases:
                print("ERROR!")
                self.strbases = "ERROR"
                return

        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        #Method called when the object is being printed#
        return self.strbases

    def len(self):
        return len(self.strbases)


# -- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
