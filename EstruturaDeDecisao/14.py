import os
os.system('clear')

print('##### MÉDIA E CONCEITO #####\n')
nota = float(input('Sua primeira nota: '))
nota += float(input('Sua segunda nota: '))
media = nota / 2

if media > 9.0 and media <= 10.0:
    print('\nA\n')
elif media > 7.5 and media <= 9.0:
    print('\nB\n')
elif media > 6.0 and media <= 7.5:
    print('\nC\n')
elif media > 4.0 and media <= 6.0:
    print('\nD\n')
elif media >= 0 and media <= 4.0:
    print('\nE\n')
else:
    print('\nValores muito altos!!!\n')