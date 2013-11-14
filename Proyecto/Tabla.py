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
        entrada.close()
        assert self.dim > 0, "self.dim <= 0"
    # {Post: self.dim > 0}


    def Escritura(self, funcion):
    # {Pre: True}
        with open("salida.txt", "a") as archivo:
            archivo.write(funcion + '\n')
            for i in self.dicc:
                archivo.write(i + '\t' + self.dicc[i] + '\n')
            archivo.write('\n')
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
        nuevaTabla.Escritura("Puntos Fijos:")

    # {Post: (%forall i | self.dicc[i] == i : nuevaTabla.dicc[i] = i) }


    def Puntos_Moviles(self):
    # {Pre: True}	
        nuevaTabla = Tabla()
        for i in self.dicc:
            if (i != self.dicc[i]):
                nuevaTabla.dicc[i] = self.dicc[i]
        nuevaTabla.Escritura("Puntos Moviles:")

    # {Post: (%forall i | self.dicc[i] != i : nuevaTabla.dicc[i] = self.dicc[i] )}

    def Puntos_Potencia(self, n):
        # {Pre: n > 0 }
        assert n > 0, "n > 0"
        nuevaTabla = Tabla()
        for i in self.dicc:
            cota = 0		
            act = i
            while cota < n and self.dicc.get(act) != None:
                act = self.dicc.get(act)	
                cota += 1
            if act == i:
                nuevaTabla.dicc[i] = i
        
        nuevaTabla.Escritura("Puntos Potencia:")
    # {Post: }

class Multi_Tablas():
    def Tope_k_Reflexivo(v, *t):
        # {Pre: len(t) > 0 }
        assert len(t) > 0, "len(t) > 0"
        act = v
        n = 0
        cota = 0
        for i in t:
            if(cota < len(i.dicc)):
                cota = len(i.dicc)
        while (n < cota) and (act != None):
            for i in t:
                act = i.dicc.get(act)
            n += 1
            if (v == act):
                return print('El valor', v, 'es reflexivo con valor', n)
        return print('El valor', v, 'no es reflexivo') 
        # {Post: }

    def Puntos_k_Estacionarios(*t):
        # {Pre: len(t) > 0 }
        assert len(t) > 0, "len(t) > 0"  
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
        nuevaTabla.Escritura("Puntos K Estacionarios:")
        # {Post: }            
    
