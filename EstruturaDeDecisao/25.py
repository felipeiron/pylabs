import os
from posix import ST_NOATIME
os.system('clear')

print('##### PERGUNTAS(Responda SIM ou NAO) #####\n')


if input('Telefonou para a vítima? ').upper() == "SIM":
    count = 1
else:
    count = 0
if input('Esteve no local do crime? ').upper() == "SIM":
    count += 1
if input('Mora perto da vítima? ').upper() == "SIM":
    count += 1 
if input('Devia para a vítima? ').upper() == "SIM":
    count += 1
if input('Já trabalhou para a vítima? ').upper() == "SIM":
    count += 1    

if count == 2:
    print('\nSuspeita!\n')
elif count == 3 or count == 4:
    print('\nCúmplice!\n')
elif count == 5:
    print('\nAssassino!!!\n')
else:
    print('\nInocente!\n')
