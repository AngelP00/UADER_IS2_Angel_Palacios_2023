#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#nombre del programa: factorial de un numero
def factorial(num): 
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

'''
if len(sys.argv) == 0:
   print("Debe informar un nÃºmero!")
   sys.exit()
'''
if len(sys.argv) == 1:
   num=int(input("Ingrese un numero: "))
else:
    num=int(sys.argv[1])

#num=int(sys.argv[1])

print("Factorial ",num,"! es ", factorial(num))