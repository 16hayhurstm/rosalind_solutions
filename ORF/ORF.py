def read_fasta_string(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]

    return ''.join(line for line in lines if not line.startswith('>'))

s = read_fasta_string('ORF/data.txt')
rs = s[::-1].translate(str.maketrans('ACGT', 'TGCA'))

def codon_gen(seq, frame_start):
    return [seq[i:i+3] for i in range(frame_start, len(seq)-2, 3)]

def find_orfs(seq):
    start_codon = 'ATG'
    stop_codons = ['TAA','TAG','TGA']
    orfs = set()
    for frame in range(3):
        codons = codon_gen(seq,frame)
        n_codons = len(codons)
        i = 0
        while i < n_codons:
            codon = codons[i]
            if codon == start_codon:
                for j in range(i+1,n_codons):
                    next_codon = codons[j]
                    if next_codon in stop_codons:
                        orf = ''.join(codons[i:j+1])
                        orfs.add(orf)
                        break
            i += 1
    return orfs
        
def translate_orfs(orfs):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L',  'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA': '',  'TAG': '',
        'TGC':'C',  'TGT':'C',  'TGA': '',  'TGG':'W',
    }
    proteins = set()
    for orf in orfs:
        protein = ''
        for i in range(0,len(orf),3):
            codon = orf[i:i+3]
            amino_acid = codon_table.get(codon,'')
            protein += amino_acid
        proteins.add(protein)
    return proteins

def main():
    orfs_fwd = find_orfs(s)
    orfs_rev = find_orfs(rs)
    all_orfs = orfs_fwd.union(orfs_rev)
    proteins = translate_orfs(all_orfs)
    for protein in proteins:
        print(protein)

if __name__ == '__main__':
    main()



