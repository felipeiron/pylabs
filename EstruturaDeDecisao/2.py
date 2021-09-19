import os
os.system('clear')

print('##### POSITIVO/NEGATIVO #####\n')
num = float(input('Digite um número: '))

if num > 0:
    print('\nNúmero positivo!\n')
elif num < 0:
    print('\nNúmero negativo!\n')
else:
    print('\nDigite um número maior ou menor que ZERO!!!\n')