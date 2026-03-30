#!/usr/bin/python3

while True:
    try:
        equacao = input('Escreva uma equação básica:\n>>> ')
        if equacao.lower() in ["exit", "break", "quit"]:
            print("Shutting Down...")
            break
        else:
            result = eval(equacao)
            print(result)
    except KeyboardInterrupt:
        print('\nInterrupted!\nQuitting...\n')
        break
    except Exception as e:
        print('Erro:', e)
