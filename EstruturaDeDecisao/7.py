import os
os.system('cls')

print('##### MAIOR E MENOR #####\n')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: 1'))

if num1 > num2 and num2 > num3:
    print('\nO maior é {} e o menor é {}.\n'.format(num1, num3))
elif num1 > num3 and num3 > num2:
    print('\nO maior é {} e o menor é {}.\n'.format(num1, num2))
elif num2 > num1 and num1 > num3:
    print('\nO maior é {} e o menor é {}.\n'.format(num2, num3))
elif num2 > num3 and num3 > num1:
    print('\nO maior é {} e o menor é {}.\n'.format(num2, num1))
elif num3 > num1 and num1 > num2:
    print('\nO maior é {} e o menor é {}.\n'.format(num3, num2))
elif num3 > num2 and num2 > num1:
    print('\nO maior é {} e o menor é {}.\n'.format(num3, num1))
else:
    print('\nNúmeros repetidos!!!.\n')