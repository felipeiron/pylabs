import os
import locale
import calendar

os.system('clear')
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

def main():
    dia, mes, ano = input('Digite a data DD/MM/AAAA: ').split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if validar_data(dia, mes, ano) == True:
        converte(dia, mes, ano)
    else:
        print('Data inválida!')

def validar_data(dia, mes, ano):
    if 1 <= mes <= 12:
        _, dias_no_mes = calendar.monthrange(ano, mes)
        if 1 <= dia <= dias_no_mes:
            return True
        else:
            return False
    else:
        return False    

def converte(dia, mes, ano):
    nome_mes = calendar.month_name[mes]
    print(f'{dia} de {nome_mes} de {ano}')

main()