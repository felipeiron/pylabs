import os
os.system('clear')

print('##### ANO BISSEXTO #####\n')
ano = int(input('Informe o ano: '))

#A primeira parte do if testa anos que sejam uniformemente divisiveis por 100 seguinto a regra do calendário gregoriano.
#Caso esse teste seja negativo ele testa o elif, e caso este também seja negativo vai pro else.
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