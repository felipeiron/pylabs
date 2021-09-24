import os
os.system('cls')

print('##### MEDIA #####\n')
nota = float(input('Primeira nota: '))
nota += float(input('Segunda nota: '))
nota = nota /2

if nota >= 7 and nota < 10:
    print('\nAprovado!\n')
elif nota < 7:
    print('\nReprovado!\n')
else:
    print('\nAprovado com distinção!\n')