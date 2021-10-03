import os
os.system('clear')

print('##### TURNO DA ESCOLA #####\n')
print('Os turnos são: M - Matutino, V-Vespertino ou N-Noturno\n')
turno = input('Qual turno você estuda:')

if turno.capitalize() == 'M':
    print('\nBom dia!\n')
elif turno.capitalize() == 'V':
    print('\nBoa tarde!\n')
elif turno.capitalize() == 'N':
    print('\nBoa noite!\n')
else:
    print('\nValor inválido!!!\n')