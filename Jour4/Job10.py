def produitPair(liste):
    som = 1
    for i in liste:
        if i >= 25 and i <= 90:
            som *= i
    if som == 1:
        return "Aucun nombre e [25,90]"
    else:
        return som
    
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(produitPair(L))