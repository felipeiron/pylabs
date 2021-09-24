import os
os.system('cls')

print('##### MAIOR NÚMERO #####\n')
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

if num1 > num2 and num1 > num3:
    print('\nO primeiro é o maior!\n')
elif num2 > num1 and num2 > num3:
    print('\nO segundo é o maior!\n')
else:
    print('\nO terceiro é o maior!\n')