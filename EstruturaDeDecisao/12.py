import os
os.system('clear')

print('##### SALARIO 2 #####\n')
hr = float(input('Quanto ganha por hora: '))
h = float(input('Horas trabalhadas: '))

if (hr * h) <= 900:
    print('\nSalário Bruto: ({} * {})     : R$ {}'.format(hr, h, hr * h))
    print('(-) IR (0%)                      : R$ {}'.format(0))
    print('(-) INSS (10%)                   : R$ {}'.format((hr * h) * 0.1))
    print('FGTS (11%)                       : R$ {}'.format((hr * h) * 0.11))
    print('Total de descontos               : R$ {}'.format((hr * h) * 0.1))
    print('Salário Liquido                  : R$ {}\n'.format((hr * h) - ((hr * h) * 0.1)))
elif (hr * h) > 900 and (hr * h) <= 1500:
    print('\nSalário Bruto: ({} * {})     : R$ {}'.format(hr, h, hr * h))
    print('(-) IR (5%)                      : R$ {}'.format((hr * h) * 0.05))
    print('(-) INSS (10%)                   : R$ {}'.format((hr * h) * 0.1))
    print('FGTS (11%)                       : R$ {}'.format((hr * h) * 0.11))
    print('Total de descontos               : R$ {}'.format((hr * h) * 0.15))
    print('Salário Liquido                  : R$ {}\n'.format((hr * h) - ((hr * h) * 0.15)))
elif (hr * h) > 1500 and (hr * h) <= 2500:
    print('\nSalário Bruto: ({} * {})    : R$ {}'.format(hr, h, hr * h))
    print('(-) IR (10%)                     : R$ {}'.format((hr * h) * 0.1))
    print('(-) INSS (10%)                   : R$ {}'.format((hr * h) * 0.1))
    print('FGTS (11%)                       : R$ {}'.format((hr * h) * 0.11))
    print('Total de descontos               : R$ {}'.format((hr * h) * 0.2))
    print('Salário Liquido                  : R$ {}\n'.format((hr * h) - ((hr * h) * 0.2)))
else:
    print('\nSalário Bruto: ({} * {})    : R$ {}'.format(hr, h, hr * h))
    print('(-) IR (20%)                     : R$ {}'.format((hr * h) * 0.2))
    print('(-) INSS (10%)                   : R$ {}'.format((hr * h) * 0.1))
    print('FGTS (11%)                       : R$ {}'.format((hr * h) * 0.11))
    print('Total de descontos               : R$ {}'.format((hr * h) * 0.30))
    print('Salário Liquido                  : R$ {}\n'.format((hr * h) - ((hr * h) * 0.30)))