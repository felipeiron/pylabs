import os
os.system('clear')

num_final = 0

for i in range(0, 5):
    num_input = float(input('Send a number: '))
    if num_input > num_final:
        num_final = num_input

print(f'The greater number is {num_final}')