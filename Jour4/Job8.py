L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def sommePair(liste):
    som = 0
    for i in liste:
        if i % 2 == 0:
            som += i
    return som

print(sommePair(L))