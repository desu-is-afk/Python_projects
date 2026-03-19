import def_roll as droll

print("\n0. Rolar até um número de limite.")
print("1. Rolar entre números específicos.")
zero_ou_um = int(input("\n>>>"))

if zero_ou_um == 0:
    z1 = int(input("0. Começar rolagem em 0.\n1. Começar rolagem em 1.\n>>> "))
    droll.zeroum(z1)
elif zero_ou_um == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    droll.numespec(num1, num2)
else:
    print("Failure!")

