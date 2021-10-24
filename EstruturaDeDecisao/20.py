#!/usr/bin/env python3
import os
os.system('clear')

print('##### MÉDIA 2 #####\n')
nota = float(input('Primeira nota: '))
nota += float(input('Segunda nota: '))
nota += float(input('Terceira nota: '))

if nota / 3 == 10:
    print('\nAprovado com distinção!\n')
elif nota / 3 >= 7:
    print('\nAprovado! Média: {}\n'.format(nota / 3))
else:
    print('\nReprovado! Média: {}\n'.format(nota / 3))