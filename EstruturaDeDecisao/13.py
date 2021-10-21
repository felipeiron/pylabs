import os
os.system('clear')

print('##### DIA DA SEMANA #####\n')
dia = int(input('Digite um número de 1 à 7: '))

if dia == 1:
    print('\n1 - Domingo\n')
elif dia == 2:
    print('\n2 - Segunda\n')
elif dia == 3:
    print('\n3 - Terça\n')
elif dia == 4:
    print('\n4 - Quarta\n')
elif dia == 5:
    print('\n5 - Quinta\n')
elif dia == 6:
    print('\n6 - Sexta\n')
elif dia == 7:
    print('\n7 - Sábado\n')
else:
    print('\nValor inválido!!!\n')