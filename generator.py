#Generates a nested list of all orthogonal bases of n dimension

import numpy as np
from checkmod import *
from orthoAlgo import *
from lemma2VectorGeneration import *

n = 7
basis = simpleList(n)
nestedList = orthogonal_bases(basis,n)
mList = []
for b in nestedList:
    m = np.column_stack((b[0], b[1], b[2], b[3], b[4], b[5], b[6]))
    if(np.linalg.matrix_rank(m) == n):
        mList.append(m)
output = []
for m in mList:
    output.append(np.ndarray.tolist(m))

print(output)
