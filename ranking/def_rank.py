def rank(result):
    if result < 0:
        return print(f'{result} pontos?\nVocê teve uma quantia negativa de pontos!\nBanido!\n')
    elif result < 100:
        return print(f'{result} pontos!\nConquistou Bronze!\n')
    elif result < 300:
        return print(f'{result} pontos!\nConquistou Prata!\n')
    elif result < 600:
        return print(f'{result} pontos!\nConquistou Ouro!\n')
    else:
        return print(f'{result} pontos!\nConquistou Diamante!\n')
