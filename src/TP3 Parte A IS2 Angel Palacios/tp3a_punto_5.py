import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------


class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getCar(self):
      car = Car()
      
      # Primero el chasis
      body = self.__builder.getBody()
      car.setBody(body)
      
      # Luego el motor
      engine = self.__builder.getEngine()
      car.setEngine(engine)
      
      # Finalmente (4) ruedas
      i = 0
      while i < 4:
        wheel = self.__builder.getWheel()
        car.attachWheel(wheel)
        i += 1

      # Retorna el vehiculo completo
      return car
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Luego el motor
      trenDeAterrisaje = self.__builder.getTrenDeAterrisaje()
      avion.setTrenDeAterrisaje(trenDeAterrisaje)
      
      # Finalmente (2) turbinas y las (2) alas
      i = 0
      while i < 2:
        turbina = self.__builder.getTurbina()
        avion.attachTurbina(turbina)

        ala = self.__builder.getAla()
        avion.attachAla(ala)
        i += 1

      # Retorna el vehiculo completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Car:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("planta motora: %d" % (self.__engine.horsepower))
      print ("ruedas: %d\'" % (self.__wheels[0].size))

#*-----------------------------------------------------------------
#* CarBuilder
#* Clase genérica que solo define la interfaz de los métodos que el
#* CarBuilder específico tiene que implementar
#*-----------------------------------------------------------------
class CarBuilder:
	
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class JeepBuilder(CarBuilder):
   
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 22
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 400
      return engine
   
   def getBody(self):
      body = CarBody()
      body.shape = "SUV"
      return body

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Wheel:
   size = None

class Engine:
   horsepower = None

class CarBody:
   shape = None

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__turbinas = list()
      self.__alas = list()
      self.__trenDeAterrisaje = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachTurbina(self, turbina):
      self.__turbinas.append(turbina)
   
   def attachAla(self, ala):
      self.__alas.append(ala)

   def setTrenDeAterrisaje(self, trenDeAterrisaje):
      self.__trenDeAterrisaje = trenDeAterrisaje

   def specification(self):
      print ("body material: %s" % (self.__body.material))
      print ("turbinas: (",len(self.__turbinas),") unidades de",self.__turbinas[0].size,"mts de diametro")
      print ("alas: (",len(self.__alas),") unidades de",self.__alas[0].size,"mts de largo")
      print ("tren de aterrisaje material: ",self.__trenDeAterrisaje.material)

#*-----------------------------------------------------------------
#* AvionBuilder
#* Clase genérica que solo define la interfaz de los métodos que el
#* AvionBuilder específico tiene que implementar
#*-----------------------------------------------------------------

class AvionBuilder:
	
      def getTurbina(self): pass
      def getAla(self): pass
      def getTrenDeAterrisaje(self): pass
      def getBody(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Boing747
#* Establece instancias para tomar turbinas, alas, tren de aterrisaje y body
#* estableciendo las partes específicas que (en un Boing747) 
#* deben tener esas partes
#*-------------------------------------------------------

class Boing747Builder(AvionBuilder):
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.size = 5
      return turbina
   
   def getAla(self):
      ala = Ala()
      ala.size = 15
      return ala
   
   def getTrenDeAterrisaje(self):
      trenDeAterrisaje = TrenDeAterrisaje()
      trenDeAterrisaje.material = "aluminio reforzado"
      return trenDeAterrisaje
   
   def getBody(self):
      body = AvionBody()
      body.material = "acero"
      return body

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------
class Turbina:
   size = None

class Ala:
   size = None

class TrenDeAterrisaje:
   material = None

class AvionBody:
   material = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():
#*----------------------------------------------------------------
#* Car
#*----------------------------------------------------------------
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo")
#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   jeepBuilder = JeepBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(jeepBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   jeep = director.getCar()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   jeep.specification()
   print ("\n\n")


#*----------------------------------------------------------------
#* Avion
#*----------------------------------------------------------------
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion")
#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   boing747Builder = Boing747Builder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(boing747Builder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   jeep = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   jeep.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   main()