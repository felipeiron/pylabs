import os
os.system('cls')

print('##### DOWNLOAD #####\n')
arq = float(input('Tamanho do arquivo em MB: '))
vel = float(input('Velocidade do link em Mbps: '))

print('\nTempo de download: {:.2f} minutos\n'.format((arq / (vel / 8)) / 60))