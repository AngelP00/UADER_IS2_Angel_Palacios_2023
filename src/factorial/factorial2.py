#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#nombre del programa: factorial de los numeros entre dos extremos [a, b] sin limite inferior y/o superior
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
if len(sys.argv) < 3:
   nums= input("Ingrese dos numeros(separados por un espacio): ")
   nums = nums.split(" ")
   a=int(nums[0])
   b=int(nums[1])
else:
    #num=int(sys.argv[1])
    a=int(sys.argv[1])
    b=int(sys.argv[2])

print(sys.argv)
#num=int(sys.argv[1])
print('a=',a,", b=",b)

for num in range(a, b+1):
    print("Factorial ",num,"! es ", factorial(num))
