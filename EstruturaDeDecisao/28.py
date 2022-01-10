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
card = input('Pagamento no cartão Tabajara(sim ou nao): ')

if card.upper() == 'SIM':
    if qtd <= 5.0:
        if type.upper() == 'FILE DUPLO':
            print(f'\nTipo da carne: {"File Duplo"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 4.9:.2f}\
                \nDesconto: {(qtd * 4.9)*0.05:.2f}\nValor a pagar: {(qtd * 4.9)*0.95:.2f}')
        elif type.upper() == 'ALCATRA':
            print(f'\nTipo da carne: {"Alcatra"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 5.9:.2f}\
                \nDesconto: {(qtd * 5.9)*0.05:.2f}\nValor a pagar: {(qtd * 5.9)*0.95:.2f}')
        elif type.upper() == 'PICANHA':
            print(f'\nTipo da carne: {"Picanha"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 6.9:.2f}\
                \nDesconto: {(qtd * 6.9)*0.05:.2f}\nValor a pagar: {(qtd * 6.9)*0.95:.2f}')
    elif qtd > 5.0:
        if type.upper() == 'FILE DUPLO':
            print(f'\nTipo da carne: {"File Duplo"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 5.8:.2f}\
                \nDesconto: {(qtd * 5.8)*0.05:.2f}\nValor a pagar: {(qtd * 5.8)*0.95:.2f}')
        elif type.upper() == 'ALCATRA':
            print(f'\nTipo da carne: {"Alcatra"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 6.8:.2f}\
                \nDesconto: {(qtd * 6.8)*0.05:.2f}\nValor a pagar: {(qtd * 6.8)*0.95:.2f}')
        elif type.upper() == 'PICANHA':
            print(f'\nTipo da carne: {"Picanha"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 7.8:.2f}\
                \nDesconto: {(qtd * 7.8)*0.05:.2f}\nValor a pagar: {(qtd * 7.8)*0.95:.2f}')
elif card.upper() == 'NAO':
    if qtd <= 5.0:
        if type.upper() == 'FILE DUPLO':
            print(f'\nTipo da carne: {"File Duplo"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 4.9:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 4.9:.2f}')
        elif type.upper() == 'ALCATRA':
            print(f'\nTipo da carne: {"Alcatra"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 5.9:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 5.9:.2f}')
        elif type.upper() == 'PICANHA':
            print(f'\nTipo da carne: {"Picanha"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 6.9:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 6.9:.2f}')
    elif qtd > 5.0:
        if type.upper() == 'FILE DUPLO':
            print(f'\nTipo da carne: {"File Duplo"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 5.8:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 5.8:.2f}')
        elif type.upper() == 'ALCATRA':
            print(f'\nTipo da carne: {"Alcatra"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 6.8:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 6.8:.2f}')
        elif type.upper() == 'PICANHA':
            print(f'\nTipo da carne: {"Picanha"}\nQuantidade: {qtd}\nPagamento: Cartão Tabajara\nTotal: {qtd * 7.8:.2f}\
                \nDesconto: {"0"}\nValor a pagar: {qtd * 7.8:.2f}')