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
        self.longitud = l 
        self.placa = p
        self.modelo = m 
        self.anyo = a
        self.color = c
        Vehiculo.i += 1
        
        
        