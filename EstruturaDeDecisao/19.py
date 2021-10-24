#!/usr/bin/env python3
import os
os.system('clear')

print('##### Centenas, Dezenas e Unidades #####\n')

num = input('Digite um número entre 0 e 999: ')

if int(num) < 0 or int(num) >= 1000:
    print('\nValor inválido!\n')
elif len(list(num)) == 1:
    print('\nApenas unidades foram digitadas. E foram {} unidades.\n'.format(num))
elif len(list(num)) == 2:
    print('\nApenas dezenas e unidades foram digitadas. E foram {} dezenas e {} unidades.\n'.format(list(num[0]), list(num[1])))
else:
    print('\nSão {} centenas, {} dezenas e {} unidades.\n'.format(list(num[0]), list(num[1]), list(num[2])))