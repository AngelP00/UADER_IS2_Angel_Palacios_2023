import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

		self.frecuenciasMemorizadas = [['m1','120.3','FM'], ['m2','121.3','AM'], ['m3','122.3','AM'],['m4','123.3','FM']]
		self.posFrecuenciasMemorizadas = 0
#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()
	
	def scanFrecuenciasMemorizadas(self):
		#self.state.scan()
		self.posFrecuenciasMemorizadas += 1
		if self.posFrecuenciasMemorizadas == len(self.frecuenciasMemorizadas):
			self.posFrecuenciasMemorizadas = 0
		
		frecuencia = self.frecuenciasMemorizadas[self.posFrecuenciasMemorizadas]
		#print(frecuencia)
		#print('if',frecuencia[2],'hola',self.state.name)
		if(frecuencia[2]!=self.state.name):
			self.toggle_amfm()
		print("Sintonizando... Frecuencia Memorizada '{}' Estación {} {}".format(frecuencia[0],frecuencia[1], self.state.name))

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scanFrecuenciasMemorizadas]*4 + [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	#print('actions:',actions)
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

