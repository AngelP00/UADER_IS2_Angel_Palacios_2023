

import os
from typing import List
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	_saves: List[Memento] = []

	def save(self, writer):
		#self.obj = writer.save()
		if(len(self._saves)>=4):
			self._saves.pop(0)
		self._saves.append(writer.save())
	
	def undo(self, writer, pos):
		#[3,2,1,0]
		if(pos < len(self._saves) and pos >=0):
			writer.undo(self._saves[-1-pos])
		else:
			print('save no encontrado')


if __name__ == '__main__':
	#os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	
	print("Se graba algo en el objeto y se salva.")
	writer.write("primer renglon\n")
	caretaker.save(writer)
	print("Se graba algo en el objeto y se salva.")
	writer.write("segundo renglon\n")
	caretaker.save(writer)
	print("Se graba algo en el objeto y se salva.")
	writer.write("tercer renglon\n")
	caretaker.save(writer)
	print("Se graba algo en el objeto y se salva.")
	writer.write("cuarto renglon\n")
	caretaker.save(writer)
	#print("Se graba algo en el objeto y se salva.")
	#writer.write("quinto renglon\n")
	#caretaker.save(writer)
	
	#print()
	#print("Se graba información adicional:")
	#writer.write("Material adicional de la clase de patrones\n")
	#print(writer.content + "\n\n")

	print("se invoca al <undo>")
	caretaker.undo(writer,pos=1)

	print("Se muestra el estado actual:")
	print(writer.content + "\n\n")