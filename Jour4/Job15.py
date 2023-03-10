
#Je reprends ma fonction du job 12
def longeur(liste):
    compteur = 0
    for i in liste:
        compteur += 1
    return compteur
        
def ajout(liste, x):
    liste += [x]
    return liste

def enleve(liste, index):
    newList = []
    for i in range(longeur(liste)):
        if i != index:
            ajout(newList,liste[i])
    return newList

def minimum(liste):
    min = [liste[0],0]
    for i in range(longeur(liste)):
        if liste[i] < min[0]:
            min = [liste[i],i]
    return min

def croissant(liste):
    newList = []
    for i in range(longeur(liste)):
        min = minimum(liste)
        ajout(newList,min[0])
        liste = enleve(liste,min[1])
    liste = newList
    return liste

def arrondi(liste): #Arrondi n'ayant pas été spécifié, je fais un arrondi supérieur
    compteur = 0
    n = 0
    newList = []
    for i in range(longeur(liste)):
        n = liste[i]
        if n > 0:
            while n > 0:
                n -= 1
                compteur += 1
        else:
            while n < 0:
                n += 1
                compteur -= 1
        ajout(newList,compteur)
        compteur = 0
    return croissant(newList)

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, -5.20, 17.50]
print(arrondi(L))