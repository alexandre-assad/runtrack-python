
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


L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(croissant(L))