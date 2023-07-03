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

print(len(bList))
print(len(projs))
print(len(elses))
