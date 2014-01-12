from nodo import baseN

class arbolBin:
    def __init__(self):
        self.raiz = baseN(None, '')
        
    def procesar(self, archivo):
        entrada = open('casoPrueba.txt', 'r')
        for i in entrada:
            print(i[0], i[1], 'hola!')
            
    
    def GET(self, nodo, clave):
        if (nodo == None):
            print(nodo.cadena + clave, 0)
            return
        if (clave == ''):
            print(nodo.cadena, nodo.cant)
            return
            
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            if nodo.izq == None:
                print(nodo.cadena + clave, 0)
                return
            self.GET(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                print(nodo.cadena + clave, 0)
                return
            self.GET(nodo.der, clave)   
        
    
    
    def ADD(self, nodo, clave):
        if (clave == ''):
            nodo.cant += 1
            return
        
        act = clave[0]
        clave = clave[1:]
        if act == 'A':
            if nodo.izq == None:
                nodo.izq = baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                nodo.der = baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.der, clave)
        

    def GETALL(self, nodo):
        if nodo == None:
            return
        if nodo.cant > 0:
            print(nodo.cadena, nodo.cant)
        self.GETALL(nodo.izq)
        self.GETALL(nodo.der)
        
        
         
h = arbolBin()
h.ADD(h.raiz, 'ATAT')
h.ADD(h.raiz, 'ATATTATAAT')
h.ADD(h.raiz, 'ATATTTTAATTTT')
h.ADD(h.raiz, 'ATATTTTTA')
h.ADD(h.raiz, 'ATATAAAAAAA')
h.ADD(h.raiz, 'ATATTATATATATATTTTAATATT')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'TTTA')
h.ADD(h.raiz, 'AAAAAAAAA')
h.ADD(h.raiz, 'AAAAAAAAA')
h.ADD(h.raiz, 'AAAAAAAAA')
h.ADD(h.raiz, 'AAAAAAAAA')
h.ADD(h.raiz, 'AAAAAAAAA')
h.ADD(h.raiz, 'AAAAAAAAA')



h.GET(h.raiz, 'ATAT')
h.GET(h.raiz, 'ATATTT')
h.GET(h.raiz, 'AT')
h.GETALL(h.raiz)








