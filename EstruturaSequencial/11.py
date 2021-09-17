import os
os.system('cls')

print('##### PRODUTO + SOMA + POTENCIA #####\n')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 3º número: '))
n3 = float(input('Digite o 3 número: '))

print('\nO produto do dobro de {} com a metade de {} é:'.format(n1, n2), (n1 * 2) * (n2 / 2))
print('A soma do triplo de {} com {} é:'.format(n1, n3), (3 * n1) + n3)
print('{} elevado ao cubo é:'.format(n3), n3 ** 3, '\n')