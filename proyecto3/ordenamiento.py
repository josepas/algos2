# Descripción: Módulo con la implementación de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos que son comparables
#              entre sí. Al aplicar algún algoritmo de ordenamiento, la lista a ordenar
#              es copiada y se retorna una nueva lista con los elementos ordenados.
# Autor: Guillermo Palma
# email: gvpalma@usb.ve
# version 0.1


# Todos los algoritmos de ordenamiento tienen los siguentes parámetros
# Parámetros: seq: objeto lista de python que contiene elementos comparables
#
#             cmpf: Función que compara dos elementos de la lista.
#             Esta función es llamada repetidamente por los algoritmos de ordenamiento
#             para comparar dos elementos. La función cmpf toma como argumento
#             dos elementos de la lista, y retorna un número entero. Su prototipo es:
#             cmpf(x, y) --> int
#             El  número entero  define el orden
#             de los elementos de la siguiente manera:
#                 cmpf(x, y) < 0 : significa que el elemento x va antes del elemento y
#                 cmpf(x, y) > 0 : significa que el elemento x va después del elemento y
#                 cmpf(x, y) = 0 : significa que los elementos x, y son equivalentes

from random import randint
from sys import maxsize


# Ordenamiento por Inserción
def insertion(seq, cmpf):
    n = len(seq)
    for i in range(1, n) :
        value = seq[i]
        pos = i
        while pos > 0 and cmpf(value, seq[pos - 1]) < 0 :
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value

# Ordenamiento por Quicksort
def Particionar(A, izq, der, cmpf):
    # Seleccion aleatoria del pivote
    pivot = der
    valorP = A[pivot]
    # Paso el pivot a la posicion final para que no estorbe
    m = izq
    for i in range(izq, der):
        if(cmpf(A[i], valorP) <= 0):
            A[i], A[m] = A[m], A[i]
            m += 1
    # Coloco el pivote en su posicion final
    A[der], A[m] = A[m], A[der]
    return m
    
def quickSort(seq, cmpf, izq=-1, der=-1):
    A = seq
    if(der==-1 and izq==-1):
        quickSort(A, cmpf, 0, len(A)-1)
    if (izq < der):
        pivot = Particionar(A, izq, der, cmpf)
        quickSort(A, cmpf, izq , pivot - 1)
        quickSort(A, cmpf, pivot + 1, der)
    return A

# Ordenamiento por MergeSort
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

# Ordenamiento por Heapsort
def Heapify(A, i, n, cmpf):
    if (2 * i + 1 > n):
        return
    if (2 * i + 2 > n):
        k = 2 * i + 1
    else:
        if(cmpf(A[2*i + 1], A[2*i + 2]) > 0):
            k = 2 * i + 1
        else:
            k = 2 * i + 2
    
    if(cmpf(A[k],A[i]) > 0):
        A[k], A[i] = A[i], A[k]
        Heapify(A,k,n,cmpf)
        
def ConstruirHeap(A,n,cmpf):
    for i in range(n // 2, -1, -1):  
        Heapify(A,i,n,cmpf)
    
def heapSort(seq, cmpf):
    A = seq
    n = len(A)-1
    ConstruirHeap(A,n,cmpf)
    for i in range(n, 0, -1):
        A[0], A[i] =  A[i], A[0]
        Heapify(A, 0, i - 1, cmpf)
    return A

# Ordenamiento por Bubblesort0
def bubbleSort0(seq, cmpf):
    A = seq
    n = len(A)
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if(cmpf(A[i],A[i+1]) > 0):
                A[i], A[i+1] = A[i+1], A[i]
                cambio = True
    return A

# Ordenamiento por Bubblesort1
def bubbleSort1(seq, cmpf):
    A = seq
    n = len(A)
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if (cmpf(A[i],A[i+1]) > 0): 
                A[i], A[i+1] = A[i+1], A[i]
                cambio = True
        n -= 1
    return A


    
    
