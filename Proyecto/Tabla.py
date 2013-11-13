# Jose Pascarella	11-10743
# Amin Arria		11-10053	
# Proyecto01 
 
class Tabla:
    
	######################################################################
	#                                                                    #
	# Inicializacion del Diccionario para la tabla con atributo para la  #
	# dimension                                                          #
	#                                                                    #
	######################################################################
    def __init__(self):
    # {Pre: True}	
    
        self.dicc = {}
        self.dim = 0
        assert self.dim == 0, "self.dim != 1"
    # {Post: self.dim = 0}


    def Lectura(self, archivo):
    # {Pre: True}		

        entrada = open(archivo, 'r')
        for i in entrada:
            a = i.strip().split()
            self.dicc[str(a[0])] = str(a[1])
            self.dim += 1
        print(self.dicc) # Aqui chequeo que el diccionario se haya cargado bien
        entrada.close()
        assert self.dim > 0, "self.dim != 1"
    # {Post: self.dim > 0}


    def Escritura(self):
    # {Pre: True}
        for i in self.dicc:
            print(i, '|', self.dicc[i])
        print()
    # {Post: True}


    def Busqueda(self, clave): 
    # {Pre: True}		
        return (clave in self.dicc)
    # {Post: Busqueda == %exists | 0 <= i < self.dim : self.dicc[clave] }


    def Puntos_Fijos(self):
    # {Pre: True}	
        nuevaTabla = Tabla()
        for i in self.dicc:
            if (i == self.dicc[i]):
                nuevaTabla.dicc[i] = self.dicc[i]
        nuevaTabla.Escritura()

    # {Post: }


    def Puntos_Moviles(self):
    # {Pre: True}	
        nuevaTabla = Tabla()
        for i in self.dicc:
            if (i != self.dicc[i]):
                nuevaTabla.dicc[i] = self.dicc[i]
        nuevaTabla.Escritura()

    # {Post: self.tam = 0}

    def Puntos_Potencia(self, n): # Esta parece estar funcionando bien
    # {Pre: True}	
        nuevaTabla = Tabla()
        for i in self.dicc:
            cota = 0		
            act = i
            while cota < n and self.dicc.get(act) != None:
                act = self.dicc.get(act)	
                cota += 1
            if act == i:
                nuevaTabla.dicc[i] = i
        
        nuevaTabla.Escritura()
    # {Post: }

def Tope_k_Reflexivo(v, *t):
    act = v
    n = 0
    cota = 0
    for i in t:
        cota += len(i.dicc)
    while (n < cota) and (act != None):
        for i in t:
            act = i.dicc.get(act)
        n += 1
        if (v == act):
            return print('El valor', v, 'es reflexivo con valor', n)
    return print('El valor', v, 'no es reflexivo') 

def Puntos_k_Estacionarios(*t):
    # {Pre: True}  
    nuevaTabla = Tabla()
    for i in t[0].dicc:
        v = t[0].dicc[i]
        final = True
        for j in t[1:]:
            if(v in j.dicc):
                v = j.dicc[v]
            else:
                final = False
                break
        if(i == v and final):
                nuevaTabla.dicc[i] = i

        nuevaTabla.Escritura()
        # {Post: }            
    
    
    
    
    
    
    
    
