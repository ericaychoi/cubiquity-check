# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

entries = [-2,-1, 0, 1, 2]
def remove_duplicates(a_list):
    for i in range(len(a_list)):
        a_list[i] = tuple(a_list[i])
    a_list = list(set(a_list))
    for j in range(len(a_list)):
        a_list[j] = list(a_list[j])
    return a_list
def remove_zero(set):
    if set == []:
        return set
    elif ([0]*len(set[0])) in set:
        set.remove([0]*len(set[0]))
    return set
def vector_start(ents):
    vectors = []
    for i in ents:
        v = [i]
        vectors.append(v)
    return vectors


vector_list = vector_start(entries)
def create_vectors(n):
    n -= 1
    entries = [-2, -1, 0, 1, 2]
    small_entries = [-1, 0, 1]
    global vector_list
    working_list = vector_list.copy()
    long_list = [i for i in vector_list if 2 in i] + [i for i in vector_list if -2 in i]
    short_list = [i for i in vector_list if i not in long_list]
    if n>0:
        #print(working_list)
        for num in entries:
            #print("this is my current number", num)
            for vector in short_list:
                #print("this is current vector", vector)
                v = vector + [num]
                #print(v)
                vector_list = vector_list + [v]
                #print(vector_list)
               # print("this is my vector list", vector_list)
                #print("this is the working list", working_list)
        for small_num in small_entries:
            for vector in long_list:
                #print("this is current vector", vector)
                v = vector + [small_num]
                #print
                vector_list = vector_list + [v]
        for old in working_list:
            if old in vector_list:
                vector_list.remove(old)
                continue
                #print("i removed an old vector", working_list)
            else:
                continue
        create_vectors(n)
    #else:
        #vector_list = remove_duplicates(vector_list)
    return vector_list


def remove_negatives(vectors):
    simple_list = []
    for i in vectors:
        if (i in simple_list) or ([j*(-1) for j in i] in simple_list):
            pass
        else:
            simple_list.append(i)
    return simple_list


def SimpleList(n):
    simple_list = remove_zero(remove_negatives(create_vectors(n)))
    return simple_list

