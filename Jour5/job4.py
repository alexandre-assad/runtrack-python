alpha = "abcdefghijklmnopqrstuvwxyz"

def recherche(lettre): #Pour avoir l'index d'une lettre sans faire de dictionnaire
    compteur = 0
    for i in alpha:
        if lettre == i:
            return compteur
        else:
            compteur +=1
    return compteur

def codage(str,n):  #Pour coder un message
    code = ""
    for i in str:
        if recherche(i)+n >= 26:
            code += alpha[(recherche(i)+n)-26]
        else:
            code += alpha[recherche(i)+n]
    return code

def encodage(str,n): #Quasiment la même fonction mais inverse
    code = ""
    for i in str:
        if recherche(i)-n <= 0:
            code += alpha[(recherche(i)-n)+26]
        else:
            code += alpha[recherche(i)-n]
    return code


print(codage("bonjour",1))
print(codage("xylo",2))
print(encodage("zanq",2))