from nodo import baseN

class arbolBin:
    def __init__(self, info, padre):
        self.raiz = baseN(None, '')
        
    def procesar(self, archivo):
        entrada = open('casoPrueba.txt', 'r')
        for i in entrada:
            print(i[0], i[1], 'hola!')
            
    
    def GET(self, nodo, clave):
        act = clave[0]
        clave = clave[1:]
        if (nodo == None) or ((act != 'A') and (act != 'T')):
            return (nodo.cadena + clave, 0)
        
        if act == 'A':
            if nodo.izq == None:
                return (nodo.cadena + clave, 0)
            self.GET(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                return (nodo.cadena + clave, 0)
            self.GET(nodo.der, clave)
        
    
    
    def ADD(self, nodo, clave):
        act = clave[0]
        clave = clave[1:]
        if (act != 'A') and (act != 'T'):
            nodo.cant += 1
            return
        
        if act == 'A':
            if nodo.izq == None:
                nodo.izq == baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.izq, clave)
        
        if act == 'T':
            if nodo.der == None:
                nodo.der == baseN(nodo, nodo.cadena + act)
            self.ADD(nodo.der, clave)
        
        
        
         
            
        
                
    
    
    
    
    

h = arbolBin(None, None)