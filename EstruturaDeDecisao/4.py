import os
os.system('clear')

print('##### VOGAL/CONSOANTE #####\n')
letra = input('Digite uma letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('\nÉ uma vogal!\n')
elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('\nÉ uma vogal!\n')
else:
    print('\nÉ uma consoante!\n')