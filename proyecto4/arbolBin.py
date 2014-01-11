from nodo import baseN

class arbolBin:
    def __init__(self, info, padre):
        self.raiz = baseN(None, '')
        
    def procesar(self, archivo):
        entrada = open('casoPrueba.txt', 'r')
        for i in entrada:
            print(i[0], i[1], 'hola!')
            
    
    def GET(self, clave):
    
    
    
    def ADD(self, nodo, clave):
        act = clave[0]
        if (act != 'A') or (act != 'T'):
            nodo.cant += 1
            return
        
        clave = clave[1:]
        if act == 'A':
            if nodo.izq == None:
                nodo.izq == baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                nodo.der == baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.der, clave)
        
        
        
         
            
        
                
    
    
    
    
    

h = arbolBin(None, None)