import numpy as np

n = int(input("Enter dimension:\n"))
basis = {}
for i in range(1,n+1):
    b_str = input("Enter " + str(i) + "th basis vector:\n")
    b_list = b_str.split()
    basis[i] = list(map(int, b_list))

basisv = {}
for i in range(1, n+1):
    basisv[i] = np.array(basis[i])

m = []
for i in range(1,n+1):
    m.append(basis[i])

M = np.array(m)
print("Matrix:\n" + str(M))
det = round(np.linalg.det(M),2)
print("det: " + str(det))
normdet = det/(2**n)
print("normdet: " + str(normdet))
if(normdet > 1):
    print("normdet is greater than 1; not cbqs")
else:
    print("normdet is less than or equal to 1; need further obstruction")

p_list = []
points = set()
for i in range(1, n+1):
    for j in range(0, 6):
        p_list.append(j * basisv[i])

for i in range(1, n):
    v = basisv[i]+basisv[i+1]
    for j in range(1, 6):
        p_list.append(j * v)

for i in range(1, n):
    for j in range(1,6):
        p_list.append(basisv[i] + j * basisv[i+1])
        p_list.append(j * basisv[i] + basisv[i+1])

for p in p_list:
    points.add(str(p))

print(points)


while(True):
    c_list = []
    p = input("cube?\n")
    p1 = np.fromstring(p, dtype=int, sep=' ')
    c_list.append(p1)
    c_list.append(p1+[0,1])
    c_list.append(p1+[1,0])
    c_list.append(p1+[1,1])

    corners = set()
    for c in c_list:
        corners.add(str(c))

    cubi = False
    for c in corners:
        if c in points:
            print(str(c) + "is in the lattice")
            cubi = True

    if not cubi:
        print("LATTICE NOT CUBI; obstructed by " + str(corners))
        break






    

