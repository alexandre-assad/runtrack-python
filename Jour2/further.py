from math import *


#On crée une fonction pour savoir si un triangle est rectangle, utile après
def rectangle(a,b,c):
    if a > b and a > c:
#Je suis obligé de mettre math.isclose() au lieux de simplemment == car pour les triangle rectalgne isocèle, il y a des floats (mathématiquement impossible d'avoir des naturels) et les calculs sont jamais exacts en python
        if isclose(a**2, b**2 + c**2):  
            return True
        else:
            return False
    elif b > a and b > c:
        if isclose(b**2, a**2 + c**2):
            return True
        else:
            return False
    elif c > b and c > a:
        if isclose(c**2 , b**2 + a**2):
            return True
        else:
            return False
    else:
        return False
        
        
def triangle(a, b, c):
    #On vérifie si le triangle est possible
    triang = False
    if a >= b and a >= c:
        if a < b + c:
            triang = True
    elif b >= a and b >= c:
        if b < a + c:
            triang = True
    elif c >= b and c >= a:
        if c < b + a:
            triang = True
    #Maintenant, si c'est un triangle, on va vérifier sa spécifité s'il y en a une
    if triang == True:
        if a == b and a == c:
            return "triangle équilatéral"
        elif a == b or a == c or b == c:
            if rectangle(a,b,c) is True:
                return "triangle rectangle isocèle"
            else:
                return "triangle isocèle"
        elif rectangle(a,b,c) is True:
            return "triangle rectangle"
        else:
            return "triangle quelconque"
    else:
        return "Ce n'est pas un triangle"
    
print(triangle(100,1,1))
print(triangle(3,4,5))
print(triangle(3,3,5))
print(triangle(3,3,3))
print(triangle(3,4,6))
print(triangle(5,5,sqrt(50)))