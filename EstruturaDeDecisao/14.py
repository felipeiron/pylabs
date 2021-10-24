import os
os.system('clear')

print('##### MÉDIA E CONCEITO #####\n')
nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua segunda nota: '))
media = (nota1 + nota2) / 2

if media > 9.0 and media <= 10.0:
    print('\nSuas notas foram {} e {}, e a média é {} - Conceito A - Aprovado\n'.format(nota1, nota2, media))
elif media > 7.5 and media <= 9.0:
    print('\nSuas notas foram {} e {}, e a média é {} - Conceito B - Aprovado\n'.format(nota1, nota2, media))
elif media > 6.0 and media <= 7.5:
    print('\nSuas notas foram {} e {}, e a média é {} - Conceito C - Aprovado\n'.format(nota1, nota2, media))
elif media > 4.0 and media <= 6.0:
    print('\nSuas notas foram {} e {}, e a média é {} - Conceito D - Reprovado\n'.format(nota1, nota2, media))
elif media >= 0 and media <= 4.0:
    print('\nSuas notas foram {} e {}, e a média é {} - Conceito E - Reprovado\n'.format(nota1, nota2, media))
else:
    print('\nValores muito altos!!!\n')