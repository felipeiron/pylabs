import os
os.system('clear')

print('##### MENOR PREÇO #####\n')
p1 = float(input('Primeiro preço: '))
p2 = float(input('Segundo preço: '))
p3 = float(input('Terceiro preço: '))

if p1 < p2 and p1 < p3:
    print('\nCompre o primeiro produto. O preço é {}\n'.format(p1))
elif p2 < p1 and p2 < p3:
    print('\nCompre o segundo produto. O preço é {}\n'.format(p2))
else:
    print('\nCompre o terceiro produto. O preço é {}\n'.format(p3))