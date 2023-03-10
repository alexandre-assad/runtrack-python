def arrondi(n):  #Comme les arrondi sont que des pas de 1 ou 2 avec des nombre naturels, je teste simplement
    if (n+1)%5 == 0:
        return n+1
    elif (n+2)%5 == 0:
        return n+2
    else:
        return n
    
def notes(liste):
    newList = []
    for i in liste:
        newList.append(arrondi(i))
    return newList


print(notes([78,72,45,53,51]))