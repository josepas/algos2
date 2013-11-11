# Jose Pascarella	11-10743
# Amin Arria		11-10053	
# Proyecto01 
 
class Tabla:
		
	def __init__(self):
	# {Pre: True}	
		self.dicc = {}
		self.dim = 0
	# {Post: self.dim = 0}


	def Lectura(self):
	# {Pre: True}		

		entrada = open('entrada', 'r')
		for i in entrada:
			a = i.strip().split()
			self.dicc[int(a[0])] = int(a[1])
			self.dim += 1
		print(self.dicc) # Aqui chequeo que el diccionario se haya cargado bien
	# {Post: self.dim > 0 /\ #self.dicc = dim}

	
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
	

	def Puntos_KEstacionarios(self, f, g): # Hasta ahora esto esta cableado feo
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			if (self.dicc[i] in f.dicc) and (f.dicc[self.dicc[i]] in g.dicc): 	
				nuevaTabla.dicc[i] = i
		nuevaTabla.Escritura()
	# {Post: }


	def Puntos_Potencia(self): # Esta parece estar funcionando bien
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			cota = 0		
			act = i
			while cota <= self.dim and self.Busqueda(act):
				act = self.dicc[act]		
				if act == i:
					nuevaTabla.dicc[i] = i
					break
				cota += 1

		nuevaTabla.Escritura()
	# {Post: }

t = Tabla()
t.Lectura()
t.Escritura()
t.Puntos_Potencia()
t.Puntos_Fijos()
t.Puntos_Moviles()
'''
	def Puntos_K_reflexivo(self, v, f, g): #esta esta mal hecha
	# {Pre: True}
		total = 0
		for i in self.dicc:
			total += 1			
			if (v == i):			
				for j in f.dicc:
					total += 1
					if self.dicc[i] == j:
						for k in g.dicc:
							total += 1
							if f.dicc[j] = k and i = g.dicc[k]:
								return total
		
	# {Post: }
'''






