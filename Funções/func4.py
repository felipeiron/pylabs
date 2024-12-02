import os

os.system('clear')

def negativo_positivo(a):
    result = 'P' if a > 0 else 'N'
    return result

num = float(input('Digite um número: '))
print(negativo_positivo(num))