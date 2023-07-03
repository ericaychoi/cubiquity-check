import numpy as np
import itertools
from math import *

#takes dimension n, prompts user to enter basis, and returns basis vectors (dtype=dict of str) 
def makeBasis(n):
    basis = {}
    for i in range(1, n+1):
        b_str = input("Enter " + str(i) + "th basis vector:\n")
        b_list = b_str.split()
        basis[i] = list(map(int, b_list))
    return basis

#takes dimension n, prompts user to enter basis, and returns basis vectors (dtype=nested list of int)
def makeBList(n):
    basis = []
    for i in range(1, n+1):
        b_str = input("Enter " + str(i) + "th basis vector:\n")
        b_list = b_str.split()
        int_list = []
        for j in range(0, len(b_list)):
            int_list.append(int(b_list[j]))
        basis.append(int_list)
    return basis

#generates basis vectors (dtype=list of np arrays) with components in {-2,-1,0,1,2} and satisfies Lemma 1's inequality
def smallB(n):
    generator = []
    good = set()
    goodList = []
    for i in range(n):
        generator.append(-2)
        generator.append(-1)
        generator.append(0)
        generator.append(1)
        generator.append(2)
    for comb in itertools.permutations(generator, n):
        norm = 0
        for i in range(n):
            norm += comb[i]**2
        if(norm <= (n+3)):
            good.add(comb)
    for v in good:
        arr = np.array(v)
        goodList.append(arr)
    return goodList

#generates basis vectors (dtype=list of lists) with components in {-2,-1,0,1,2} and satisfies Lemma 1's inequality
def smallBList(n):
    generator = []
    good = set()
    goodList = []
    for i in range(n):
        generator.append(-2)
        generator.append(-1)
        generator.append(0)
        generator.append(1)
        generator.append(2)
    for comb in itertools.permutations(generator, n):
        norm = 0
        for i in range(n):
            norm += comb[i]**2
        if(norm <= (n+3)):
            good.add(comb)
    for v in good:
        arr = np.array(v)
        goodList.append(np.ndarray.tolist(arr))
    return goodList

#generates nxn matrices of orthogonal basis vectors (dtype=list of np arrays)
def orthogonal(basis, n):
    orthList = []
    mList = []
    for comb in itertools.combinations(basis, n):
        orth = True
        for pair in itertools.combinations(comb, 2):
            if not checkOrth(pair[0],pair[1]):
                orth = False
        if orth and n == 3:
            m = np.column_stack((comb[0],comb[1],comb[2]))
            if np.linalg.matrix_rank(m) == 3:
                mList.append(m)
        if orth and n == 4:
            m = np.column_stack((comb[0],comb[1],comb[2],comb[3]))
            if np.linalg.matrix_rank(m) == 4:
                mList.append(m)
    return mList

#formats vectors given by orthogonal() to (dtype=nested list)
def orthFormat(mList):
    olist = []
    for m in mList:
        ml = m.tolist()
        olist.append(ml)
    return olist

#checks if two inputted vectors are orthogonal or not (dtype=boolean)
def checkOrth(v, w):
    if(np.dot(v,w) == 0):
        return True
    else:
        return False

#takes in basis of form dict of str and outputs np matrix M
def makeM(basis, n):
    basisv = {}
    for i in range(1, n+1):
        basisv[i] = np.array(basis[i])
    m = []
    for i in range(1, n+1):
        m.append(basis[i])
    M = np.array(m)
    return M

#takes matrix M and performs determinant obstruction
def detObs(M, n):
    det = round(np.linalg.det(M),2)
    normdet = det/(2**n)
    if(normdet > 1):
        return False
    else:
        return True

#takes matrix M and performs determinant obstruction
def detObsMessage(M, n):
    det = round(np.linalg.det(M),2)
    print("det: " + str(det))
    normdet = det/(2**n)
    print("normdet: " + str(normdet))
    if(normdet > 1):
        print("not cbqs; det obstructioin successful")
        return False
    else:
        print("det obstruction fails; need further obstruction")
        return True

