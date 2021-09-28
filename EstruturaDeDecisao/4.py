import os
os.system('clear')

print('##### VOGAL/CONSOANTE #####\n')
letra = input('Digite uma letra: ')


if letra.capitalize() == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('\nÉ uma vogal!\n')
else:
    print('\nÉ uma consoante!\n')