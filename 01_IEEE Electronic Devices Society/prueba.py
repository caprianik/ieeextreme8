# -*- coding: utf-8 -*-
import random

n=[]
N=20
for i in range(N):
    n.append(str(random.randint(1,100)))

M=3
K=2
print n

n_prima=n[:] #una copia del vector para ir rotando el vector
n_sub=[] #el vector de subsecuencias
for i in range(len(n)):
    n_sub=n_prima[0:M] #Coge la primera subsecuencia
    n_sub=sorted(n_sub)#ordenado de menor a mayor
    print n_sub[K-1]
    #Ahora roto el vector
    n_prima.append(n_prima[0]) #Se añade el ultimo numero al final
    n_prima=n_prima[1:len(n)+1] #Se coge desde la posicion 1 hasta el final +1, para que asi este rotado
    
    
    
