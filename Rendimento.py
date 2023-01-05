import sys, os
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from tqdm import tqdm


sys.path.append('/home/sebastiano/MCF/progetto')

import spettrometro

print(spettrometro.p, spettrometro.f) #parametri trovati con l'altro programma
        
mass=np.random.randint(low=1, high=211, size=10000)
num=np.zeros(shape=210)
eff1=np.zeros(shape=210)

for i in range(0, mass.size):
        a=spettrometro.spett(spettrometro.p[0], spettrometro.f[0], mass[i])
        num[mass[i]-1]+=1
        if a==mass[i]:
                eff1[a-1]+=1

eff=eff1/num
mass=np.arange(1, 211, 1)

plt.plot(mass, eff, "o")

plt.xlabel('A')
plt.ylabel('efficienza')
plt.show()
plt.hist(eff, weights=mass, bins=420)
plt.show()
print (eff, np.sum(eff)/eff.size)


        



