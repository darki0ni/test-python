import random

a = random.randint(1,6)
b = random.randint(1,6)
x = str(a) + str(b)

def nombre1():
    print('Voici ton nombre: ' +(''.join(sorted(x, reverse=True))))
    return nombre1
nombre1()

def mentirOuPas():
    print('Veux-tu garder ton nombre ? ')
    ouiNon = input('(O)UI ou (N)ON')
    if ouiNon != 'O' or ouiNon != 'N':
        print('Mauvaise saisie')
    elif ouiNon == 'O':
        print(nombre1)
    elif ouiNon == 'N':
        nombre1()

mentirOuPas()