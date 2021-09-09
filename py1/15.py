import os
os.system('cls')

print('##### HOLERITE #####\n')
hr = float(input('Quanto ganha por hora: '))
h = float(input('Quantas horas trabalhadas: '))

print('\n+ Salário Bruto: R$ {}\n- IR (11%): R$ {}\n- INSS (8%): R$ {}\n- Sindicato (5%): R$ {}\n= Salário Liquido: R$ {}'.format(hr * h, 11 % (hr * h)))