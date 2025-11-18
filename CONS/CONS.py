from Bio import SeqIO
import numpy as np
from collections import Counter

def fasta_to_matrix_biopython(fasta_path):
    seqs = [list(str(rec.seq).upper()) for rec in SeqIO.parse(fasta_path, "fasta")]
    max_len = max(len(s) for s in seqs)
    seqs = [s + ["-"]*(max_len - len(s)) for s in seqs]
    return np.array(seqs)

matrix = fasta_to_matrix_biopython("CONS/test.txt")

consensus = []
profile = {b: [] for b in "ACGT"}

for i in range(matrix.shape[1]):
    col = matrix[:, i]
    counts = Counter(col)

    # Add profile counts in A,C,G,T order
    for b in "ACGT":
        profile[b].append(counts[b])

    # Consensus base
    most_common = counts.most_common(1)[0][0]
    consensus.append(most_common)

# ----- OUTPUT ROSALIND FORMAT -----

# Consensus string
print("".join(consensus))

# Profile matrix
print("A:", *profile["A"])
print("C:", *profile["C"])
print("G:", *profile["G"])
print("T:", *profile["T"])
