def extremite(n):
    ligne = ""
    for i in range(n+3): 
        if i == 0 or i == n+2:
            ligne += "+"
        else:
            ligne += "-"
    print(ligne)
def diagonale(n):
    ligne = ""
    extremite(n) #On fera les extrémité avec des fonctions car elles sont totalment différentes
    for i in range(n+1):
        for j in range(n+1): # on va voir, selon la position dans la ligne on affiche quelque chose de différent
            if j == 0 or j == n+1:
                ligne += "|"
            if j == n-i:
                ligne += " "
            else:
                ligne += "#"
        ligne +="|"
        print(ligne)
        ligne = ""
    extremite(n)


diagonale(10)
diagonale(20)