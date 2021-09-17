import os
os.system('cls')

print('##### CONVERTE TEMPERATURA #####\n')
f = float(input('Qual a temperatura em Fahrenheit? '))
c = 5 * ((f - 32) / 9)

print('\nA temperatura {:.2f}°C equivale ao valor digitado em Fahrenheit,'.format(c))