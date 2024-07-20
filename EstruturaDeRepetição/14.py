import os
os.system('clear')

print('### PAIR/ODD NUMBERS ###')
pair_num = 0
odd_num = 0
for i in range(0, 10):
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        pair_num += 1
    else:
        odd_num += 1

print(f'The amount of pair numbers is {pair_num} and odd numbers is {odd_num}.')