#This takes in a nested list of bases that failed DW obstruction and outputs a list of non-projections

import ast
import numpy as np
from checkmod import *

n = 6
basis = input()
bList = ast.literal_eval(basis)
projs = []
elses = []
for b in bList:
    m = np.asarray(b)
    if(proj(m,n)):
        projs.append(m)
    else:
        elses.append(m)

print(str(len(elses)) + " out of " + str(len(bList)))
for p in elses:
    print("-----------------")
    print(p)
