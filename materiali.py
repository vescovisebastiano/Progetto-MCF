import sys, os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('/home/sebastiano/MCF/progetto')

import spett
import ottimizzato

pixel=ottimizzato.bestp
fend=ottimizzato.bestf

m1=spett.prob_mat1(39, 41, 93, 10000)
y=np.empty(0)

for i in m1:
    a=spett.spe(pixel, fend, i)
    y=np.append(y, a)

plt.hist(y, bins=200)
plt.xlabel('massa(uma)')
plt.ylabel('abbondanza')
plt.title('93% 39-K, 7% 41_k')
plt.show()

m2=spett.prob_mat2(191, 97, 194, 195, 196, 198, 74, 200, 464, 736, 936, 10000)
y=np.empty(0)


for i in m2:
    a=spett.spe(pixel, fend, i)
    y=np.append(y, a)

plt.hist(y, bins=200)
plt.title('7.4% 191-Ir, 12.6% 97-Ir, 26.4% 194-Pt, 27.2% 195-Pt, 20% 196-Pt, 5.6% 198 Pt')
plt.xlabel('massa(uma)')
plt.ylabel('abbondanza')
plt.show()


