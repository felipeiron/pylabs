import os
os.system('clear')

print('##### TRIANGULO #####\n')
lado1 = float(input('Primeiro lado do triangulo: '))
lado2 = float(input('Segundo lado do triangulo: '))
lado3 = float(input('Terceiro lado do triangulo: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    if lado1 == lado2 and lado1 == lado3:
        print('\nTemos um triangulo EQUILATERO!\n')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('\nTemos um triangulo ESCALENO!\n')
    else:
        print('\nTemos um triangulo ISOSCELES!\n')
else:
    print('\nNão forma um triangulo! Tente novamente!!!\n')