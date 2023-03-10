import math

def premier(x):
    racine = math.ceil(math.sqrt(x))
    for i in range(2,racine+1):
        if x % i == 0:
            return False
    return True
    
def comptage():
    #2 étant petit, cette méthode plus rapide fonctionne mieux
    print(2)
    for i in range (2,1001):
        if premier(i) is True:
            print(i)
            
print(premier(2))

