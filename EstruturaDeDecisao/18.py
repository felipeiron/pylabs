#!/usr/bin/env python3

import datetime
import os
from posixpath import split
os.system('clear')

print('##### DATE VALIDATION #####\n')
date = input('Digite uma data no formato dd/mm/aaaa: ')
split_text = date.split('/')

if int(split_text[0]) <= 0 or int(split_text[1]) <= 0 or int(split_text[2]) <= 0:
    print('\nData inválida! Dia, mês ou ano não podem ser ZERO.\n')
elif int(split_text[0]) > 31 or int(split_text[1]) > 12 or int(split_text[2]) > 9999:
    print('\nData inválida! Dia, mês ou ano não podem ser maior que 31,12 e 9999 respectivamente.\n')
elif int(split_text[1]) == 2 and int(split_text[0]) > 28:
    print('\nData inválida! Fevereiro não tem mais que 28 dias!\n')
elif int(split_text[1]) == 4 or int(split_text[1]) == 6 or int(split_text[1]) == 9 or int(split_text[1]) == 11:
    if int(split_text[0]) == 31:
        print('\nData inválida! Esse mês não tem 30 dias!\n')
    else:
        print('\nA data {} é válida!\n'.format(date))
else:
    print('\nA data {} é válida!\n'.format(date))