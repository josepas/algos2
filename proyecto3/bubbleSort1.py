#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento BubbleSort1
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

import time
from random import *

def BubbleSort1(A):
    n = len(A)
    co = 0
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if (A[i] > A[i+1]): 
                A[i], A[i+1] = A[i+1], A[i]
                cambio = True
                co += 1
        n -= 1

A = [randint(0,10) for i in range(10)]
start_time = time.time()
BubbleSort1(A)
print(A)
print(time.time() - start_time)
