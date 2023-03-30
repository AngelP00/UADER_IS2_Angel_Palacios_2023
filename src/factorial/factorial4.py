#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#nombre del programa: factorial de los numeros entre dos extremos [1, b] sin limite superior
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
   a= int(input("Ingrese el limite inferior(mayor o igual a 1): "))
else:
    a=int(sys.argv[1])

if(a<lim_inf):
       a= lim_inf

print(sys.argv)
#num=int(sys.argv[1])
print('a=',a,", b=",b)

#for para calcular y mostrar el factorial de cada numero
for num in range(a, b+1):
    print("Factorial ",num,"! es ", factorial(num))
