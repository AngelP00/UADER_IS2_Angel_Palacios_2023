from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):

        self._parent = parent


    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def operation(self) -> str:

        pass


class Leaf(Component):

    def operation(self) -> str:
        return "Leaf node"


class Composite(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []


    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


class Configuracion():

    #def __init__(self, component) -> None:
        #self._children: List[Component] = []


    def crear(self, productoPrincipal:Composite, nRamas:int, piezasPorRamas:int) -> None:
        print('nRamas:',nRamas,', piezasPorRamas:',piezasPorRamas)
        for num in range(0, nRamas):
            print('sub-conjuto',num+1,':')
            sub_conjunto = Composite()
            for num in range(0, piezasPorRamas):
                print('pieza:',num+1)
                sub_conjunto.add(Leaf())
            
            productoPrincipal.add(sub_conjunto)
        
        return productoPrincipal



if __name__ == "__main__":

    productoPrincipal = Composite()

    configuracion = Configuracion()
    productoPrincipal = configuracion.crear(productoPrincipal=productoPrincipal,nRamas=3,piezasPorRamas=4)

    print("Client: productoPrincipal:")
    client_code(productoPrincipal)
    print("\n")


    
    
    print("Client: al productoPrincipal se le agrega el sub-conjunto opcional:")
    productoPrincipal = configuracion.crear(productoPrincipal=productoPrincipal,nRamas=1,piezasPorRamas=4)
    client_code(productoPrincipal)
    print("\n")

    #productoPrincipal.add(sub_conjunto_Opcional)
    #print("Client: Client: productoPrincipal y el subconjunto opcional:")
    #client_code2(productoPrincipal, sub_conjunto_Opcional)

    #print("\n")
    #print("\n")