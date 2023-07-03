import numpy as np
from checkmod import *

#n = int(input("Enter dimension:\n"))
n = 4
comb = smallB(n)
orth = orthogonal(comb, n)
mList = orthFormat(orth)
for m in mList:
    print("---------------------------------------------------")
    print(m[0])
    print(m[1])
    print(m[2])
    print(m[3])
    print("obstructing by det...")
    detObsMessage(m, n)
    print("obstructing by wu...")
    wu = makeWu(m)
    print("wu: " + str(wu))
    wuObsMessage(wu)
