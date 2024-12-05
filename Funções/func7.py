import os, time

#Funções
def valorPagamento(valor, atraso):
    if valor == 0:
        return valor
    elif valor > 0:
        valor = valor + (valor * 0.03) + (valor * 0.001 * atraso)
        return valor
    else:
        valor = 0
        return valor
    
def resultado(parcela, valor_atraso):
    novo_valor = valorPagamento(parcela, valor_atraso)
    print(f'O novo valor da parcela é {novo_valor}')

#Entrada e saída de dados

prestacoes = 100.0
while prestacoes > 0:
    os.system('clear')
    valor_prestacao = float(input('Digite: '))
    dias_atraso = int(input('Quantos dias em atraso: '))
    prestacoes = valor_prestacao
    resultado(valor_prestacao, dias_atraso)
    time.sleep(5)