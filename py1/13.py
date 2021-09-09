import os
os.system('cls')

print('##### ALTURA - HOMEM E MULHER #####\n')
altura = float(input('Digite sua altura: '))

print('\nPeso ideal se for mulher: {:.2f}\nPeso Ideal se for homem: {:.2f}\n'.format((62.1 * altura) - 44.7, (72.7 * altura) - 58))