import Estacionamiento
from Vehiculo import Vehiculo

p = Estacionamiento.Estacionamiento()
v1 = Vehiculo("A11", 10, "cadillac", 91, "rojo")
v2 = Vehiculo("A22", 10, "cadillac", 92, "rojo")
v3 = Vehiculo("A33", 10, "cadillac", 93, "rojo")
v4 = Vehiculo("A44", 10, "cadillac", 94, "rojo")

t1 = p.Estacionar(v1)
t2 = p.Estacionar(v2)
t3 = p.Estacionar(v3)
t4 = p.Estacionar(v4)


print(t1, "  ", t2, "  ", t3, "  ", t4)

print (p.Existe("A11", t1))

p.Retirar("A11", t1)

print (p.Existe("A11", t1))


