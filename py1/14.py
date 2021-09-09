import os
os.system('cls')

print('##### QUILOS DE PEIXE #####\n')
peso = float(input('Digite quantos quilos pescou: '))
excesso = peso - 50.0
multa = excesso * 4.0

print('\nPara {} KG com excesso de {} KG a multa é R$ {}.\n'.format(peso, excesso, multa))