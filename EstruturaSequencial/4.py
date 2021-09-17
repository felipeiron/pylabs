import os
os.system('clear')

print('##### CALCULANDO MÉDIA ANUAL #####\n')
nota = float(input('Digite a primeira nota:'))
nota += float(input('Digite a segunda nota:'))
nota += float(input('Digite a terceira nota:'))
nota += float(input('Digite a última nota:'))

print('\n##### RESULTADO #####\n\nMédia:', nota/4 )