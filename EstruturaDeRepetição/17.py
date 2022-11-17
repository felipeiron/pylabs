import os
os.system('clear')

print('### FACTORIAL ###\n')

num = int(input('Please, enter a integer: '))
fat = 1

for x in range(num):
    fat = fat * (num - x)
else:
    print(fat)