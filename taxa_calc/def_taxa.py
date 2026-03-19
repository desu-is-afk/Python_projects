def saque(saldo, sacar):
    if sacar > saldo:
        return print('Saldo insuficiente!\n')
    elif sacar >= 1000:
        print('Seu saque, por ser um valor muito alto, será cobrado uma taxa de 2%')
        total = float(saldo - (sacar * 1.02))
        return print(f'Para sacar {sacar}, será cobrado {float(sacar * 1.02)}.\nSaldo: {total}.\n')
    else:
        total = int(saldo - sacar)
        return print(f'Sucesso!\nSaldo: {total}.')
