print("="*10, "TIME CALC", "="*10)

# Tempo em minutos e em segundos para facilitar
tempo_min = int(input('\nQuantos minutos tem o vídeo?\n>>> '))
tempo_sec = int(input('Quantos segundos tem o vídeo?\n>>> '))

# Subtotal é o tempo do vídeo em segundos
tempo_subtotal = (tempo_min * 60) + tempo_sec
acelerado = float(input('Quanto quer acelerar o vídeo? (1.01x~2x)\n>>>'))

# Bloco para caso o usuário exagere...haha
if acelerado <= 1:
    print('Valor muito pequeno!')
elif acelerado > 2:
    print("valor muito alto!")
# Tempo total é igual ao tempo subtotal vezes a porcentagem do aceleramento
# Dividido por 2, porque quando voce acelera em 2x voce economiza 50% do tempo, e não 100%
tempo_total = int(tempo_subtotal * (1 - (((acelerado) - 1) / 2)))

# tempo salvo em minutos e segundos (para facilitar)
tempo_salvo_min = int(tempo_total / 60)
tempo_salvo_sec = int(tempo_total % 60)

# OUTPUT!
print(f"\nAo invés de gastar {tempo_min} minutos e {tempo_sec} segundos")
print(f'Você gastará {tempo_salvo_min} minutos e {tempo_salvo_sec} segundos! :D')

#FIM
print('\nFim.')
print("="*10, "TIME CALC", "="*10)
