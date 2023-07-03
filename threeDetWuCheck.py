import numpy as np
from checkmod import *

#n = int(input("Enter dimension:\n"))
n = 3
comb = smallB(n)
orth = orthogonal(comb, n)
mList = orthFormat(orth)
fail = []
for m in mList:
    detb = detObs(m,3)
    wu = makeWu(m)
    wub = wuObs(wu)
    if(detb and wub):
        fail.append(m)

for m in fail:
    print("---------------------------------------------------")
    print(m[0])
    print(m[1])
    print(m[2])
    print("obstructing by det...")
    detObsMessage(m, 3)
    print("obstructing by wu...")
    wu = makeWu(m)
    print("wu: " + str(wu))
    wuObsMessage(wu)
