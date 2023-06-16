

import numpy as np
import matplotlib.pyplot as plt
print("La lista aleatoria es")
test=np.random.choice((0,1,2,3,4,5,6,7,8,9,10),(30))
data=test
   

def random(longitud, enteroshasta):
    random=np.random.choice(np.arange(enteroshasta+1),longitud)
    return random

def indicesminimos(data):
    
    indicesminimos=[]
    minimo=np.min(data)
    for i in range(len(data)):
        if (data[i]==minimo):{indicesminimos.append(i)}
    return indicesminimos        
            
def indicesmaximos(data):
    maximo=np.max(data)
    indicesmaximos=[]    
    for i in range(len(data)):
        if (data[i]==maximo):{indicesmaximos.append(i)}
    return indicesmaximos


def plotminmax(array):
    minimos=np.zeros(len(array))
    maximos=np.zeros(len(array))
    for i in range(len(array)):
        if (array[i]<max(array)):
            maximos[i]=5
        else:
            maximos[i]=array[i]

    for i in range(len(array)):
        if (array[i]>min(array)):
            minimos[i]=5
        else:
            minimos[i]=array[i]
    plt.plot(range(len(minimos)),minimos)
    plt.plot(range(len(maximos)),maximos,)
    plt.text(2,0,"En naranja los maximos, en azul los minimos")
    plt.show()



   
if __name__=="__main__":
    print(test)
    print("los indices de los minimos de la funcion son") 
    print(indicesminimos(test))
    print("los indices de los maximos de la funcion son")
    print(indicesmaximos(test))
    plotminmax(test)