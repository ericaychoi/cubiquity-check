import ast
import numpy as np
from checkmod import *

n = 4
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

print(str(len(elses)) + " out of " + str(len(bList)))
for p in elses:
    print("---------------")
    print(p)
