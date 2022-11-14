import os
os.system('clear')

print('### MULTIPLICATION TABLE ###\n')
num = int(input('Enter a integer 1 - 10: '))
print('\nMultiplication table of', num)
for x in range(1, 11):
    print(num, 'x', x, '=', num * x)
