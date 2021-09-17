import os
os.system('cls')

print('##### PESO IDEAL #####\n')
calc = float(input('Digite sua altura: '))
calc = (72.7 * calc) - 58

print('\nSeu peso ideal é {:.2f}\n'.format(calc))