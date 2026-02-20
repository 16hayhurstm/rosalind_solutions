from Bio import SeqIO
from Bio.Seq import Seq


records = list(SeqIO.parse("SSEQ/rosalind_sseq.txt", "fasta"))

s = str(records[0].seq)
t = str(records[1].seq)

indices = []
j = 0

for i, ch in enumerate(s):
    if j < len(t) and ch == t[j]:
        indices.append(i+1)  
        j +=1
        if j == len(t):
            break

print(' '.join(map(str, indices)))

