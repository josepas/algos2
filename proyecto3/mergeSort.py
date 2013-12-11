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


def merge(A):
    if(len(A) == 1):
        return A
    m = len(A) // 2
    izq = merge(A[:m])
    der = merge(A[m:])
    i, j = 0, 0
    final = []
    while(i < len(izq) and j < len(der)):
        if(izq[i] <= der[j]):
            final.append(izq[i])
            i += 1
        else:
            final.append(der[j])
            j += 1
    if(i < len(izq)):
        final += izq[i:]
    if(j < len(der)):
        final += der[j:]
    return final
    


# Casos de prueba
for i in range(5):
    A = [randint(0,x) for x in range(1000000)]

    x = time.time()
    
    A = merge(A)
   
    print(time.time() - x)
