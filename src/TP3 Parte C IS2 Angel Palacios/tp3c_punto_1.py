#!/usr/python
#*--------------------------------------------------
#* chain.py
#* Patron chain of command
#* excerpt from https://refactoring.guru/design-patterns
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


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

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

class NumerosPrimosHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if es_primo(request):
            return f"NumerosPrimosHandler: {request} es primo"
        else:
            return super().handle(request)

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

class NumerosParesHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if es_par(request):
            return f"NumerosParesHandler: {request} es par"
        else:
            return super().handle(request)



def client_code(handler: Handler) -> None:

    for num in range(0,101):
        print(f"\nClient: {num}?")
        result = handler.handle(num)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {num} no consumido.", end="")
    


if __name__ == "__main__":

    numerosPrimos = NumerosPrimosHandler()
    numerosPares = NumerosParesHandler()

    numerosPrimos.set_next(numerosPares)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.

    print("Chain: numerosPrimos > numerosPares\n")
    client_code(numerosPrimos)
    print("\n")