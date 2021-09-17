import os
os.system('cls')

print('##### SALÁRIO #####\n')
salario = float(input('Quanto você ganha em 1 hora? '))
salario *= float(input('Quantas horas trabalhadas? '))

print('\nSeu salario é ${} dólares.\n'.format(salario))