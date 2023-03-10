string1 = "Je suis une phrase avec e"
string2 = "J'suis un'phras sans la lttr"

def contientE_Parcour(str): #Une fonction qui parcours lettre par lettre
    for i in str: #i va s'indenter avec le caractère de la string
        if i == "e":    #On vérifie si la lettre de la chaine est un "e"
            return "La string '{}' contient la lettre e".format(str)
    return "La string '{}' ne contient pas la lettre e".format(str)

#Surement une fonction (avec de légères modifications) plus utile si on veut connaître la quantité et la position des lettre dans la string

def contientE_simple(str): #Une fonctions plus simple
    if "e" in str:          #Ici on demande si la chaine contient directement la lettre E
        return "La string '{}' contient la lettre e".format(str)
    else:
        return "La string '{}' ne contient pas la lettre e".format(str)

#Surement la meilleure fonction pour cet exercice

print(contientE_Parcour(string1))
print(contientE_Parcour(string2))
print(contientE_simple(string1))
print(contientE_simple(string2))

