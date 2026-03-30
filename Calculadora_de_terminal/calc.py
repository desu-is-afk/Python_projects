#!/usr/bin/python3

while True:
    try:
        equacao = input('Write a simple math expression:\n>>> ')
        if equacao.lower() in ["exit", "break", "quit"]:
            print("Shutting Down...")
            break
        else:
            print("Result:")
            result = eval(equacao)
            print(result)
    except KeyboardInterrupt:
        print('\nInterrupted!\nQuitting...\n')
        break
    except Exception as e:
        print('Erro:', e)
