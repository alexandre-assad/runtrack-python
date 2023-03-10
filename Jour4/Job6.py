def inversion(liste):
    premier = liste[0]
    dernier = liste[len(liste)-1]
    liste[0] = dernier
    liste[len(liste)-1] = premier
    return liste


L = [8, 24,48,2,16]

print(inversion(L))