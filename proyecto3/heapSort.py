#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento HeapSort 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

# Este metodo consiste en usar una estructura de datos llamada Heap (Arbol Binario no completo)
# en el cual los elementos estan semiordenados (el padre es siempre mayor que los hijos
# construyes el heap desde el arreglo desordenano y sacas los elementos como en una cola de prioridades
# aprovechandote de 

from random import *
import time

def Heapify(A, i, n):
    # Caso Base
    # No tengo hijos
    if (2 * i + 1 > n):
        return
    # Tengo un solo hijo 
    if (2 * i + 2 > n):
        k = 2 * i + 1
    # Tengo mas de un hijo, busco el mayor
    else:
        if (A[2 * i + 1] > A[2 * i + 2]):
            k = 2 * i + 1
        else:
            k = 2 * i + 2
    
    # Intercambio al padre por su hijo mayor que el
    if (A[k] > A[i]):
        A[k], A[i] = A[i], A[k]
        Heapify(A,k,n)
        
def ConstruirHeap(A,n):
    for i in range(n // 2, -1, -1):  
        Heapify(A,i,n)

def HeapSort(A,n):
    n -= 1
    ConstruirHeap(A,n)
    for i in range(n, 0, -1):
        A[0], A[i] =  A[i], A[0]
        Heapify(A, 0, i - 1)
 

