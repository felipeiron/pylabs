import random
import os
os.system('clear')

def main():
    palavra = input('Informe uma string: ')
    print(embaralha_string(palavra))

def embaralha_string(palavra):
    lista_caracteres = list(palavra)
    random.shuffle(lista_caracteres)
    return ''.join(lista_caracteres).upper()

main()