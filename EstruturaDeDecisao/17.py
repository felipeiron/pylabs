import os
os.system('clear')

print('##### ANO BISSEXTO #####\n')
ano = int(input('Informe o ano: '))

if ano % 100 == 0:
    if ano % 400 == 0:
        if ano % 4 == 0:
            print('\nO ano {} é bissexto.\n'.format(ano))
    else:
        print('\nO ano {} não é bissexto!\n'.format(ano))     
elif ano % 4 == 0:
    print('\nO ano {} é bissexto.\n'.format(ano))
else:
    print('\nO ano {} não é bissexto!\n'.format(ano))