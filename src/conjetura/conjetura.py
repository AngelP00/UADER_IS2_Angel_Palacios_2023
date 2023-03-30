import matplotlib.pyplot as plt
import numpy as np



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
    #print('i',i)
    return i

lista = []

a=int(input("Ingrese un numero >= 1: "))
b=int(input("Ingrese un numero <= 10000: "))

#a=1
#b=25
for num in range(a, b+1):
    lista.append([num,iteraciones(num)])
    print('num:',num,',i:',lista[-1])


# X axis parameter:
#xaxis = np.array([2, 10])
#xaxis = np.array([15, 30])

# Y axis parameter:
#yaxis = np.array([20, 100])

#print(np.array)

for i in range(0,len(lista)-1):
    
    x=[lista[i][0],lista[i+1][0]]
    y=[lista[i][1],lista[i+1][1]]
    
    #x=[lista[i][1],lista[i+1][1]]   # 3, 
    #y=[lista[i][0],lista[i+1][0]]   # 8,

    plt.plot(x, y,color = 'm')
    #plt.legend(loc=1)
    
    plt.scatter(lista[i][0],lista[i][1])
    plt.annotate((lista[i][0],lista[i][1]),             # The label for this point
                xy=(lista[i][0], lista[i][1]), # Position of the corresponding point
                xytext=(-18, 7),     # Offset text by 7 points to the right
                textcoords='offset points', # tell it to use offset points
                ha='left',         # Horizontally aligned to the left
                va='center')       # Vertical alignment is centered


#plt.plot([20, 30], [40, 50])
#plt.plot([30, 60], [50, 70])

#plt.plot(3, 4)

plt.show()

