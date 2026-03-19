from random import randint as rint
import def_rank as drank

pontos = rint(900, 1000)
derrotas = rint(0, 125)

print('')
print(10*'=', " ESSES VALORES SÃO DE EXEMPLO! ", 10*'=')
print('Você adquiriu {} pontos e {} derrotas'.format(pontos, derrotas))

resultado = int(pontos - (derrotas * 10))

drank.rank(resultado)
