import os
os.system('clear')

def reverter(valor):
    return str(valor)[::-1]
#[::-1] é um slice (fatia) que indica que queremos todos os elementos da string (:) em ordem inversa (-1)

numero = int(input('Digite um número inteiro: '))
resultado = reverter(numero)
print(f'O valor revertido é {resultado}')