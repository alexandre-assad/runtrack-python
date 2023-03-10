def Salade(type, saison):
    if type == "fruit" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruit" and saison == "ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine,navet"
    else:
        return "Le type d'alliment ou la saison est non correct"
    
print(Salade("fruit","ete"))
print(Salade("legume","ete"))
print(Salade("fruit","hiver"))
print(Salade("legume","hiver"))
print(Salade("fleur","printemps"))