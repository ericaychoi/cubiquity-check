import numpy as np
from checkmod import *

n = int(input("Enter dimension:\n"))
basis = makeBList(n)
wu = makeWu(basis)
print(basis)
print("wu: ")
print(wu)