#takes a basis (dtype=nested list of ints) and outputs the wu element (dtype=list)
def makeWu(basis):
    wu = []
    for i in range(len(basis)):
        comp = 0
        for j in range(len(basis)):
            comp += basis[i][j]
        wu.append(comp)
    return wu

#takes the wu element and performs wu obstruction (dtype=boolean)
def wuObs(wu):
    zeros = 0
    evens = []
    odds = []
    lhs = 0
    for w in wu:
        if w == 0:
            zeros+=1
        elif(w%2 == 1):
            odds.append(w)
        else:
            evens.append(w)
    for o in odds:
        lhs += ((o**2-1)/4)
    for e in evens:
        lhs += ((e**2-4)/4)
    if(lhs > zeros):
        return False
    else:
        return True

#takes the wu element and performs wu obstruction (dtype=boolean)
def wuObsMessage(wu):
    zeros = 0
    evens = []
    odds = []
    lhs = 0
    for w in wu:
        if w == 0:
            zeros+=1
        elif(w%2 == 1):
            odds.append(w)
        else:
            evens.append(w)
    for o in odds:
        lhs += ((o**2-1)/4)
    for e in evens:
        lhs += ((e**2-4)/4)
    if(lhs > zeros):
        print("not cbqs; wu obstruction successful")
        return False
    else:
        print("wu obstruction fails; need further obstruction") 
        return True

#takes a np matrix and checks if it is a projection
def proj(m, n):
    index = 1000
    proc = False
    for c in m:
        zeros = 0
        for i in c:
            if(i == 0):
                zeros += 1
        if(zeros == n-1):
            proc = True
            for j in range(len(c)):
                if(c[j] != 0):
                    index = j
    if(proc):
        v = m[:, index]
        zeros2 = 0
        for i in v:
            if(i == 0):
                zeros2 += 1
        if(zeros2 == n-1):
            return True
        else:
            return False
    else:
        return False

#takes basis vectors (dtype=dict of str) and generates points for 2D lattice; returns a set of strings(points)
def twoGen(basisv, n):
    p_list = []
    points = set()
    for i in range(1, n):
        for j in range(-20,21):
            for k in range(-20,21):
                p_list.append(j * basisv[i] + k * basisv[i+1])
    for p in p_list:
        points.add(str(p))   
    return points

#takes basis vectors (dtype=dict of str) and generates points for 3D lattice; returns a set of strings(points)
def threeGen(basisv, n):
    p_list = []
    points = set()
    for i in range(1, n-1):
        for j in range(-30,31):
            for k in range(-30,31):
                for l in range (-30,31):
                    p_list.append(j * basisv[i] + k * basisv[i+1] + l * basisv[i+2])             
    for p in p_list:
        points.add(str(p))   
    return points

def nwCube(p):
    c = [str(p), str(p+[0,1]), str(p+[-1,0]), str(p+[-1,1])]
    return c

def neCube(p):
    c = [str(p), str(p+[0,1]), str(p+[1,0]), str(p+[1,1])]
    return c

def swCube(p):
    c = [str(p), str(p+[0,-1]), str(p+[-1,0]), str(p+[-1,-1])]
    return c

def seCube(p):
    c = [str(p), str(p+[0,-1]), str(p+[1,0]), str(p+[1,-1])]
    return c

def twoCubes(basisv, n):
    corners = []
    for i in range(1, n+1):
        p1 = basisv[i] + [1,0]
        p2 = basisv[i] + [0,1]
        p3 = basisv[i] + [-1,0]
        p4 = basisv[i] + [0,-1]
        corners.append(neCube(p1))
        corners.append(seCube(p1))
        corners.append(nwCube(p2))
        corners.append(neCube(p2))
        corners.append(nwCube(p3))
        corners.append(swCube(p3))
        corners.append(swCube(p4))
        corners.append(seCube(p4))
    return corners

