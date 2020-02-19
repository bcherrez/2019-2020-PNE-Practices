FOLDER="../Session--04/"
FILENAME="U5.txt"

print("The first 20 bases are:", seq_read_fasta(FOLDER + FILENAME))

#EX2
def seq_read_fasta(filename):
    file_cocntents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace("\n", "")
    seq_dna = seq_dna[:20] #until base 20
    return seq_dna

#EX3
def seq_len(filename):
    file_contents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace("\n", "")
    return len(seq_dna)
