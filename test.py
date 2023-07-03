import numpy as np
from checkmod import *
from orthoAlgo import *

basis = smallBList(3)
#rmBasis = remove_negatives(basis)
bases = orthogonal_bases(basis, 3)
for b in bases:
    arr = np.array(b)
    print("---------------")
    print(arr)
print(len(bases))
