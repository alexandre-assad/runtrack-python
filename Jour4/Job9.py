def minetmax(liste):
    min = liste[0]
    max = liste[0]
    for i in liste:
        if i > max:
            max = i
        elif i < min:
            min = i
    return [max,min]

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print(minetmax(L))