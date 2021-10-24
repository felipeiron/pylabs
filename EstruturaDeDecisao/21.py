#!/usr/bin/env python3
import os
os.system('clear')

print('##### CAIXA ELETRONICO #####\n')
valor = int(input('Quanto deseja sacar: '))

if valor >= 10 and valor <= 600:
    if len(list(str(valor))) == 2:
        print('\nSerão {} nota(s) de R$ 50, {} de R$ 10, {} de R$ 5 e {} de R$ 1\n'
        .format
        (valor // 50, 
        (valor % 50) // 10, 
        ((valor % 50) % 10) // 5, 
        (((valor % 50) % 10) % 5) //1))
    else:
        print('\nSerão {} nota(s) de R$ 100, {} de R$ 50, {} de R$ 10, {} de R$ 5 e {} de R$ 1\n'
        .format
        (valor // 100, 
        (valor % 100) // 50, 
        ((valor % 100) % 50) // 10, 
        (((valor % 100) % 50) % 10) // 5, 
        ((((valor % 100) % 50) % 10) % 5) // 1))
else:
    print('\nO valor deve ser entre RS$ 10 e R$ 600.\n')

