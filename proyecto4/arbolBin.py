from nodo import baseN
import sys


class arbolBin:
    def __init__(self):
        self.raiz = baseN()
        
    def PRINT(self, string):
        with open(self.salida, 'a') as s:
            s.write(string + '\n')
  
    def GET(self, nodo, clave):
        aux = self.raiz
        for i in clave:
            if aux == None:
                return(clave + ' ' + '0')
            if(i == 'A'):
                aux = aux.izq
            if(i == 'T'):
                aux = aux.der
        return(clave + ' ' + aux.cant)
        
    def ADD(self, nodo, clave):
        if (clave == ''):
            nodo.cant += 1
            return
        
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            if nodo.izq == None:
                nodo.izq = baseN()
            self.ADD(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                nodo.der = baseN()
            self.ADD(nodo.der, clave)
        

    def GETALL(self, nodo, camino):     
        if nodo == None:
            return
        #if nodo.cant > 0:
        print(camino, nodo.cant)
        self.PRINT(camino + str(nodo.cant))
        self.GETALL(nodo.izq, camino + 'A')
        self.GETALL(nodo.der, camino + 'T')
        
    def MAXLENGTH(self, nodo, maximo=-1):
        if nodo == None:
            return maximo
        if (nodo.cant > maximo):
            maximo = nodo.cant
        maximo = self.MAXLENGTH(nodo.izq, maximo)
        maximo = self.MAXLENGTH(nodo.der, maximo)
        return maximo
    
    def DELETE(self, nodo, clave):
        if nodo == None:
            self.PRINT('ERROR: Cannot DELETE.')
            return
        if (clave == ''):
            nodo.cant = 0
            act = ''
        
        if clave != '':
            act = clave[0]
        clave = clave[1:]

        if act == 'A':
            if self.DELETE(nodo.izq, clave):
                nodo.izq = None
        if act == 'T':
            if self.DELETE(nodo.der, clave):
                nodo.der = None
        
        if nodo.izq == None and nodo.der == None and nodo.cant == 0:
            return True
        else:
            return False
       
    
    def SET(self, nodo, clave, cantidad):
        if cantidad == 0:
            self.DELETE(nodo, clave)
        if (nodo == None):
            return
        if (clave == ''):
            nodo.cant = cantidad
            return
            
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            self.SET(nodo.izq, clave, cantidad)
        
        if act == 'T':
            self.SET(nodo.der, clave, cantidad)  
        
    def CHANGE(self, nodo, secO, secD):
        if(secD == ''):
            if(nodo.cant > 0 or nodo.izq != None or nodo.der != None):
                self.PRINT("ERROR: Cannot CHANGE. Use CHANGEMERGE instead.")
            else:
                aux = self.raiz
                for i in secO:
                    if(i == 'A'):
                        aux = aux.izq
                    if(i == 'T'):
                        aux = aux.der
                nodo.izq = aux.izq
                nodo.der = aux.der
                nodo.cant = aux.cant
                aux.izq = None
                aux.der = None
                self.DELETE(self.raiz, secO)
        elif(secD[0] == 'A'):
            if(nodo.izq == None):
                nodo.izq = baseN()
            self.CHANGE(nodo.izq, secO, secD[1:])
        elif(secD[0] == 'T'):
            if(nodo.der == None):
                nodo.der = baseN()
            self.CHANGE(nodo.der, secO, secD[1:])


    def UnionA(self, nodo1, nodo2):
        raiz = baseN()
        cant = 0
        if(nodo1 != None):
            cant += nodo1.cant
        if(nodo2 != None):
            cant += nodo2.cant
        raiz.cant = cant
        if(nodo1 == None and nodo2 == None):
            return None
        elif(nodo1 != None and nodo2 == None):
            raiz.izq = nodo1.izq
            raiz.der = nodo1.der
        elif(nodo1 == None and nodo2 != None):
            raiz.izq = nodo2.izq
            raiz.der = nodo2.der
        else:
            raiz.izq = self.UnionA(nodo1.izq, nodo2.izq)
            raiz.der = self.UnionA(nodo1.der, nodo2.der)
        return raiz

    def CHANGEMERGE(self, nodo, secO, secD):
        aux1 = nodo
        aux2 = nodo
        for i in secO:
            if(i == 'A'):
                aux1 = aux1.izq
            if(i == 'T'):
                aux1 = aux1.der
        for i in secD:
            if(i == 'A'):
                aux2 = aux2.izq
            if(i == 'T'):
                aux2 = aux2.der
        tmp = self.UnionA(aux1, aux2)
        aux2.cant = tmp.cant
        aux2.izq = tmp.izq
        aux2.der = tmp.der
        aux1.izq = None
        aux1.der = None
        self.DELETE(self.raiz, secO)
    
    def procesar(self, archivo):
        entrada = open(archivo, 'r')
        for i in entrada:
            i = i.split()
            print(i[0], 'hola!')
            if i[0] == 'ADD':
                self.ADD(self.raiz, i[1])
                
            if i[0] == 'GET':
                self.PRINT(self.GET(self.raiz, i[1]))
                
            if i[0] == 'GETALL':
                self.GETALL(self.raiz, '')
                
            if i[0] == 'SET':
                self.SET(self.raiz, i[1], i[2])
                
            if i[0] == 'CHANGE':    
                self.CHANGE(self.raiz, i[1], i[2])
                
            if i[0] == 'CHANGEMERGE':
                self.CHANGEMERGE(self.raiz, i[1], i[2])
                
            if i[0] == 'DELETE':
                self.DELETE(self.raiz, i[1])
                
            if i[0] == 'PRINT':
                self.PRINT(self.raiz, i[1])
                
            if i[0] == 'MAXLENGTH':
                self.PRINT('maxlength == ' + self.MAXLENGTH(self.raiz))
    

print(sys.argv[1], sys.argv[2])
h = arbolBin()
h.salida = sys.argv[2]
h.procesar(sys.argv[1])


