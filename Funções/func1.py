import os

os.system('clear')

def imprime_num(x):
    for linha in range(1, x+1):
        lista_num = []
        for rept in range(linha):
            lista_num.append(linha)
        print(" ".join(map(str, lista_num)))

num = int(input('Digite um número inteiro: '))
imprime_num(num)