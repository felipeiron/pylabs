import os
os.system('clear')

print('##### NÚEMROS EM ORDEM DECRESCENTE #####\n')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

if n1 > n2 and n2 > n3:
    print('\n', n1, n2, n3, '\n')
elif n2 > n1 and n1 > n3:
    print('\n', n2, n1, n3, '\n')
elif n3 > n1 and n1 > n2:
    print('\n', n3, n1, n2, '\n')
elif n1 > n3  and n3 > n2:
    print('\n', n1, n3, n2, '\n')
elif n2 > n3 and n3 > n1:
    print('\n', n2, n3, n1, '\n')
else:
    print('\n', n3, n2, n1, '\n')