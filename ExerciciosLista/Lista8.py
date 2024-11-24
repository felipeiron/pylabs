import os
import random

os.system('clear')

idade = []
altura = []

for i in range(0, 4):
    idade.append(random.randint(1, 100))
    altura.append(round(random.uniform(1.2, 2.1), 2))

print(f'Idades {idade} e alturas {altura}')
idade.reverse()
altura.reverse()
print(f'Idades {idade} e alturas {altura}')