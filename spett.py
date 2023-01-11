import sys, os
import numpy as np
import math

#definizione parametri e funzioni
e=1.602*pow(10, -19)
V=1000
B=0.1
uma=1.66*pow(10, -27)

def raggio(m, s0): #punto di arrivo da massa
    return 2*np.sqrt(m*2*V*uma/(e*pow(B, 2)))-s0  


#COSTRUZIONE SPETTROMETRO l=pixel, L=fenditura

def spe(l, L, m):
    rmin=raggio(1, L) #minimo raggio che una massa può fare
    alfa=np.random.random(1)
    r=raggio(m, alfa*L)
    n=math.floor((r-rmin)/l)+1 #quanti pixel si accendono
    for i in range (1, 211):
        nmax=math.floor((raggio(i,0)-rmin)/l)+1 #massimo numero di pixel per l'i-esima massa
        nmin=math.floor((raggio(i,L)-rmin)/l)+1 #minimo numero di pixel per l'i-esima massa
        if n >= nmin and n <= nmax:
            return i

#ottimizzazione per avere vedere quali valori di l(pixel) e L(fenditura) vanno bene per tutte le masse

def optimize(pixel, fend, mass):
    p=np.empty(0)
    f=np.empty(0)
    for i in range (0, pixel.size):
        j=0
        k=0
        for j in range (0, fend.size):
            while k <= mass.size-1:
                b = spe(pixel[i], fend[j], mass[k])
                if b != mass[k]:
                    j+=1
                    break
                else:
                    k+=1
                if k==mass.size-1:
                    p=np.append (p,[pixel[i]])
                    f=np.append(f, [fend[j]])
                    j+=1
                    k=0
                    break


    return p , f



#funzione per determinare l'efficienza di una copppia di valori L e l

def eff(l, L, m):
    num=np.zeros(shape=210)
    e=np.zeros(shape=210)
    for i in range(0, m.size):
        a=spe (l, L, m[i])
        num[m[i]-1]+=1
        if a==m[i]:
                e[a-1]+=1

    return e/num


def eff1(l, L, m): #efficienza media, quando non ci sono tutte le masse
    k=0
    for i in m:
        a=spe (l, L, i)
        if a==i:
            k+=1

    return k/m.size

    
#funzioni per generare varie masse con varie probabilità

def prob_mat1(m1, m2, p1, size):
    a=np.random.randint(1, 101, size)
    b=np.zeros(len(a))

    mask1= a < p1
    mask2= a >= p1

    b[mask1]=m1
    b[mask2]=m2
    
    return b


def prob_mat2(m1, m2, m3, m4, m5, m6, p1, p2, p3, p4, p5, size):
    a=np.random.randint(1, 1001, size)
    b=np.zeros(len(a))

    mask1= a < p1
    mask2= (a >= p1) & (a < p2)
    mask3= (a >= p2) & (a < p3)
    mask4= (a >= p3) & (a < p4)
    mask5= (a >= p4) & (a < p5)
    mask6= a >= p5

    b[mask1]=m1
    b[mask2]=m2
    b[mask3]=m3
    b[mask4]=m4
    b[mask5]=m5
    b[mask6]=m6


    return b

#set di pixel e fenditure  per provare lo spettrometro

set1=np.arange(5*pow(10, -4), 65*pow(10, -4), 5*pow(10, -4))

#distibuzione casuale di masse per provare lo spettrometro

mass=np.random.randint(low=1, high=211, size=1000)
