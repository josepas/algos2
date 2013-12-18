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

def comp(x,y):
    return x-y

def merge(seq, cmpf, default=-1):
    if(default == -1):
        A = merge(seq,cmpf,1)
        for i in range(len(A)):
            seq[i] = A[i]
    else:
        A = seq
        if(len(A) == 1):
            return A
        m = len(A) // 2
        izq = merge(A[:m], cmpf, 1)
        der = merge(A[m:], cmpf, 1)
        i, j = 0, 0
        final = []
        while(i < len(izq) and j < len(der)):
            if(cmpf(izq[i], der[j]) <= 0):
                final.append(izq[i])
                i += 1
            else:
                final.append(der[j])
                j += 1
        if(i < len(izq)):
            final += izq[i:]
        if(j < len(der)):
            final += der[j:]
        A = final
        return A

a = [x for x in range(20)]
shuffle(a)
print(a)
merge(a, comp)
print(a)
    
