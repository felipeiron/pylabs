import os
import time

os.system('clear')

while True:
    nota = float(input('Digite sua nota(0 ~~ 10): '))
    if nota < 0 or nota > 10:
         print('Valor inválido! Tente novamente!')
         time.sleep(2)
    else:
        break