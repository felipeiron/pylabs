import os
import math
import sys
os.system('clear')

print('##### Equação #####\n')
a = float(input('Valor de a: '))

if a == 0:
    print('\nA equação não é de segundo grau pois A é igual 0.\n')
else:
    b = float(input('Valor de b: '))
    c = float(input('Valor de c: '))
    delta = (b**2) - (4*a*c)

    if delta < 0:
        print('\nA equação não possui raizes reais.\n')
        sys.exit()
    elif delta == 0:
        print('\nA equação possui apenas a raiz: {}.\n'.format(((-1) * b) / 2 * a))
    elif delta > 0:
        print('\nA equação possui duas raizes: {} e {}.\n'.format((((-1) * b)+ math.sqrt(delta) )/ (2 * a),(((-1) * b)- math.sqrt(delta) )/ (2 * a)))
        

