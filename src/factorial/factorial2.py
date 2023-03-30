#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#nombre del programa: factorial de los numeros entre dos extremos [a, b]
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
if len(sys.argv) < 3:# si los limites no fue ingresados se los pide
   nums= input("Ingrese dos numeros(separados por un espacio): ")
   nums = nums.split(" ")#separa el texto en dos numeros
   a=int(nums[0])#limite inferior
   b=int(nums[1])#limite superior
else:# si los limites superiores fue ingresados utiliza esos limite
    #num=int(sys.argv[1])
    a=int(sys.argv[1])
    b=int(sys.argv[2])

#print(sys.argv)
#num=int(sys.argv[1])
print('a=',a,", b=",b)

#for para calcular y mostrar el factorial de cada numero
for num in range(a, b+1):
    print("Factorial ",num,"! es ", factorial(num))