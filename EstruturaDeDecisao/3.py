import os
os.system('clear')

print('##### M ou F #####\n')
sexo = input('Digite F ou M: ')

if sexo == 'F':
    print('\nF - Feminino\n')
elif sexo == 'M':
    print('\nM - Masculino\n')
else:
    print('\nEntrada inválida!\n')