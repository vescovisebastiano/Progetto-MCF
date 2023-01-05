'''utilizzare una simulazione Monte Carlo per ottimizzare la geometria del sistema in modo tale da poter risolvere isotopi con una differenza di numero di massa1 in un intervallo di masse 1-210;'''

import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import math

#definizione parametri e funzioni
e=1.6*pow(10, -19)
V=1000
B=0.1
uma=1.66*pow(10, -27)

def raggio(m, s0): #raggio da massa
    return np.sqrt(m*8*V*uma/(e*pow(B, 2)))-s0  #cost circa 0.0083

def m(r): #massa da raggio
    return pow(r, 2)*pow(B,2)*e/(2*V) 

#COSTRUZIONE SPETTROMETRO 
def spett(l, L, m):
    alfa=np.random.random(1)
    r=raggio(m, alfa*L)
    rmin=raggio(1, L) #minimo raggio che può fare
    n=math.floor((r-rmin)/l)+1  #quanti pixel si accendono
    for i in range (1, 211):
        if n*l >= (raggio(i, L)-rmin) and  n*l <= (raggio(i, 0)-rmin):
            return i

        
#ottimizzazione per avere un solo valore di l e L               
def ottimizza(l, L, m):
    for i in range(1, l.size):
        for j in range(1, m.size):
            if l.size == 1:
                return np.array(l[0], L[0])
            if spett(l[i], L[i], m[j]) != m[j]:
                l=np.delete(l, i)
                L=np.delete(L, i)


#distibuzione casuale per creare le masse 
mass=np.random.randint(low=1, high=211, size=10000)

#distribuzione da 10mm a 100nm, sensibilità 100nm
fend=np.random.randint(low=pow(10, 2), high=pow(10, 3), size=100)/pow(10, 7)
pixel=np.random.randint(low=pow(10, 2), high=pow(10, 3), size=100)/pow(10, 7)

#ciclo che sceglie larghezza della fenditura e dimensione pixel tra quelli sopra
j=0
p=np.empty(0)
f=np.empty(0)
for i in range (0, fend.size):
    for k in range (0, pixel.size):
        while j <= mass.size-1:
            b = spett(pixel[k], fend[i], mass[j])
            if b != mass[j]:
                break
            else:
                j+=1
            if j==mass.size-1 :
                print(i)
                f=np.append (f,fend[i])
                p=np.append(p, pixel[k])
                j=0 #questo ne fa trovare più di una

print(f, p)
ott=ottimizza(f, p, mass)
print(ott)

        

'''print(np.sum(f)/f.size)
print(np.sum(p)/p.size)
print(f, f.size)
print(p,p.size)

plt.plot(f, p, 'o')
plt.xlabel('fenditura')
plt.ylabel('pixel')
plt.show()'''
