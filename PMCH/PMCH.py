from math import factorial

def read_fasta_string(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]

    return ''.join(line for line in lines if not line.startswith('>'))

s = read_fasta_string('PMCH/rosalind_pmch.txt')

count_A = s.count('A')
count_C = s.count('C')


result = factorial(count_A) * factorial(count_C)
print(result)
