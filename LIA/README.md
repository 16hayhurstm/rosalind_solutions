# Rosalind: Independent Alleles (LIA)

## Problem
We are given two values:

- `k`: the generation number (starting from 0 = Tom, 1 = Tom's children, etc.)
- `N`: the minimum number of AaBb individuals required

Tom is `AaBb` and self-crosses in every generation.  
Each individual always mates with another `AaBb`, producing offspring with genotypes determined by Mendelian inheritance.

We want to compute:

\[
P(\text{at least N AaBb individuals in generation k})
\]