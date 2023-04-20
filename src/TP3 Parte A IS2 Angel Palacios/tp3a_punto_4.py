#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class CreatorFactura(ABC):

    @abstractmethod
    def crearFactura(self,monto):
        pass
    
    
    def some_operation(self, monto) -> Factura:
        result = self.crearFactura(monto)
        return result
    


class FacturaIVAResponsable(CreatorFactura):

    def crearFactura(self,monto) -> Factura:
        factura = Factura(monto*1.4, "IVA Responsable")
        return factura

class FacturaIVANoInscripto(CreatorFactura):

    def crearFactura(self,monto) -> Factura:
        factura = Factura(monto*1.3, "IVA No Inscripto")
        return factura

class FacturaIVAExento(CreatorFactura):

    def crearFactura(self,monto) -> Factura:
        factura = Factura(monto, "IVA Exento")
        return factura


class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def imprimir_factura(self):
        print("Factura:")
        print(f"Importe: ${self.importe}")
        print(f"Condición impositiva: {self.condicion_impositiva}")

def client_code(creator: CreatorFactura) -> None:

    #print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          #f"{creator.CalcularImpuestos(345)}", end="")
    #print(f"La factura:")
    factura = creator.some_operation(345)
    factura.imprimir_factura()


if __name__ == "__main__":

    print("\n\n")
    print("App: ")
    client_code(FacturaIVAResponsable())
    print()
    client_code(FacturaIVANoInscripto())
    print()
    client_code(FacturaIVAExento())
    print()
    print("\n")