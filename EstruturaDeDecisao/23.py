#!/usr/bin/env python3
import os

os.system('clear')

print('##### INTEIRO ou DECIMAL #####\n')
num = float(input('Digite um número: '))

if num == round(num):
    print('\nO número {} é inteiro.\n'.format(num))
else:
    print('\nO número {} é decimal.\n'.format(num))