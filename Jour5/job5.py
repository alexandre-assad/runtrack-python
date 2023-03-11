def parcours(x,y):
    distance = ((((x * y)*2) * 5)*7)/100
    return "Pour {} marches de {} cm, il parcours {} m par semaine en allant 5 fois aux toilettes par jour".format(x,y,distance)


print(parcours(5,6))