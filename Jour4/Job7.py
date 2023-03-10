def multiple(liste):
    compteur = 0
    for i in liste:
        if i % 3 == 0:
            compteur += 1
    return compteur


L = [8, 24,48,2,16]
print(multiple(L))