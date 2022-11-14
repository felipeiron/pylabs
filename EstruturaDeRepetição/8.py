import os

os.system('clear')
l_num = []
print('### SUM AND AVERAGE ###\n')
for x in range(5):
    l_num.append(int(input('Enter a number: ')))
else:
    print('\nThe sum is', sum(l_num),'\nThe average is', sum(l_num)/5,'\n')