def n1Cube(p):
    c = [str(p), str(p+[1,0,0]), str(p+[0,1,0]), str(p+[1,1,0]), str(p+[0,0,1]), str(p+[1,0,1]), str(p+[0,1,1]), str(p+[1,1,1])]
    return c

def n2Cube(p):
    c = [str(p), str(p+[1,0,0]), str(p+[0,1,0]), str(p+[1,1,0]), str(p+[0,0,-1]), str(p+[1,0,-1]), str(p+[0,1,-1]), str(p+[1,1,-1])]
    return c

def n3Cube(p):
    c = [str(p), str(p+[-1,0,0]), str(p+[0,1,0]), str(p+[-1,1,0]), str(p+[0,0,1]), str(p+[-1,0,1]), str(p+[0,1,1]), str(p+[-1,1,1])]
    return c

def n4Cube(p):
    c = [str(p), str(p+[-1,0,0]), str(p+[0,1,0]), str(p+[-1,1,0]), str(p+[0,0,-1]), str(p+[-1,0,-1]), str(p+[0,1,-1]), str(p+[-1,1,-1])]
    return c

def s1Cube(p):
    c = [str(p), str(p+[1,0,0]), str(p+[0,-1,0]), str(p+[1,-1,0]), str(p+[0,0,1]), str(p+[1,0,1]), str(p+[0,-1,1]), str(p+[1,-1,1])]
    return c

def s2Cube(p):
    c = [str(p), str(p+[1,0,0]), str(p+[0,-1,0]), str(p+[1,-1,0]), str(p+[0,0,-1]), str(p+[1,0,-1]), str(p+[0,-1,-1]), str(p+[1,-1,-1])]
    return c

def s3Cube(p):
    c = [str(p), str(p+[-1,0,0]), str(p+[0,-1,0]), str(p+[-1,-1,0]), str(p+[0,0,1]), str(p+[-1,0,1]), str(p+[0,-1,1]), str(p+[-1,-1,1])]
    return c

def s4Cube(p):
    c = [str(p), str(p+[-1,0,0]), str(p+[0,-1,0]), str(p+[-1,-1,0]), str(p+[0,0,-1]), str(p+[-1,0,-1]), str(p+[0,-1,-1]), str(p+[-1,-1,-1])]
    return c

def threeCubes(basisv, n):
    corners = []
    for i in range(1, n+1):
        p1 = basisv[i] + [1,1,1]
        p2 = basisv[i] + [1,1,-1]
        p3 = basisv[i] + [1,-1,1]
        p4 = basisv[i] + [1,-1,-1]
        p5 = basisv[i] + [-1,1,1]
        p6 = basisv[i] + [-1,1,-1]
        p7 = basisv[i] + [-1,-1,1]
        p8 = basisv[i] + [-1,-1,-1]
        corners.append(n1Cube(p1))
        corners.append(n2Cube(p1))
        corners.append(n3Cube(p1))
        corners.append(n4Cube(p1))
        corners.append(n1Cube(p2))
        corners.append(n2Cube(p2))
        corners.append(n3Cube(p2))
        corners.append(n4Cube(p2))
        corners.append(n1Cube(p5))
        corners.append(n2Cube(p5))
        corners.append(n3Cube(p5))
        corners.append(n4Cube(p5))
        corners.append(n1Cube(p6))
        corners.append(n2Cube(p6))
        corners.append(n3Cube(p6))
        corners.append(n4Cube(p6))
    
        corners.append(s1Cube(p3))
        corners.append(s2Cube(p3))
        corners.append(s3Cube(p3))
        corners.append(s4Cube(p3))
        corners.append(s1Cube(p4))
        corners.append(s2Cube(p4))
        corners.append(s3Cube(p4))
        corners.append(s4Cube(p4))
        corners.append(s1Cube(p7))
        corners.append(s2Cube(p7))
        corners.append(s3Cube(p7))
        corners.append(s4Cube(p7))
        corners.append(s1Cube(p8))
        corners.append(s2Cube(p8))
        corners.append(s3Cube(p8))
        corners.append(s4Cube(p8))

    return corners

