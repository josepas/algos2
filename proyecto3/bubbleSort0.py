#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento BubbleSort0
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

import time
from random import *

def BubbleSort0(A):
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

A = [randint(0,15) for i in range(5000)]
start_time = time.time()
BubbleSort0(A)
print(time.time() - start_time)
    
