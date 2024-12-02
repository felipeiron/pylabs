import os, time

def conv_hora(nova_hora):
    global periodo
    if nova_hora > 12:
        nova_hora = nova_hora - 12
        periodo = 'P'
    else:
        periodo = 'A'
    return nova_hora

def resultado(hora):
    horario[0] = conv_hora(hora)
    if horario[1] < 10:
        horario[1] = '0'+str(horario[1])
    if periodo == 'P':
        print(f'A hora é {horario[0]}:{horario[1]} P.M.')
    else:
        if horario[0] < 10:
            horario[0] = '0'+str(horario[0])
        print(f'A hora é {horario[0]}:{horario[1]} A.M.')

#Entrada e saída de dados
while True:
    os.system('clear')

    print('### CONVERSÃO 24h/12h ###')
    horario = []
    horario.append(int(input('Digite o valor das horas: ')))
    horario.append(int(input('Digite o valor dos minutos: ')))
    resultado(horario[0])
    parar = str(input('Para para digite "s": '))
    if parar == "s" or parar == "S":
        break