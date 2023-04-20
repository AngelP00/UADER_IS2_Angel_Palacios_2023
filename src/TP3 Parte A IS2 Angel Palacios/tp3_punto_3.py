#!/usr/python
#*--------------------------------------------------
#* builder.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def entregar_en_mostrador(self) -> None:
        pass

    @abstractmethod
    def retirar_por_el_cliente(self) -> None:
        pass

    @abstractmethod
    def enviar_por_delivery(self) -> None:
        pass


class Hamburguesa1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def entregar_en_mostrador(self) -> None:
        self._product.add("entregada en mostrador")

    def retirar_por_el_cliente(self) -> None:
        self._product.add("retirada por el cliente")

    def enviar_por_delivery(self) -> None:
        self._product.add("enviada por delivery.")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Parts: {', '.join(self.parts)}", end="")



if __name__ == "__main__":
    builder = Hamburguesa1()

    # Remember, the Builder pattern can be used without a Director class.
    print('Hamburguesa1:')
    print("Recorrido: ")
    builder.entregar_en_mostrador()
    builder.product.list_parts()

    print("\n")
    print('Hamburguesa2:')
    builder = Hamburguesa1()
    print("Recorrido: ")
    builder.retirar_por_el_cliente()
    builder.product.list_parts()

    print("\n")
    print('Hamburguesa3:')
    builder = Hamburguesa1()
    print("Recorrido: ")
    builder.enviar_por_delivery()
    builder.product.list_parts()