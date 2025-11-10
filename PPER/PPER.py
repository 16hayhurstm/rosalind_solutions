n = 95
k = 8

import math
from math import comb

x =comb(n, k) * math.factorial(k)
ans = x%1000000
print(ans)

