class Seq:
     """A classs for representing sequence objects"""
     def __init__(self,strbases):
         self.strbases = strbases
         print("New sequence created")
     def __str__(self):
         return self.strbases

     def len(self):
         return len(self.strbases)

class Gene(Seq):
    pass

#.. Main program
s1 = Seq("AACGTC")
g=Gene("ACCTGA")
s2 = Seq("CCGTCGA")
print(f"Sequence 1: {s1}") #print str and value object
print(f"Sequence 2: {g}")
print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {s2.len()}")