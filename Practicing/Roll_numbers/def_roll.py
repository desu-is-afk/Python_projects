from random import randint as rint

def zeroum(z1):
    if z1 == 0:
        num = int(input("Qual o número de rolagem?\n>>>"))
        randola = rint(0, num)
    elif z1 == 1:
        num = int(input("Qual o número de rolagem?\n>>>"))
        randola = rint(1, num)
    else:
        print('Valor inválido!')
    return print(f"Na sua rolagem caiu: {randola}")

def numespec(num1, num2):
    try:
        randola = rint(num1, num2)
    except ValueError:
        randola = rint(num2, num1)
    return print(f"Na sua rolagem caiu: {randola}")
