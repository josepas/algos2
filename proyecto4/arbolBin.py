from nodo import baseN

class arbolBin:
    def __init__(self):
        self.raiz = baseN()
        
    def procesar(self, archivo):
        entrada = open('casoPrueba.txt', 'r')
        for i in entrada:
            print(i[0], i[1], 'hola!')
            
            
    def GET(self, nodo, clave):
        if (nodo == None):
            print(0)
            return
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
    
    
    #def PODAR(self, nodo):
        #if nodo.cant > 0 or nodo.izq != None or nodo.der != None:
            #return
        #print('borre un nodo')
        #aux = nodo.padre
        #del(nodo)
        #nodo = None
        #self.PODAR(aux)
    
    
    #Aqui la estoy cagando con podar
    def DELETE(self, nodo, clave):
        if (nodo == None):
            return
        if (clave == ''):
            nodo.cant = 0
        if clave != '':
            act = clave[0]
        clave = clave[1:]

        if act == 'A':
            self.DELETE(nodo.izq, clave)
            if nodo.der != None or nodo.cant > 0:
                print(clave)
                nodo.izq = None
                return
        if act == 'T':
            self.DELETE(nodo.der, clave)
            if nodo.izq != None or nodo.cant > 0:  
                nodo.der = None
                print(clave)
                return
    
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
        
        
         
h = arbolBin()
h.ADD(h.raiz, 'A')
h.ADD(h.raiz, 'T')
h.ADD(h.raiz, 'T')
h.ADD(h.raiz, 'T')
h.ADD(h.raiz, 'AA')
h.ADD(h.raiz, 'AA')
h.ADD(h.raiz, 'AT')
h.ADD(h.raiz, 'AT')
h.ADD(h.raiz, 'AT')
h.ADD(h.raiz, 'AT')
h.ADD(h.raiz, 'AT')
h.ADD(h.raiz, 'TA')
h.ADD(h.raiz, 'TA')
h.ADD(h.raiz, 'TA')
h.ADD(h.raiz, 'TA')
h.ADD(h.raiz, 'TT')
h.ADD(h.raiz, 'TT')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'ATA')
h.ADD(h.raiz, 'TTA')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTAT')
h.ADD(h.raiz, 'TTATTATATATTTTA')
h.ADD(h.raiz, 'TTATTATATATTTTA')
h.ADD(h.raiz, 'TTATTATATATTTTA')
h.ADD(h.raiz, 'TTATTATATATTTTA')
h.GETALL(h.raiz, '')
h.DELETE(h.raiz, 'TTATTATATATTTTA')
h.GETALL(h.raiz, '')


print(h.MAXLENGTH(h.raiz))









