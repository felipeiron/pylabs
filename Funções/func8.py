import os
os.system('clear')

def digitos(valor):
    return len(str(valor))

numero = int(input('Digite um número inteiro: '))
resutado = digitos(numero)

print(f'O número possui {resutado} digitos')