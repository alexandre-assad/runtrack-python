alpha = "abcdefghijklmnopqrstuvwxyz"

def recherche(lettre): #Pour avoir l'index d'une lettre sans faire de dictionnaire
    compteur = 0
    for i in alpha:
        if lettre == i:
            return compteur
        else:
            compteur +=1
    return compteur

def inversion(str,i,j):
    chaine = []
    temporaire = 0
    for x in str:
        chaine.append(x)
    temporaire = chaine[i]
    chaine[i] = chaine[j]
    chaine[j] = temporaire
    return ''.join(chaine)

def tri_chaine(str,x): #On va trier à partir d'un nombre donnée
    chaine = []
    newstr = ""
    for x in range(x):
        newstr += str[x]
    for i in range(x+1,len(str)):
        chaine.append(recherche(str[i]))
    chaine.sort()

    for j in chaine:
        newstr += alpha[j]
    return newstr

def loin(str):
    for i in range(len(str)-1,-1,-1):#On parcours la liste par la fin, ou les modifications sont minimes dans l'alphabet
        for j in range (len(str)-1,-1,-1):
            if recherche(str[i])>recherche(str[j]): #Si la lettre est plus grande que celle avant, le mot sera plus "loin" après inversion
                str = inversion(str,i,j) #Maintenant que j'ai inversé, je vais essayé de trier la suite de la chaine pour avoir le mot le plus proche
                if i != len(str)-1 or j != len(str)-2:
                    str = tri_chaine(str,i-1)
                return str
    return str
            
print(loin("abeedfe"))
print(loin("abcde"))
print(loin("canape"))