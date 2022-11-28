def interface():
    x = (input('Votre nombre: '))
    if (x != int):
            print('Veuillez entrer un nombre entier.')
            continuer = True
            while continuer:
                interface()
                continuer = input("On continue? (o/n) ").lower() in ("o", "oui")
    y = (input('Votre deuxième nombre: '))
    if (y != int):
            print('Veuillez entrer un nombre entier.')
            while continuer:
                interface()
            continuer = ("On continue? (o/n) ").lower() in ("o", "oui")
    mat = str(input('Type de calcul: '))
    if (mat != ('x','+','-','/')):
        print('Veuillez entrer un type de calcul: x, -, +, /')
        while continuer:
            interface()
        continuer = input("On continue? (o/n) ").lower() in ("o", "oui")
def calculator():
    if (mat == 'x'):
        print(int(x*y))
    if (mat == '+'):
        print(int(x+y))
    if (mat == '-'):
        print(int(x-y))
    if (mat == '/'):
        print(float(x/y))
    calculator()
