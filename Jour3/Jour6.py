alpha = "abcdefghijklmnopqrstuvwxyz"

def pyramide(str, x):
    comptage = 0
    ligne = ""
    #On commencer le nombre de ligne qu'on veut
    for i in range (x):
        #A l'intérieur, on veille à ce que chaque ligne est une lettre de plus, et démarre de la fin de la ligne précédence
        for y in range (comptage, comptage + i):
            # On gère les cas entre z et a
            while y >= 26:
                y = y - 26
            if comptage >= 26:
                comptage -= 26
            ligne += str[y]
            comptage += 1

        print(ligne)
        ligne = ""

pyramide(alpha,250)
