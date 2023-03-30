import matplotlib.pyplot as plt
import numpy as np


#funcion para calcular el numero total de iteraciones que fueron necesarias para entrar al bucle 4 2 1
def iteraciones(num): 
    i=0
    while(num!=1):
        #print('num=',num)
        i+=1
        if((num%2)==0): #par / 2
            num = num/2
        else:#impar (n*3)+1
            num = (num*3)+1
    i+=1
    return i #retorna el numero total de iteraciones

lista = []

a=int(input("Ingrese un numero >= 1: "))
b=int(input("Ingrese un numero <= 10000: "))

#for para mostrar los elementos del array
for num in range(a, b+1):
    lista.append([num,iteraciones(num)])
    print('num:',num,',i:',lista[-1])


#for para crear la grafica
for i in range(0,len(lista)-1):
    xaxis=[lista[i][0],lista[i+1][0]]
    yaxis=[lista[i][1],lista[i+1][1]]
    
    plt.plot(xaxis, yaxis,color = 'm')#creacion de una recta
    #plt.legend(loc=1)
    
    plt.scatter(lista[i][0],lista[i][1])#creacion de un punto

    #creacion del texto(x,y)
    plt.annotate((lista[i][0],lista[i][1]),             # The label for this point
                xy=(lista[i][0], lista[i][1]), # Position of the corresponding point
                xytext=(-18, 7),     # Offset text by 7 points to the right
                textcoords='offset points', # tell it to use offset points
                ha='left',         # Horizontally aligned to the left
                va='center')       # Vertical alignment is centered


plt.show()

