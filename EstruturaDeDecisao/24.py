#!/usr/bin/env python3
import os
from decimal import Decimal

os.system('clear')

print('##### OPERAÇÕES #####\n')
num1 = Decimal(input('Digite um número: '))
op = input('Escolha umas das operação(+, -, *, /): ')
num2 = Decimal(input('Digite o segundo número: '))

if op == '+':
    print('\nO Resultado da soma é: {}'.format(num1 + num2))
    if num1 + num2 == round(num1 + num2):
        print('A soma é inteiro.')
        if (num1 + num2) % 2 != 0:
            print('A soma é IMPAR!')
        else:
            print('A soma é PAR!')
    else:
        print('A soma é decimal.')
    if num1 + num2 > 0:
        print('A soma é positivo!\n')
    elif num1 + num2 < 0:
        print('A soma é negativo.\n')
    else:
        print('A soma é ZERO!\n')

elif op == '-':
    print('\nO Resultado da subtração é: {}\n'.format(num1 - num2))
    if num1 - num2 == round(num1 - num2):
        print('A subtração é inteiro.')
        if (num1 - num2) % 2 != 0:
            print('A subtração é IMPAR!')
        else:
            print('A subtração é PAR!')
    else:
        print('A subtração é decimal.')
    if num1 - num2 > 0:
        print('A subtração é positivo!\n')
    elif num1 - num2 < 0:
        print('A subtração é negativo.\n')
    else:
        print('A subtração é ZERO!\n')    
elif op == '/':
    print('\nO Resultado da divisão é: {}\n'.format(num1 / num2))
    if num1 / num2 == round(num1 / num2):
        print('A divisão é inteiro.')
        if (num1 / num2) % 2 != 0:
            print('A divisão é IMPAR!')
        else:
            print('A divisão é PAR!') 
    else:
        print('A divisão é decimal.')
    if num1 / num2 > 0:
        print('A divisão é positivo!\n')
    elif num1 / num2 < 0:
        print('A divisão é negativo.\n')
    else:
        print('A divisão é ZERO!\n') 
elif op == '*':
    print('\nO Resultado da multiplicação é: {}\n'.format(num1 * num2))
    if num1 * num2 == round(num1 * num2):
        print('A multiplicação é inteiro.')
        if (num1 * num2) % 2 != 0:
            print('A multiplicação é IMPAR!')
        else:
            print('A multiplicação é PAR!') 
    else:
        print('A multiplicação é decimal.')
    if num1 * num2 > 0:
        print('A multiplicação é positivo!\n')
    elif num1 * num2 < 0:
        print('A multiplicação é negativo.\n')
    else:
        print('A multiplicação é ZERO!\n')
else:
    print('\nOperação inválida!\n')