import math
print("Soit une équation de la forme : ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b**2 - 4*a*c
if(delta < 0):
    print("L'équation n'a pas de solution") 
else:
    if (delta == 0):
        print("L'équation a une solution double.")
        x = -b / (2.*a)
        print ("La solution est x = ",x)
    else:
        print("L'équation a deux solutions solutions.")
        x1 = (-b - math.sqrt(delta)) /(2*a)
        x2 = (-b + math.sqrt(delta)) /(2*a)
        print ("Les solutions sont x1 = ",x1, " et ", x2)