#*--------------------------------------------------
#* bridge.py
#* excerpt from https://refactoring.guru/design-patterns/bridge/python/example
#*--------------------------------------------------

from __future__ import annotations
from abc import ABC, abstractmethod


class LaminaGenerica:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def crearLamina(self) -> str:
        return (f"LaminaGenerica: Base crearLamina with con 0.5'' de espesor, 1,5 mts de ancho y:\n"
                f"{self.implementation.operation_implementation()}")

'''
class ExtendedLaminaGenerica(LaminaGenerica):

    def crearLamina(self) -> str:
        return (f"ExtendedLaminaGenerica: Extended crearLamina with:\n"
                f"{self.implementation.operation_implementation()}")
'''


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass



class Tren5mts(Implementation):
    def operation_implementation(self) -> str:
        #return "Tren5mts: Here's the result on the platform A."
        return "Tren5mts: genera la plancha con 5 mts de largo"


class Tren10mts(Implementation):
    def operation_implementation(self) -> str:
        #return "Tren10mts: Here's the result on the platform B."
        return "Tren10mts: genera la plancha con 10 mts de largo"



def client_code(laminaGenerica: LaminaGenerica) -> None:

    # ...

    print(laminaGenerica.crearLamina(), end="")

    # ...


if __name__ == "__main__":

    implementation = Tren5mts()
    laminaGenerica = LaminaGenerica(implementation)
    client_code(laminaGenerica)

    print("\n")

    implementation = Tren10mts()
    #LaminaGenerica = ExtendedLaminaGenerica(implementation)
    laminaGenerica = LaminaGenerica(implementation)
    client_code(laminaGenerica)

    print("\n")
