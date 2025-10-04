# prtm.py — Calculating Protein Mass (Rosalind)

# Monoisotopic mass table (Rosalind standard)
MONO = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276,  "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841,  "W": 186.07931, "Y": 163.06333,
}

def protein_monoisotopic_mass(seq: str) -> float:
    """Calculate total monoisotopic mass of a protein sequence."""
    seq = seq.strip().upper()
    return sum(MONO[a] for a in seq)

def main():
    # Change this filename if needed
    input_file = "rosalind_prtm.txt"
    
    with open(input_file, "r") as f:
        seq = f.read().strip()
    
    mass = protein_monoisotopic_mass(seq)
    print(f"Protein sequence: {seq}")
    print(f"Monoisotopic mass: {mass:.3f}")

if __name__ == "__main__":
    main()

