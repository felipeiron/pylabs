import os
os.system('clear')

print('##### VALOR FRUTAS #####\n')
peso_mor = float(input('Digite o peso dos morangos em KG: '))
peso_mac = float(input('Digite o peso das maçãs em KG: '))
peso_total = peso_mor + peso_mac

if peso_total <= 5:
    print('\nVocê pagará R$ {:.2f}.\n'.format((peso_mor * 2.5)+(peso_mac * 1.8)))
elif peso_total > 5 and peso_total <= 8:
    print('\nVocê pagará R$ {:.2f}.\n'.format((peso_mor * 2.2)+(peso_mac * 1.5)))
else:
    print('\nVocê pagará R$ {:.2f}.\n'.format(((peso_mor * 2.2)+(peso_mac * 1.5))*0.9))