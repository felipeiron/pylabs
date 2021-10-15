import os
os.system('clear')

print('##### MAIOR E MENOR #####\n')
<<<<<<< HEAD
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: 1'))

if num1 > num2 and num2 > num3:
    print('\nO maior é {} e o menor é {}.\n'.format(num1, num3))
elif num1 > num3 and num3 > num2:
    print('\nO maior é {} e o menor é {}.\n'.format(num1, num2))
elif num2 > num1 and num1 > num3:
    print('\nO maior é {} e o menor é {}.\n'.format(num2, num3))
elif num2 > num3 and num3 > num1:
    print('\nO maior é {} e o menor é {}.\n'.format(num2, num1))
elif num3 > num1 and num1 > num2:
    print('\nO maior é {} e o menor é {}.\n'.format(num3, num2))
elif num3 > num2 and num2 > num1:
    print('\nO maior é {} e o menor é {}.\n'.format(num3, num1))
else:
    print('\nNúmeros repetidos!!!.\n')
=======
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
>>>>>>> ecd7b81694fa94da7fe30d8665e5faa3a6c25831
