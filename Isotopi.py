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
    return -s0+np.sqrt(m*8*V*uma/(e*pow(B, 2))) #cost circa 0.0083

def m(r):
    return pow(r, 2)*pow(B,2)*e/(2*V) #massa da raggio

#COSTRUZIONE SPETTROMETRO FACILE
def spett1(L, m):
    alfa=np.random.random(1)
    r=raggio(m, alfa*L)
    #print(r)
    n=math.floor(r/L)+1 #quanti pixel si accendono
    #print(n)
    for i in range (1, 211):
        if n*L >= raggio(i, 0) and  n*L<= raggio(i, L):
            return i

#distibuzione casuale per creare le masse 
mass=np.random.randint(low=1, high=210, size=50)

fend=np.random.uniform(low=pow(10, -7), high=pow(10, -3), size=100000)

j=0
f=np.empty(0)
for i in range (0, fend.size):
    print (i ,"primo ciclo")
    while j <= mass.size-1:
        b = spett1(fend[i], mass[j])
        if b != mass[j]:
            j=0
            break
        else:
            j+=1
        if j==mass.size:
            f=np.append (f ,fend[i])
            j=0

print(np.sum(f)/f.size)
print(f)
print (f.size)
