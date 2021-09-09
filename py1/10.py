import os
os.system('cls')

print('##### CELSIUS --> FAHRENHEIT #####\n')
C = float(input('Digite o valor em Celsius: '))
F = (C * (9 / 5)) + 32

print('\nA temperatura {:.2f}°F equivale ao valor digitado em Celsius.\n'.format(F))