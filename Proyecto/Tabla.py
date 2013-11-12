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


    def Lectura(self):
    # {Pre: True}		

        entrada = open('entrada', 'r')
        for i in entrada:
            a = i.strip().split()
            self.dicc[int(a[0])] = int(a[1])
            self.dim += 1
        print(self.dicc) # Aqui chequeo que el diccionario se haya cargado bien
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


    def Puntos_KEstacionarios(self, *t): # Hasta ahora esto esta cableado feo
    # {Pre: True}  
        nuevaTabla = Tabla()
        for i in self.dicc:
            v = self.dicc[i]
            final = True
            for j in t:
                if(v in j.dicc):
                    v = j.dicc[v]
                else:
                    final = False
                    break
            if(i == v and final):
                 nuevaTabla.dicc[i] = i

        nuevaTabla.Escritura()
     # {Post: }


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

    
    
t = Tabla()
t.Lectura()
t.Escritura()
t.Puntos_Potencia(4)
#t.Puntos_Fijos()
#t.Puntos_Moviles()


