import os
os.system('clear')

print('##### MAIOR E MENOR #####\n')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print('\nO maior número é {}'.format(n1))
    if n2 < n3:
        print('O menor número é {}\n'.format(n2))
    else:
        print('O menor número é {}\n'.format(n3))
elif n2 > n1 and n2 > n3:
    print('\nO maior número é {}'.format(n2))
    if n1 < n3:
        print('O menor número é {}\n'.format(n1))
    else:
        print('O menor número é {}\n'.format(n3))
elif n3 > n1 and n3 > n2:
    print('\nO maior número é {}'.format(n3))
    if n1 < n2:
        print('O menor número é {}\n'.format(n1))
    else:
        print('O menor número é {}\n'.format(n2))
else:
    print('\nTodos números são iguais!!!\n')