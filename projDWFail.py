#This takes in a nested list of bases that failed DW obstruction and outputs a list of projections

import ast
import numpy as np
from checkmod import *

n = 6
basis = input()
bList = ast.literal_eval(basis)
projs = []
elses = []
for b in bList:
    m = np.array(b)
    if(proj(m,n)):
        projs.append(m)
    else:
        elses.append(m)

print(str(len(projs)) + " out of " + str(len(bList)))
for p in projs:
    print("---------------")
    print(p)
