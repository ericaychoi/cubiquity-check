import numpy as np
from checkmod import *
# import math


n = int(input("Enter dimension:\n"))
basis = makeBasis(n)

basisv = {}
for i in range(1, n+1):
    basisv[i] = np.array(basis[i])

m = []
for i in range(1,n+1):
    m.append(basis[i])
M = np.array(m)

detObs(M, n)

if(n == 2):
    points = twoGen(basisv, n)
    corners = twoCubes(basisv, n)
elif(n == 3):
    points = threeGen(basisv, n)
    corners = threeCubes(basisv,n)
elif(n == 4):
    points = fourGen(basisv, n)
    corners = fourCubes(basisv, n)

print(points)
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')

# print(corners)

for cube in corners:
    cubi = False
    for c in cube:
        if c in points:
            print(str(c) + " is in the lattice; moving on to next cube")
            cubi = True
            break
        if not cubi:
            print("obstructed by " + str(cube))
            exit()
if cubi:
    print("all cubes failed to obstruct; most likely cubiquitous")

