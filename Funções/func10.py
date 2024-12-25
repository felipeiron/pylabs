import os, time, random
os.system('clear')

def dados():
    global dado1, dado2
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():   
    resultado = dados()
    print(f'O primeiro resultado dos dados {dado1} e {dado2} é igual {resultado}')
    if resultado == 7 or resultado == 11:
        print(f'Você venceu!!!')
    elif resultado == 2 or resultado == 3 or resultado == 12:
        print(f'Você perdeu!!!')
    else:
        print('Vamos continuar :D')
        while True:
            novo_resultado = dados()
            if novo_resultado == 7:
                print(f'VOCÊ PERDEU!!! O resultado dos dados {dado1} e {dado2} é igual {novo_resultado}')
                break
            elif novo_resultado == resultado:
                print(f'VOCÊ VENCEU!!! O resultado dos dados {dado1} e {dado2} é igual {novo_resultado}')
                break
            else:
                time.sleep(1)
                print(f'Vamos continuar!!! O resultado dos dados {dado1} e {dado2} é igual {novo_resultado}')         

iniciar = input('Deseja iniciar? S - N: ')
if iniciar.upper() == 'S':
    print('###### C R A P S ######')
    craps()
elif iniciar.upper() == 'N':
    print('O jogo não será iniciciado.')
else:
    print('Valor inválido! O jogo não será iniciciado.')