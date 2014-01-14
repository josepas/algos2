from nodo import baseN

class arbolBin:
    def __init__(self):
        self.raiz = baseN()
        
    def procesar(self, archivo):
        entrada = open('casoPrueba.txt', 'r')
        for i in entrada:
            print(i[0], i[1], 'hola!')
            if i[0] = 'ADD':
                self.AAD(self.raiz, i[1])
                
            if i[0] = 'GET':
                self.GET(self.raiz, i[1])
                
            if i[0] = 'GETALL':
                self.GETALL(self.raiz, '')
                
            if i[0] = 'SET':
                self.SET(self.raiz, i[1], i[2])
                
            if i[0] = 'CHANGE':    
                self.CHANGE(self.raiz, i[1], i[2])
                
            if i[0] = 'CHANGEMERGE':
                self.CHANGEMERGE(self.raiz, i[1], i[2])
                
            if i[0] = 'DELETE':
                self.DELETE(self.raiz, i[1])
                
            if i[0] = 'PRINT':
                self.PRINT(self.raiz, i[1])
                
            if i[0] = 'MAXLENGTH':
                self.MAXLENGTH(self.raiz)
            
    def GET(self, nodo, clave):
        if (clave == ''):
            print(nodo.cadena, nodo.cant)
            return
            
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            self.GET(nodo.izq, clave)
        
        if act == 'T':
            self.GET(nodo.der, clave)   
        

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
                print("ERROR")
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

            
            
            
            


h = arbolBin()

h.ADD(h.raiz, "ATA")
h.ADD(h.raiz, "ATT")
h.ADD(h.raiz, "ATT")
h.ADD(h.raiz, "T")
h.ADD(h.raiz, "TT")

h.GETALL(h.raiz, '')

print(h.MAXLENGTH(h.raiz))

print("Cambiando: AT -> TA")
h.CHANGE(h.raiz, "AT", "TA")

h.GETALL(h.raiz, '')

