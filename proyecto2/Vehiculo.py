class Vehiculo:
    i = 0
    def __init__(self, l, p, m, a, c): 
        self.iden = Vehiculo.i
        self.longitud = l 
        self.placa = p
        self.modelo = m 
        self.anyo = a
        self.color = c
        Vehiculo.i += 1
        
        
        