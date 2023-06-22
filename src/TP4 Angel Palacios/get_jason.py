"""
Es propiedad de la compañía:
(“copyright IS2 © 2022,2023 todos los derechos reservados).
Fecha de creación: jue. 20/6(jun.)/2023
"""
from __future__ import annotations
import json
import sys
from abc import ABC, abstractmethod
from typing import Any, Optional

from collections.abc import Iterable, Iterator
from typing import Any, List


class SingletonMeta(type):
    """
    SingletonMeta.

    Es una clase para controlar que la clase ClassGetKeySingletonRefactorizado
    tenga una unica instancia
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ClassGetKeyOriginal():
    """
    ClassGetKeyOriginal

    Es una clase que contiene el codigo original sin la refactorizacion
    """
    def get_key(self,jsonfile, jsonkey):
        """
        getKey

        El codigo original sin la refactorizacion
        """

        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]


        try:
            with open(jsonfile, 'r', encoding="utf-8") as (myfile):
                data = myfile.read()
        except FileNotFoundError:
            print("No se encontro el archivo .json en la ruta indicada")
            sys.exit(3)

        obj = json.loads(data)
        try:
            print(str(obj[jsonkey]))
        except KeyError:
            #print(e)
            print("token no encontrado")

class ClassGetKeySingletonRefactorizado(metaclass=SingletonMeta):
    """
    ClassGetKeySingletonRefactorizado

    Es una clase que contiene el codigo original refactorizacion
    """

    def get_key(self,jsonfile, jsonkey):
        """
        getKey

        El codigo original con la refactorizacion
        """
        try:
            with open(jsonfile, 'r', encoding="utf-8") as (myfile):
                data = myfile.read()
        except FileNotFoundError:
            return "No se encontro el archivo .json en la ruta indicada"

        obj = json.loads(data)
        try:
            return str(obj[jsonkey])
        except KeyError:
            return "token no encontrado"



class AbstractClassGetKey(ABC):
    """
    ClassGetKeySingletonRefactorizado

    Es una clase abstacta para utilizar la estrategia “Branching by abstraction”.
    """
    @abstractmethod
    def get_key(self,jsonfile, jsonkey):
        """
        getKey

        Es un metodo abtracto
        """

class ClaseGetKeyNoRefacorizacionYSinSingleton(AbstractClassGetKey):
    """
    ClaseGetKeyNoRefacorizacionYSinSingleton

    Es una clase concreta que va a ser utilizda en la estrategia “Branching by abstraction”.
    """

    def get_key(self,jsonfile, jsonkey) :
        get_key = ClassGetKeyOriginal()
        return get_key.get_key(jsonfile, jsonkey)

class ClaseGetKeyConRefacorizacionYConSingleton(AbstractClassGetKey):
    """
    ClaseGetKeyConRefacorizacionYConSingleton

    Es una clase concreta que va a ser utilizda en la estrategia “Branching by abstraction”.
    """

    def get_key(self,jsonfile, jsonkey) :
        get_key1 = ClassGetKeySingletonRefactorizado()
        get_key2 = ClassGetKeySingletonRefactorizado()

        if id(get_key1) == id(get_key2):
            print("ClassGetKeySingleton funciona, las variables contienen las mismas instancias.")
            #print("\n")
        else:
            print("ClassGetKeySingleton fallo, las variables contienen diferentes instancias.")
        return get_key1.get_key(jsonfile, jsonkey)



class PedidoDePago:
    """
    PedidoDePago guarda el monto que se debe pagar

    """
    def __init__(self,numero_de_pedido, monto, pagado=False, info_pago_exitoso=""):
        self._numero_de_pedido = numero_de_pedido
        self._monto = monto
        self._pagado = pagado
        self._info_pago_exitoso = info_pago_exitoso

    def get_monto(self):
        return self._monto
    
    def get_numero_de_pedido(self):
        return self._numero_de_pedido

    def get_pagado(self):
        return self._pagado
    
    def set_pagado(self, estado):
        self._pagado = estado

    def set_info_del_pago_exitoso(self, _info_pago_exitoso):
        self._info_pago_exitoso = _info_pago_exitoso
    
    def get_info_del_pago_exitoso(self):
        return self._info_pago_exitoso

    def __str__(self):
        if(self._pagado == True):
            return f"Pedido de Pago: {self._info_pago_exitoso}"
        else:
            return f"Pedido de Pago: El Pedido de Pago: {self._numero_de_pedido}, con monto de ${self._monto} no fue pagado."


#===================== Cuentas ================================
class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""
class Cuenta(AbstractHandler):
    """
    Cuenta guarda el saldo

    """
    def __init__(self, saldo, key):
        self._saldo = saldo
        self._key = key

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo
        return self._saldo
    
    def agregar_saldo(self, cantidad):
        self._saldo += cantidad

    def quitar_saldo(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Saldo insuficiente. No se puede quitar más saldo.")
    
    def handle(self, request: PedidoDePago) -> str:
        '''
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)
        '''

        if request.get_monto() <= self._saldo:
            '''
            para lo cual se indicará el número de pedido, el token a
            utilizar y el monto del pago realizado como salida de la clase.
            '''
            self.quitar_saldo(request.get_monto())
            return f"Pago exitoso, Numero de pedido: '{request.get_numero_de_pedido()}', Token a utilizado '{self._key}', Monto: ${request.get_monto()}"
        else:
            return super().handle(request)



#===================== Fin Cuentas ================================

#===================== Iterator ================================
"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    """
    `_position` attribute stores the current traversal position. An iterator may
    have a lot of other fields for storing iteration state, especially when it
    is supposed to work with a particular kind of collection.
    """
    _position: int = None

    """
    This attribute indicates the traversal direction.
    """
    _reverse: bool = False

    def __init__(self, collection: PedidosDePagosCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class PedidosDePagosCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)


    def add_item(self, item: Any):
        self._collection.append(item)



#===================== Fin Iterator ================================

if __name__ == "__main__":
    if sys.argv[1] == "-h":
        print("Help:")
        print(
        '''
    Extractor de token para acceso API Servicios Banco XXX (version 1.0)

    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.

    El programa operara como un microservicio invocado mediante:

            {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

    ej.
            ./getJason.pyc ./sitedata.json

    El token podra recuperarse mediante el standard output de ejecucion en el formato

        {1.0}XXXX-XXXX-XXXX-XXXX

    Para obtener un mensaje de ayuda detallado ejecutar

        ./getJason.pyc -h
        ''')
        sys.exit(2)

    if len(sys.argv) != 3:
        print("Debe ingresar dos argumentos:")
        print("1) El archivo .json y 2) El nombre del toquen o -h para obtener ayuda")
        sys.exit(1)

    jsonfile_external = sys.argv[1]
    jsonkey_external = sys.argv[2]

    s1 = ClaseGetKeyNoRefacorizacionYSinSingleton()
    s2 = ClaseGetKeyConRefacorizacionYConSingleton()

    ObjGetKey = s2
    print(ObjGetKey.get_key(jsonfile_external,jsonkey_external))

    '''
    c. Partiendo del objeto singleton que dado un nombre de token (banco) da
    la clave integrarlo en un nuevo componente que ante una solicitud de
    pago seleccione automáticamente la cuenta desde la que se hará el
    mismo. La información de relación entre banco (token) y clave está en
    sitedata.json
    '''


    cuenta1 = Cuenta(1000,"C598-ECF9-F0F7-881A")
    cuenta2 = Cuenta(2000,"C598-ECF9-F0F7-881B")

    cuenta1.set_next(cuenta2)

    print("Chain: cuenta1 > cuenta2\n")

    pedidos_de_pagos = []
    pedidos_de_pagos = PedidosDePagosCollection()
    pedidos_de_pagos.add_item(PedidoDePago(1,500))
    pedidos_de_pagos.add_item(PedidoDePago(2,500))
    pedidos_de_pagos.add_item(PedidoDePago(3,500))
    pedidos_de_pagos.add_item(PedidoDePago(4,500))
    pedidos_de_pagos.add_item(PedidoDePago(5,500))
    pedidos_de_pagos.add_item(PedidoDePago(6,500))
    pedidos_de_pagos.add_item(PedidoDePago(7,500))

    #print("\n")
    #result = cuenta1.handle(pedidoDePago1)

    

    for pedidoDePago in pedidos_de_pagos:
        print(f"\nClient: Que cuenta tiene va consumir el pedido de pago con monto de ${pedidoDePago.get_monto()}?")
        result = cuenta1.handle(pedidoDePago)
        if result:
            print(f"  {result}", end="")
            #pedidoDePago = PedidoDePago(1,1)
            pedidoDePago.set_pagado(True)
            pedidoDePago.set_info_del_pago_exitoso(result)
            print()
        else:
            pedidoDePago.set_pagado(False)
            print(f"  El pedido {pedidoDePago.get_numero_de_pedido()} con monto ${pedidoDePago.get_monto()} no se pudo realizar. No hay cuenta con suficiente saldo.", end="")
            print()


    print("Pedidos de pagos:")

    #collection = PedidosDePagosCollection()
    '''
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    '''

    print("Straight traversal:")
    print("\n".join(str(item) for item in pedidos_de_pagos), end="")
    print("")
    
    print("Reverse traversal:")
    print("\n".join(str(item) for item in pedidos_de_pagos.get_reverse_iterator()), end="")
    print("\n")
