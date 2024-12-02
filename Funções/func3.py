import os

os.system('clear')

def soma(a, b, c):
    result = a + b + c
    return result

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

print(f'A soma dos valores é: {soma(num1, num2, num3)}')