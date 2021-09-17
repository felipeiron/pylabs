import os
os.system('cls')

print('##### HOLERITE #####\n')
hr = float(input('Quanto ganha por hora: '))
h = float(input('Quantas horas trabalhadas: '))

print('\n+ Salário Bruto: R$ {}\n- IR (11%): R$ {}\n- INSS (8%): R$ {}\n- Sindicato (5%): R$ {}\n= Salário Liquido: R$ {}\n'\
    .format(hr * h, 0.11 * (hr * h), 0.08 * (hr * h), 0.05 * (hr * h), (hr * h) - (0.24 * (hr * h))));