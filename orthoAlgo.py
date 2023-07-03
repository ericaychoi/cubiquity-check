import numpy as np

def remove_negatives(vectors):
    simple_list = []
    for i in vectors:
        if (i in simple_list) or ([j*(-1) for j in i] in simple_list):
            pass
        else:
            simple_list.append(i)
    return simple_list

def list_ortho(vector, set):
    #n = len(vector)
    ortho = [i for i in set if np.dot(i, vector) == 0]
    return ortho

def orthogonal_bases(vector_set, dim):
    basis = []
    bases = []
    orthogonal_recursion(vector_set, dim, basis, bases)
    return bases

def orthogonal_recursion(vector_set, dim, basis, bases):
    for vector in vector_set:
        basis.append(vector)
        if len(basis) != dim:
            working_list = list_ortho(vector, vector_set[vector_set.index(vector):])
            if len(working_list) + len(basis) < dim:
                basis.remove(vector)
            else:
                orthogonal_recursion(working_list, dim, basis, bases)
                basis.remove(vector)
        else:
            bases.append(basis.copy())
            basis.remove(vector)

import main
import checkmod

bases = orthogonal_bases(main.simple_vectors3, 5)
print(bases)
for b in bases:
    arr = np.array(b)
    print("---------------")
    print(arr)
    checkmod.detObsMessage(arr, 5)
    checkmod.wuObsMessage(checkmod.makeWu(b))




print(len(bases))






