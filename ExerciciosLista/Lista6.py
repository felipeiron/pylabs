import os
import random

os.system('clear')

geral = []
media = []
cont = 0

#O loop abaixo armazena o número do aluno, as 4 notas e a média respectivamente.
for linha in range(1, 11):
    soma = 0
    alunos_notas = []
    alunos_notas.append(linha)
    for elemento in range(4):
        nota = random.randint(0, 10)
        alunos_notas.append(nota)
        soma += nota
    media.append(soma/4)
    alunos_notas.append(soma/4)
    geral.append(alunos_notas)
    if soma / 4 >= 7.0:
        cont += 1 


print("Essa é a lista de alunos, notas e médias:")
for aluno in geral:
    print(aluno)
    
print("Medias:")
print(media)
print(f"Média iguais ou maiores que 7: {cont}")