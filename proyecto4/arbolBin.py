from nodo import baseN
import sys


class arbolBin:
    def __init__(self):
        self.raiz = baseN()
        
    def PRINT(self, string):
        with open(self.salida, 'a') as s:
            s.write(string + '\n')
  
    def GET(self, clave):
        aux = self.raiz
        for i in clave:
            if(i == 'A'):
                aux = aux.izq
            if(i == 'T'):
                aux = aux.der
            if(aux == None):
                break
        if aux == None:
            return(clave + ' ' + '0')
        else:
            return(clave + ' ' + str(aux.cant))
        
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
        if nodo.cant > 0:
            self.PRINT(camino + ' ' + str(nodo.cant))
        self.GETALL(nodo.izq, camino + 'A')
        self.GETALL(nodo.der, camino + 'T')
        
    def MAXLENGTH(self, nodo):
        if (nodo == None):
            return 0

        if nodo == self.raiz:
            max1 = self.MAXLENGTH(nodo.izq)
            max2 = self.MAXLENGTH(nodo.der)
        else:
            max1 = 1 + self.MAXLENGTH(nodo.izq)
            max2 = 1 + self.MAXLENGTH(nodo.der)
        if (max1 >= max2):
            return max1
        else:
            return max2
    
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
        if (clave == ''):
            nodo.cant = cantidad
            return False
            
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            if(nodo.izq == None):
                nodo.izq = baseN()
            self.SET(nodo.izq, clave, cantidad)
        
        if act == 'T':
            if(nodo.der == None):
                nodo.der = baseN()
            self.SET(nodo.der, clave, cantidad)
    
    def CHANGE(self, secO, secD):
       #Chequeo de precondicion
       aux = self.raiz
       pre = False
       for i in secD:
           if(i == 'A'):
               aux = aux.izq
           elif(i == 'T'):
               aux = aux.der
           if(aux == None):
               pre = True
               break
       if(pre):
           nodo_O = self.raiz
           padre_D = self.raiz
           for i in secO[:-1]:
               if(i == 'A'):
                   nodo_O = nodo_O.izq
               elif(i == 'T'):
                   nodo_O = nodo_O.der
           if(secO[-1] == 'A'):
               aux = nodo_O
               nodo_O = nodo_O.izq
               aux.izq = None
           elif(secO[-1] == 'T'):
               aux = nodo_O
               nodo_O = nodo_O.der
               aux.der = None
           for i in secD[:-1]:
               if(i == 'A'):
                   if(padre_D.izq == None):
                       padre_D.izq = baseN()
                   padre_D = padre_D.izq
               elif(i == 'T'):
                   if(padre_D.der == None):
                       padre_D.der = baseN()
                   padre_D = padre_D.der
           if(secD[-1] == 'A'):
               padre_D.izq = nodo_O
           elif(secD[-1] == 'T'):
               padre_D.der = nodo_O
       else:
           self.PRINT("ERROR: Cannot CHANGE. Use CHANGEMERGE instead.")


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
        
        #Borrar nodo innecesario
        aux = self.raiz
        for i in secO[:-1]:
            if(i == 'A'):
                aux = aux.izq
            if(i == 'T'):
                aux = aux.der
        if(secO[-1] == 'A'):
            aux.izq = None
        elif(secO[-1] == 'T'):
            aux.der = None

    def procesar(self, archivo):
        entrada = open(archivo, 'r')
        for i in entrada:
            j = i.split()
            if j[0] == 'ADD':
                self.ADD(self.raiz, j[1])
                
            if j[0] == 'GET':
                self.PRINT(self.GET(j[1]))
                
            if j[0] == 'GETALL':
                self.GETALL(self.raiz, '')
                
            if j[0] == 'SET':
                self.SET(self.raiz, j[1], int(j[2]))
                
            if j[0] == 'CHANGE':    
                self.CHANGE(j[1], j[2])
                
            if j[0] == 'CHANGEMERGE':
                self.CHANGEMERGE(self.raiz, j[1], j[2])
                
            if j[0] == 'DELETE':
                self.DELETE(self.raiz, j[1])
                
            if j[0] == 'PRINT':
                i = i[6:].strip("\'\n ")
                self.PRINT(i)
                
            if j[0] == 'MAXLENGTH':
                self.PRINT('maxlength == ' + str(self.MAXLENGTH(self.raiz)))
    
h = arbolBin()
h.salida = sys.argv[2]
h.procesar(sys.argv[1])


