import os
import math
os.system('cls')

print('##### LOJA DE TINTAS #####\n')
area = float(input('Área a ser pintata(m²): '))

print('\nVocê precisa de {:.2f} latas de tinta.\nO valor é: {:.2f}'.format(math.ceil(area / 54.0), math.ceil((area / 54.0)) * 80.0))