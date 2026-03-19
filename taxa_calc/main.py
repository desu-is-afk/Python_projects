import def_taxa as dtaxa
from random import randint as rint

saldo = rint(1000, 9999)
extrato = rint(50, 9999)

print(10*'=', ' SAQUE ', 10*'=')
print(f'\nSeu saldo é de: R${saldo}')
print(f'Desejas sacar: R${extrato}\n')

dtaxa.saque(saldo, extrato)
