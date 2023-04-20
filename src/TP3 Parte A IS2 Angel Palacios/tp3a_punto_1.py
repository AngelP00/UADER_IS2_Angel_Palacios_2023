class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FactorialCalculator(metaclass=SingletonMeta):
    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser mayor o igual a cero.")
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

if __name__ == "__main__":
    # The client code.

    fact1 = FactorialCalculator()
    fact2 = FactorialCalculator()
    if id(fact1) == id(fact2):
        print("Singleton works, both variables contain the same instance.")
    
    num = 5
    print('fact de',num,'es =',fact1.calculate_factorial(num))