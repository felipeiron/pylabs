import os

os.system('clear')

caracteres = []
consoantes = []
cont = 0

for i in range(0, 10):
    caracteres.append(input('Digite uma letra: '))

for item in caracteres:
    if item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
        cont += 1
        consoantes.append(item)

print(f'São {cont} consoantes: {consoantes}')
