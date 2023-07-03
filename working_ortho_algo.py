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
    n = len(vector)
    ortho = [i for i in set if np.dot(i, vector) == 0]
    return ortho

basis = []
bases = []
def orthogonal_bases(vector_set, dim):
    global bases
    global basis
    for vector in vector_set:
        basis.append(vector)
        if len(basis) != dim:
            working_list = list_ortho(vector, vector_set[vector_set.index(vector):])
            if len(working_list) + len(basis) < dim:
                basis.remove(vector)
                orthogonal_bases(working_list, dim)
                basis.remove(vector)
            else:
                orthogonal_bases(working_list, dim)
                basis.remove(vector)
        else:
            bases.append(basis.copy())
            basis.remove(vector)
