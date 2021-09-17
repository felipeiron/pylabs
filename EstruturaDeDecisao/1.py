import os
os.system('cls')

print('##### MAIOR NÚMERO #####\n')
#Here I will not store information in two variables. Only one is necessary.
num = float(input('Digite um número: '))
num -= float(input('Digite outro número: '))
#As I didn't store two values, so now I won't show the value of variable. This value still on screen yet.
if num < 0:
    print('\nO segundo número é maior!\n')
elif num > 0:
    print('\nO primeiro número é maior!\n')
else:
    print('\nOs números são iguais!\n')