#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self,base_imponible):
        pass

    def CalcularImpuestos(self, base_imponible) -> float:

        result = self.factory_method(base_imponible)
        return result


class ImpuestosSimplificado(Creator):

    def factory_method(self, base_imponible) -> float:
        cImp = CalculadorImpuestoIndividual(base_imponible)
        total_impuestos = 0
        total_impuestos += cImp.calcular(0.21) # iva
        total_impuestos += cImp.calcular(0.05) # iibb
        total_impuestos += cImp.calcular(0.012) # Contribuciones municipales
        return total_impuestos

class CalculadorImpuestoIndividual:
    def __init__(self, base_imponible):
        self.base_imponible = base_imponible

    def calcular(self,porcentaje):
        impuesto = porcentaje * self.base_imponible
        return impuesto




def client_code(creator: Creator) -> None:

    #print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          #f"{creator.CalcularImpuestos(345)}", end="")
    print(f"El total de impuestos es: {creator.CalcularImpuestos(345)}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("App: Creando impuestos simplificados")
    client_code(ImpuestosSimplificado())
    print("\n")