def ajout(liste, x):
    liste += [x]
    return liste

def doublon(liste):
    newList = []
    condition = True
    for i in liste:
        for y in newList:
            if i == y:
                condition = False
        if condition:
            ajout(newList,i)
        condition = True
    return newList

L = [10,20,30,20,10,50,60,40,80,50,40]
print(doublon(L))