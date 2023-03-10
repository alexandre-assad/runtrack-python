def draw_rectangle(x,y):
    ligne = "" #Les lignes que je vais afficher
    for i in range (y):
        for j in range (x):
            if j == 0 or j == x-1: #Si on est au début ou a la fin de la ligne, j'affiche un |
                ligne += "|"
            elif i == 0 or i == y-1: #Si on est la ligne du dessous ou du dessus et pas aux extremité, j'affiche -
                ligne += "-"
            else:
                ligne += " " #Sinon un espace (surtout pour le centre)
        print(ligne)
        ligne = ""
    
draw_rectangle(10,3)
draw_rectangle(20,4)