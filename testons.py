import random

a = random.randint(1,6)
b = random.randint(1,6)
x = str(a) + str(b)
result = (''.join(sorted(x, reverse=True)))

def nombre1():
    print('Voici ton nombre: ' + result )
    return nombre1

def mentirOuPas():
    while
    print('Veux-tu garder ton nombre ? ')
    choix = input('(O)UI ou (N)ON')
    if choix == 'O':
        print('Tu gardes: ' + (result))
    elif choix == 'N':
        print('Voici votre nouveau nombre: ' + nombre1())
    elif choix != 'O' and choix != 'N':
        print('Mauvaise saisie')
        nombre1()

while
nombre1()
mentirOuPas()