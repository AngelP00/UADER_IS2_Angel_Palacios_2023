#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component():

    def operation(self, num:float) -> tuple[float, str]:
        pass
        #return num


class ConcreteComponent(Component):
    #def __init__(self, num: float) -> None:
        #self._num = num
    
    def operation(self, num:float) -> tuple[float, str]:
        return num,'num_base='+ str(num)


class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:

        return self._component

    def operation(self, num:float) -> tuple[float, str]:
        #return self._component.operation()
        pass


class ConcreteDecoratorSumar2(Decorator):

    def operation(self, num:float)-> tuple[float, str]:
        #return f"ConcreteDecoratorSumar2({self.component.operation(num+2)})"
        num, text = self.component.operation(num)
        resultado = num+2
        print('ConcreteDecoratorSumar2: {}+2 = {}'.format(num, resultado))
        text = f"ConcreteDecoratorSumar2({text})"
        return resultado, text


class ConcreteDecoratorMultiplicarPor2(Decorator):

    def operation(self, num:float) -> tuple[float, str]:
        num, text = self.component.operation(num)
        resultado = num*2
        print('ConcreteDecoratorMultiplicarPor2: {}*2 = {}'.format(num, resultado))
        text = f"ConcreteDecoratorMultiplicarPor2({text})"
        return resultado, text

class ConcreteDecoratorDividirPor3(Decorator):

    def operation(self, num:float) -> tuple[float, str]:
        #return f"ConcreteDecoratorMultiplicarPor2({self.component.operation(num/3)})"
        num, text = self.component.operation(num)
        resultado = num/3
        print('ConcreteDecoratorDividirPor3: {}/3 = {}'.format(num, resultado))
        text = f"ConcreteDecoratorDividirPor3({text})"
        return resultado, text
        


def client_code(component: Component) -> None:

    # ...
    num = 10
    print('numero:',num)
    print(f"RESULT: {component.operation(num)}", end="")

    # ...
    #pass


if __name__ == "__main__":

    simple = ConcreteComponent()
    decorator1 = ConcreteDecoratorSumar2(simple)
    decorator2 = ConcreteDecoratorMultiplicarPor2(decorator1)
    decorator3 = ConcreteDecoratorDividirPor3(decorator2)

    client_code(decorator3)

    print("\n")