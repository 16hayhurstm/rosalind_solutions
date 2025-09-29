from scipy.stats import binom

# parameters
k = 6        # generation
N = 15        # threshold
n = 2**k     # number of individuals in generation k
p = 0.25     # probability any one is AaBb

# Compute P(X >= N)

prob = binom.sf(N-1, n, p)

print(f"P(X >= {N}) = {prob:.3f}")
