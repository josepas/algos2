# Proyecto 2
#
# Clase Vehiculo
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013


class Vehiculo:
    i = 0
    def __init__(self, p, l, m, a, c): 
        self.iden = Vehiculo.i
        self.longitud = float(l) 
        self.placa = p
        self.modelo = m 
        self.anyo = int(a)
        self.color = c
        Vehiculo.i += 1
        
    def __str__(self):
        outStr = '--> ... ' + self.placa + ' ' + str(self.longitud) + '\t' + self.modelo + '\t' + str(self.anyo) + '\t' + self.color + '\n' 
        return outStr
        
        
