from Bio import SeqIO
from Bio.Seq import Seq


records = list(SeqIO.parse("SPLC/rosalind_splc.txt", "fasta"))


dna = records[0].seq  
introns = [r.seq for r in records[1:]]

# Remove introns
spliced = str(dna)
for intron in introns:
    spliced = spliced.replace(str(intron), "")

# Transcribe + translate
rna = Seq(spliced).transcribe()                 
protein = rna.translate(to_stop=True)           

print(str(protein))