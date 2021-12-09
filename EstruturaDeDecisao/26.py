import os
os.system('clear')

print('##### ALCOOL x GASOLINA #####\n')

comb = input('Qual combustivél(A - Alcool ou G - Gasolina): ')
lit = int(input('Quantos litros: '))

if comb.upper() == 'A':
    if lit > 20:
        print('\nValor a ser pago: {}\n'.format(lit * (1.9 - 1.9 * 0.05)))
    else:
        print('\nValor a ser pago: {}\n'.format(lit * (1.9 - 1.9 * 0.03)))
elif comb.upper() == 'G':
    if lit > 20:
        print('\nValor a ser pago: {}\n'.format(lit * (2.5 - 2.5 * 0.06)))
    else:
        print('\nValor a ser pago: {}\n'.format(lit * (2.5 - 2.5 * 0.04)))
