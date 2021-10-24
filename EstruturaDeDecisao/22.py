#!/usr/bin/env python3
import os
os.system('clear')

print('##### PAR OU IMPAR #####\n')
num = int(input('Digite um número inteiro: '))

if num % 2 != 0:
    print('\nO número {} é IMPAR!\n'.format(num))
else:
    print('\nO número {} é PAR!\n'.format(num))