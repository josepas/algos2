#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento MergeSort 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

from random import *
import time
import sys

def comp(x,y):
    return x-y

def mezclar(A, cmpf, izq, med, der):
    final = []
    I = A[izq:med]
    J = A[med:der]
    i, j = 0, 0
    while(i < len(I) and j < len(J)):
        if(cmpf(I[i],J[j]) <= 0):
            final.append(I[i])
            i += 1
        else:
            final.append(J[j])
            j += 1
    for k in range(i, len(I)):
        final.append(I[k])
    for k in range(j, len(J)):
        final.append(J[k])
    for k in range(der-izq):
        A[izq+k] = final[k]


def mergeSort(seq, cmpf, p=0, r=-1):
    if(r == -1):
        r = len(seq)
    if(r - p >= 2):
        med = (p + r) // 2
        mergeSort(seq, cmpf, p, med)
        mergeSort(seq, cmpf, med, r)
        mezclar(seq, cmpf, p, med, r)


a = [x for x in range(20)]
shuffle(a)
print(a)
mergeSort(a, comp)
print(a)
    
