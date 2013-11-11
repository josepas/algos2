# Jose Pascarella	11-10743
# Amin Arria		11-10053	
# Proyecto01 
 
class Tabla:

	def __init__(self):
	# {Pre: True}	
		self.dicc = {}
		self.dim = 0
	# {Post: self.tam = 0}

	def Lectura(self, xfilexx):
	# {Pre: True}		

		entrada = open('entrada', 'r')

		for i in entrada:
			a = i.strip().split()
			self.dicc[a[0]] = a[1]
			self.dim += 1
	# {Post: self.tam = 0}
	
	def Escritura(self):
	# {Pre: True}
		for i in self.dicc:
			print(i, '|', self.dicc[i])
		
	# {Post: }



	def Busqueda(self, clave):
	# {Pre: True}		
		return clave in self.dicc
	# {Post: self.tam = 0}


	def Puntos_Fijos(self):
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			if (i == self.dicc[i]):
				nuevaTabla[i] = self.dicc[i]
		nuevaTabla.Escritura()

	# {Post: self.tam = 0}


	def Puntos_Moviles(self):
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			if (i != self.dicc[i]):
				nuevaTabla[i] = self.dicc[i]
		nuevaTabla.Escritura()

	# {Post: self.tam = 0}
	

	def Puntos_KEstacionarios(self, f, g): # Hasta ahora esto esta cableado feo
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			if (self.dicc[i] in f.dicc) and (f.dicc[self.dicc[i]] in g.dicc): 	
				nuevaTabla[i] = i
		nuevaTabla.Escritura()
	# {Post: }


	def Puntos_Potencia(self):
	# {Pre: True}	
		nuevaTabla = Tabla()
		for i in self.dicc:
			cota = 0		
			act = i
			while cota <= self.dim and self.Busqueda(act):
				act = self.dicc[act]			
				if act == i:
					nuevaTabla[i] = i
					break
				cota += 1

		nuevaTabla.Escritura()
	# {Post: }

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

t1 = Tabla()    
t1.Lectura()




