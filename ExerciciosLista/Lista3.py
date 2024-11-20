import os

os.system('clear')

notas = []

for i in range(1, 5):
    notas.append(float(input(f'Digite a nota {i}: ')))

print(f'As notas foram: {notas[0]}, {notas[1]}, {notas[2]} e {notas[3]}')
print(f'A média é {((sum(notas))/len(notas)):.2f}')