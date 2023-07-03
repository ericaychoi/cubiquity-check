#ndDetWuCheck.py prompts the user for n (dimension) and basis vectors (each component separated by a space) and outputs det, normdet, wu element, and the result of det and we obstructions

import numpy as np
from checkmod import *

n = int(input("Enter dimension:\n"))
basis = makeBasis(n)

m = []
for i in range(1, n+1):
    m.append(basis[i])
M = np.array(m)

print("------------------------------------------")
for i in range(0, n):
    print(str(m[i])+'\n')
print("obstructing by det...")
detObsMessage(m,n)
print("obstructing by wu...")
wu = makeWu(m)
print("wu: " + str(wu))
wuObsMessage(wu)
