#This takes a nested list of orthogonal bases and outputs (with log messages) the results of DW obstruction

import ast
import numpy as np
from checkmod import *

n = 6
basis = input()
bList = ast.literal_eval(basis)
mList = []
for b in bList:
    mList.append(np.array(b))

for m in mList:
    print("------------------------------------------")
    print(m)
    print("obstructing by det...")
    detObsMessage(m,n)
    print("obstructing by wu...")
    wu = makeWu(m)
    print("wu: " + str(wu))
    wuObsMessage(wu)
