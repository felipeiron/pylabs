import os
import random

os.system('clear')

lista_numeros = []
impar = []
par = []

for i in range(0, 20):
    lista_numeros.append(random.randint(-500, 500))
    if lista_numeros[i] % 2 == 0:
        par.append(lista_numeros[i])
    else:
        impar.append(lista_numeros[i])
     
print(f'O vetor inicial é {lista_numeros}')
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')