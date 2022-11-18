import os, random

os.system('clear')
print("### GERADOR DE NÚMEROS DA MEGA-SENA ###")

mega = []
for x in range(6):
    rand = random.randint(1,60)
    while rand in mega:
        rand = random.randint(1,60)
    else:
        mega.append(rand)        
else:
    mega = sorted(mega)
    print(mega)