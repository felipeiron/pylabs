import os
os.system('clear')

print('### PAIRS or ODDS ###\n')
num_list = []
pair = 0
odd = 0
for x in range(10):
    num_list.append(int(input('Enter a integer: ')))
    if num_list[x] % 2 == 0:
        pair += 1
    else:
        odd += 1
else:
    print('\nList of numbers:',num_list)
    print('Pair numbers:', pair)
    print('Odd numbers:', odd)