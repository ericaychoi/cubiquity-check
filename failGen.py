#Takes nested list of orthogonal bases and outputs a nested list of bases that are unobstructed by DW

import ast
import numpy as np
from checkmod import *

n = 6
basis = input()
bList = ast.literal_eval(basis)
mList = []
failList = []

for b in bList:
    mList.append(np.array(b))

for m in mList:
    wu = makeWu(m)
    if(detObs(m,n) and wuObs(wu)):
        failList.append(np.ndarray.tolist(m))

print(failList)
