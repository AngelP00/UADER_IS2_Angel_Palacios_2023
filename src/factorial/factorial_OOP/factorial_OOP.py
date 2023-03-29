class Factorial:
    def __init__(self):
        print('_Factorial creado_')
  
    def run(self, min, max):
        print('print min =',min,', max =',max)
        for num in range(min, max+1):
            print("Factorial ",num,"! es ", self.factorial(num))

    def factorial(self, num):
        if num < 0: 
            print("Factorial de un nÃºmero negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 
    


if __name__ == '__main__':
    print('modulo_animales in main')

    a= int(input("Ingrese el limite inferior(mayor o igual a 1): "))
    b= int(input("Ingrese el limite superior: "))

    print('a=',a,", b=",b)

    
    factorial = Factorial()
    factorial.run(a,b)
    pass