import random

def somme(liste,x):
    liste[x] = liste[x-1] + liste[x+1]
    return liste
    
def loto():
    L = []
    for i in range(5):
        L.append(random.randint(5,50))
    print(L[1])
    somme(L,3)
    print(L[len(L)-1])
    
loto()