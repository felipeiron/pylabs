import os
import random
os.system("clear")

num = []
soma = 0
mult = 1

for i in range(0, 4):
    num.append(random.randint(0, 10))
    soma += num[i]
    mult *= num[i]

print(f'A soma é: {soma}')
print(f'A multiplicação é: {mult}')
print(f'A lista de números é: {num}')
