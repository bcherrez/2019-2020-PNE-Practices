from pathlib import Path


class Seq:

    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):

        # si es una secuencia nula:
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return

        # comprueba si es string metido por el user es válido
        if not self.valid_str(strbases):
            self.strbases = self.ERROR
            print("INVALID Seq!")
            return

     #GUARDA EL STRING EN EL OBJETO
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    @staticmethod
    def ping():
        print("PING OK")

    @staticmethod
    def valid_str(strbases): #comprueba si la base es válida
        valid_bases = ['A', 'C', 'T', 'G']

        for b in strbases:
            if b not in valid_bases:
                return False
        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)

    def read_fasta(self, filename):
        # lee el archivo
        contents = Path(filename).read_text()
        body = contents.split('\n')[1:]

        # guarda la secuencia del archivo
        self.strbases = "".join(body)
        return self

    def count_base(self, base):

        return self.strbases.count(base)

    def count(self): #numero de veces que se repite una base
        res = {'A': self.count_base('A'), 'T': self.count_base('T'),
               'C': self.count_base('C'), 'G': self.count_base('G')}
        return res

    def reverse(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return self.strbases
        else:
            return self.strbases[::-1]  # lo pone del revés

    def complement(self): #devuelve bases complementarias
        if self.strbases in [self.NULL, self.ERROR]:  # si es una sequencia inválida o nula imprime error
            return self.strbases

        basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'} #diccionario de las bases complementarias

        res = ""

        for b in self.strbases:
            res += basec[b]

        return res