#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#nombre del programa: factorial de los numeros entre dos extremos [1, b] sin limite inferior
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
print(sys.argv)
lim_inf = 1
lim_sup = 60

a= lim_inf
b= lim_sup
if len(sys.argv) == 1:
   b= int(input("Ingrese el limite superior(menor a 60): "))
else:
    b=int(sys.argv[1])

if(b>lim_sup):
       b= lim_sup

print(sys.argv)
#num=int(sys.argv[1])
print('a=',a,", b=",b)

for num in range(a, b+1):
    print("Factorial ",num,"! es ", factorial(num))
