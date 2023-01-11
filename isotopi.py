import numpy as np
import sys
import scipy 
import matplotlib.pyplot as plt
import math

sys.path.append('/home/sebastiano/MCF/progetto')

import spett
import ottimizzato

pixel=ottimizzato.bestp
fend=ottimizzato.bestf

C=np.random.randint(12, 14, 10000) #isotopo 1 (carbonio 12 e 13)
Po=np.random.randint(209, 211, 10000) #isotopo 2 (polonio 209 e 210)
Ge=np.random.randint(36, 38, 10000)*2 #isotopo 3 (germanio 72 e 74)


test=np.arange(0.001, 0.02, 0.001)
test1=np.arange(0.0005, 0.02, 0.0005)


#carbonio

y=np.empty(0)
for j in test:
    a=spett.eff1(pixel, j, C)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("carbonio, mantengo pixel costante")
plt.xlabel("fenditura")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test:
    a=spett.eff1(j, fend, C)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("carbonio, mantengo fenditura costante")
plt.xlabel("pixel")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test1:
    a=spett.eff1(j, j, C)
    y=np.append(y, a)
    
plt.plot(test1, y)
plt.plot(test1, y, 'o')
plt.title("carbonio, vario simultaneamente pixel e fenditura")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()


#polonio

y=np.empty(0)
for j in test:
    a=spett.eff1(pixel, j, Po)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("carbonio, mantengo pixel costante")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test:
    a=spett.eff1(j, fend, Po)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("carbonio, mantengo fenditura costante")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test1:
    a=spett.eff1(j, j, Po)
    y=np.append(y, a)
    
plt.plot(test1, y)
plt.plot(test1, y, 'o')
plt.title("carbonio, vario simultaneamente pixel e fenditura")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()

#germanio

y=np.empty(0)
for j in test:
    a=spett.eff1(pixel, j, Ge)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("germanio, mantengo pixel costante")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test:
    a=spett.eff1(j, fend, Ge)
    y=np.append(y, a)

plt.plot(test, y)
plt.plot(test, y, 'o')
plt.title("germanio, mantengo fenditura costante")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()

y=np.empty(0)
for j in test1:
    a=spett.eff1(j, j, Ge)
    y=np.append(y, a)
    
plt.plot(test1, y)
plt.plot(test1, y, 'o')
plt.title("germanio, vario simultaneamente pixel e fenditura")
plt.xlabel("L")
plt.ylabel("eff")
plt.show()
