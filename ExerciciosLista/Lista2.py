import os

os.system('clear')

lista1 = []

for i in range(0, 10):
    lista1.append(float(input('Digite um número: ')))

lista1.sort(reverse=True)
print(lista1)
