import os
os.system('clear')

print('### INTEGERS NUMBERS ###\n')
int1 = [int(input('Enter a integer: '))]
int1.append(int(input('Enter a integer: ')))
int1 = sorted(int1)

for x in range(int1[0],int1[1]+1):
    print(x)