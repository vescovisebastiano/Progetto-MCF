import sys, os
import numpy as np
import matplotlib.pyplot as plt


sys.path.append('/home/sebastiano/MCF/progetto')

import spett

#prova della distribuzione di fend e pixel

pixel=spett.set1
fend=spett.set1
a=spett.optimize(pixel, fend, spett.mass)


plt.plot(a[0],a[1], "o")
plt.xlabel('pixel')
plt.ylabel('fenditura')
plt.title("0.5mm-6.0mm sens 0.5mm, test su 1000 masse")

plt.show()


masstest=np.random.randint(low=1, high=211, size=10000)
mass=np.arange(1, 211, 1)
eff=np.empty(0)

for i in range(0, a[0].size):
    b=spett.eff(a[0][i], a[1][i], masstest)
    print("prestazioni con pixel=", a[0][i], "e fenditura=", a[1][i])
    plt.plot(mass, b)
    plt.xlabel('A')
    plt.ylabel('efficienza')
    plt.show()
    eff=np.append(eff, np.sum(b)/b.size)

besteff=np.argmax(eff)

bestp=a[0][besteff]
bestf=a[1][besteff]

print ("i valori ottimizzati per pixel e fenditura sono: ", bestp, bestf)
        



        



