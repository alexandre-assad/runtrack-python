def inverse(str):
    newWord = ""
    #On fait une boucle inversé (de la fin du mot à 0, avec un pas de -1)
    for i in range (len(str)-1,-1,-1):
        newWord += str[i]
    return newWord

print(inverse("nikana"))
print(inverse("Je suis une phrase"))
print(inverse("A Cuba Anna a bu ca"))