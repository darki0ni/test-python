import random
# random.randint prends un chiffre au hasard entre les deux cond données
num1 = random.randint(1,6)
num2 = random.randint(1,6)
def mexion():
    global rule
    rule = (str(num1)+(str(num2)))
    global descending
    descending =''.join(sorted(rule, reverse=True))
    print('Tu as fais: ' + descending)
mexion()
def mentir():
    print("Veux-tu garder ton résultat ?")
    choice = str(input('O = OUI, N = NON'))
    if choice : "O"
    print(descending)
    elif choice == "N":
    print('Bluff ici: ')
    else:
    num1 = int(input())
    print(num1)
    #elif:
    #print("O ou N")
mentir()