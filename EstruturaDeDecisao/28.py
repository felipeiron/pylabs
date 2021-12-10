import os
from tabulate import tabulate

os.system('clear')

print('##### PROMOÇÃO DE CARNES #####\n')

tab = [['File Duplo', 'R$ 4,90 por Kg', 'R$ 5,80 por Kg'],
['Alcatra', 'R$ 5,90 por Kg', 'R$ 6,80 por Kg'],
['Picanha', 'R$ 6,90 por Kg', 'R$ 7,80 por KG']
]

print(tabulate(tab, headers=['   ', 'Até 5Kg', 'Acima de 5Kg']))

type = input('\nTipo da carne: ')
qtd = float(input('Quantidade em Kg: '))
card = input('Pagamento no cartão Tabajara(sim ou não): ')

if card.capitalize == 'SIM':
    if qtd <= 5.0:
        if type.capitalize == 'FILE DUPLO':
            print('\nTipo da carne: {}\nQuantidade: {}\nPagamento: Cartão Tabajara\n\Total: {}\nDesconto: {}\nValor a pagar: {}
            ')