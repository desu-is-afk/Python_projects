from random import randint as rint
import rps_def as rps

print('\nROCK & PAPER & SCISSORS\n')
uinput = int(input('1. Rock\n2. Paper\n3. Scissor\n>>> '))
mchn = int(rint(1, 3))

if uinput == 1:
    rps.userrock(mchn)
elif uinput == 2:
    rps.userpaper(mchn)
elif uinput == 3:
    rps.userscissors(mchn)
else:
    print('Play normally, bruh...')