import os
import math
os.system('cls')

print('##### LOJA DE TINTAS #####\n')
area = float(input('Área a ser pintata(m²): '))

print('\nApenas latas: {} ----------------------- Valor: {}\nApenas galões: {} ---------------------- Valor: {} \nLatas e galões: {} Latas e {} Galões -- Valor: {}\n'\
    .format(math.ceil(area / 108.0), math.ceil(area / 108.0) * 80.0,\
    math.ceil(area / 21.6), math.ceil(area / 21.6) * 25.0,\
    area // 108.0, math.ceil((area / 108.0) - (area // 108.0)), ((area // 108.0) * 80.0) + (math.ceil(((area / 108.0) - (area // 108.0))) * 25.0)));