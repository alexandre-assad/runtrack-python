def signe(nombre):
    if type(nombre) is not int:
        return "Pas un nombre"
    elif nombre > 0:
        return "Positif"
    elif nombre < 0:
        return "Négatif"
    else:
        return "Zéro"

        
    
print(signe(10))
print(signe(-10))
print(signe(0))
print(signe("10"))