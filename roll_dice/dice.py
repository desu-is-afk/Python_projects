from random import randint as rint

print('\n!! Use apenas números\n')

try:
    dice = int(input('Qual dado deseja rolar?\n>>> d'))
    if dice == 1:
        print('\nIsso não faz sentido!\n')
except ValueError:
    print('Valor inserido é inválido.')

multirll = str(input('Deseja rolar mais de um dado?\n0. Não\n1. Sim\n>>> '))
if multirll == '1':
    try:
        un = int(input('Rolará quantos?\n>>> '))
    except ValueError:
        print('Valor inserido é inválido.')
    listrolls = []
    print('\nRolou {}d{}\nCaiu:\n'.format(un, dice))
    for rll in range(un):
        roll = rint(1, dice)
        if roll == dice:
            print(roll, 'CRITICAL!')
        else:
            print(roll)
        listrolls.append(roll)
    result = sum(listrolls)
    print('Total: ', result)
elif multirll == '0':
    roll = rint(1, dice)
    if roll == dice:
        print('CRITICAL')
    print('\nRodou d{}!\nCaiu {}'.format(dice, roll))
else:
    print('ué')