def calcule(num1,operator,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Je ne peux calculer avec cet opérateur"

print(calcule(10,"+",2))
print(calcule(10,"-",2))
print(calcule(10,"*",2))
print(calcule(10,"/",2))
print(calcule(10,"%",2))
print(calcule(10,"**",2))