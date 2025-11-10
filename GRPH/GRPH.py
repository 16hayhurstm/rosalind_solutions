from Bio import SeqIO

fasta_file = "GRPH/rosalind_grph.txt"
records = list(SeqIO.parse(fasta_file, "fasta"))
k = 3  # overlap length

for s in records:
    s_seq = str(s.seq)
    s_suffix = s_seq[-k:]  # last k bases
    for t in records:
        t_seq = str(t.seq)
        if s.id != t.id:  # avoid self-loop
            t_prefix = t_seq[:k]  # first k bases
            if s_suffix == t_prefix:
                print(f"{s.id} {t.id}")
 